#!/usr/bin/env python3
"""Checks a built prseo7.github.io site (Jekyll _site/ directory).

Usage: _tools/check-site.py <site_dir>

App pages: title <= 60 chars, meta description <= 155, canonical, one <h1>,
JSON-LD parses and has MobileApplication + FAQPage + BreadcrumbList, FAQ
count matches the visible FAQ, hreflang pairs are reciprocal, no Font
Awesome, no banned wording. All pages: internal links and images resolve.
Homepage: not wrapped in the primer layout, has the cookie banner, links
to every app page. Exits 1 on any failure.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://prseo7.github.io"
APP_PAGES = ["/jlpt-vocab-master/", "/easyvocab/", "/provocab/", "/tabata-timer/", "/ko/easyvocab/"]
BANNED = [r"native speaker", r"원어민", r"\bpreset", r"\$\d", r"￦\d", r"AdMob", r"LevelPlay"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self.meta, self.links, self.refs = "", {}, [], []
        self.jsonld, self.h1, self.faq_items = [], 0, 0
        self._in_title = self._in_jsonld = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
            if a.get("rel") not in ("canonical", "alternate", "preconnect", "dns-prefetch"):
                self.refs.append(a.get("href"))
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld, self._buf = True, ""
        elif tag == "h1":
            self.h1 += 1
        if tag in ("a",):
            self.refs.append(a.get("href"))
        if tag in ("img", "source", "script"):
            self.refs.append(a.get("src"))
            self.refs.extend(c.split()[0] for c in (a.get("srcset") or "").split(",") if c.strip())
        if "faq-item" in (a.get("class") or "").split():
            self.faq_items += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self.jsonld.append(self._buf)
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf += data


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


def resolves(site, page_path, ref):
    if not ref or ref.startswith(("http:", "https:", "mailto:", "#", "data:", "//")):
        return True
    ref = ref.split("#")[0].split("?")[0]
    if not ref:
        return True
    base = site if ref.startswith("/") else page_path.parent
    target = (base / ref.lstrip("/")).resolve()
    return target.is_file() or (target / "index.html").is_file() or target.with_suffix(".html").is_file()


def main(site_dir):
    site = Path(site_dir).resolve()
    errors = []

    def err(where, msg):
        errors.append(f"{where}: {msg}")

    alternates = {}
    for url in APP_PAGES:
        f = site / url.strip("/") / "index.html"
        if not f.exists():
            err(url, "page missing")
            continue
        p = parse(f)
        if not p.title or len(p.title) > 60:
            err(url, f"title length {len(p.title)} (1-60): {p.title!r}")
        desc = p.meta.get("description", "")
        if not desc or len(desc) > 155:
            err(url, f"description length {len(desc)} (1-155)")
        canon = [l.get("href") for l in p.links if l.get("rel") == "canonical"]
        if canon != [SITE + url]:
            err(url, f"canonical {canon}")
        if p.h1 != 1:
            err(url, f"{p.h1} <h1> elements")
        types, faq_count = set(), 0
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(url, f"JSON-LD does not parse: {e}")
                continue
            roots = data if isinstance(data, list) else [data]
            nodes = [n for r in roots if isinstance(r, dict) for n in r.get("@graph", [r])]
            for node in nodes:
                t = node.get("@type")
                types.update(t if isinstance(t, list) else [t])
                if "FAQPage" in (t if isinstance(t, list) else [t]):
                    faq_count = len(node.get("mainEntity", []))
        for t in ("MobileApplication", "FAQPage", "BreadcrumbList"):
            if t not in types:
                err(url, f"JSON-LD missing {t}")
        if faq_count == 0 or faq_count != p.faq_items:
            err(url, f"FAQ JSON-LD {faq_count} vs visible {p.faq_items}")
        alternates[url] = {l.get("hreflang"): l.get("href") for l in p.links if l.get("rel") == "alternate"}
        text = f.read_text(encoding="utf-8")
        if re.search(r"font-?awesome|\bfa-[a-z]", text):
            err(url, "Font Awesome reference")
        for pattern in BANNED:
            if re.search(pattern, text, re.IGNORECASE):
                err(url, f"banned wording /{pattern}/")

    for url, alts in alternates.items():
        for lang, href in alts.items():
            other = href.replace(SITE, "") if href else ""
            if lang == "x-default":
                continue
            if other not in alternates:
                err(url, f"hreflang {lang} -> {href} is not an app page")
            elif SITE + url not in alternates[other].values():
                err(url, f"hreflang {lang} -> {href} is not reciprocal")
    for url in ("/easyvocab/", "/ko/easyvocab/"):
        if url in alternates and not alternates[url]:
            err(url, "no hreflang alternates")

    home = site / "index.html"
    home_text = home.read_text(encoding="utf-8")
    if "container-lg" in home_text:
        err("/", "wrapped in the primer layout (front matter needs layout: null)")
    if 'id="cookie-consent"' not in home_text or "window.loadAnalytics" not in home_text:
        err("/", "cookie banner or analytics loader missing")
    for url in APP_PAGES[:4]:
        if f'href="{url}"' not in home_text:
            err("/", f"no link to {url}")

    for f in sorted(site.rglob("*.html")):
        if f.name.startswith("google"):
            continue
        for ref in parse(f).refs:
            if not resolves(site, f, ref):
                err(str(f.relative_to(site)), f"broken reference {ref}")

    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "_site"))
