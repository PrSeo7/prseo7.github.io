# App landing pages — design (2026-09-30)

Implements SEO audit 2순위 (`_docs/seo-audit-2026-09-30.md`) plus the GEO 1·2순위
items that live on app pages (one-sentence definition, FAQ, `SoftwareApplication`
JSON-LD, last-updated date).

## Scope

In:
- Four English app pages: `/jlpt-vocab-master/`, `/easyvocab/`, `/provocab/`, `/tabata-timer/`.
- One Korean page: `/ko/easyvocab/` (App Store Korean name "수능 영단어 – EasyVocab"; the audit doc's "오늘의 영단어" was wrong), linked to `/easyvocab/` with hreflang.
- Homepage app cards link to the pages and show real app icons; store-badge alt text names the app.
- Sitemap entries; site privacy policy scope sentence updated to cover the new pages.

Out (separate tasks):
- Homepage repositioning (title, H1, description, Organization JSON-LD, `serviceType`/`hasOfferCatalog`).
- Korean pages for the other apps, Naver registration (3순위).
- Moving or renaming the existing `/<app>/PRIVACY_POLICY` URLs — apps link to them.

## Source of facts

Every factual claim (word counts, levels, price, platforms, languages, free vs premium,
offline, account) comes from the app repo, and each repo's wording rules apply:

| Page | Repo | Store text |
|---|---|---|
| jlpt-vocab-master | `~/workspace/prseo7/jlpt_n3_words` | `playstore.html`, `appstore_de.html`, `CLAUDE.md`, code |
| easyvocab, ko/easyvocab | `~/workspace/prseo7/hello_english` | `APP_STORE_DESCRIPTIONS.md` |
| provocab | `~/workspace/prseo7/pro_vocab` | `APP_STORE_DESCRIPTION_KO.md` (source of truth), `APP_STORE_DESCRIPTIONS.md` |
| tabata-timer | `~/workspace/prseo7/tabata_timer` | no store file — `README.md`, `lib/`, l10n strings |

Rules:
- Audio is described the way the repo describes it (ProVocab: AI voice, never "native speaker").
  The audit doc's example sentence ("원어민 음성") is not used.
- Each fact is cross-checked against the live App Store / Google Play listing before it is written.
  A fact goes on a page only when the code and the live store agree; where they disagree, the
  page leaves the fact out and the mismatch is reported (e.g. Tabata: store still says "Contains
  ads" / "Remove all ads" but the ad SDK was removed 2026-09-13 → the page says nothing about ads).
- No price amount on any page: "one-time purchase" only. The store sets regional prices, and the
  ProVocab repo rule forbids exact Premium prices (Apple 3.1.1); applied to every app for consistency.
  JSON-LD `offers` states only the free download (price 0).
- Store links: ProVocab is not released on Google Play yet (confirmed 2026-09-30) — iOS link only, `os: ["iOS"]`;
  add the Play link when it ships.
- Privacy/data FAQ answers summarize the app's own `PRIVACY_POLICY.md` "short version" and link to it.
  No deletion promises for Firebase data; no statement that contradicts the policy.

## Page structure (top to bottom)

1. Site bar: "PrSeo7" → `/`, "Apps" → `/#products`.
2. Hero: app icon, H1 = store app name, one-sentence definition (what, for whom, key number,
   platforms, price model), store badges with alt "Download <App> on the App Store / Google Play".
3. Screenshots: horizontal scroll strip, 3–5 images, `loading="lazy"`, explicit width/height, descriptive alt.
   Section is omitted when `screenshots` is empty.
4. Features: bullet list from the store description.
5. How it works: 3–4 short steps.
6. Free vs Premium: two-column table, "one-time purchase" without an amount (omitted for apps without premium).
7. FAQ: 5–7 questions (free? offline? account? who is it for? where is my data?).
8. Footer: "Last updated YYYY-MM-DD", app privacy policy, site privacy policy, Cookie Settings button, other apps.

Body text target: 300–800 words. Visual style follows the homepage (purple `#667eea` accent,
Inter font, cards) but content-first on a light background. No Font Awesome.

## Files

```
_layouts/app.html              full page: <head>, sections, JSON-LD
_includes/site-head.html       favicons, manifest, theme-color, fonts (shared with index.html)
_includes/analytics.html       GA4 consent-mode block, moved verbatim from index.html
_includes/cookie-banner.html   banner markup + script, moved verbatim from index.html
assets/css/app.css             app page styles
images/apps/<slug>/icon.webp, icon.png (256px), screenshot-<n>.webp (390px wide)
images/apps/<slug>/raw/        originals copied by Claude from ~/Documents/prseo7/*_screenshot; git-ignored, excluded from the build
_tools/make-app-images.sh      icon (from app repo 1024px PNG) + raw screenshots → WebP/PNG
jlpt-vocab-master/index.html   front matter only (same for the other four pages)
```

`index.html` gains an empty front matter block so Jekyll processes it and it can use the
includes. The GA4 and cookie-banner code is replaced by the includes with identical behaviour
(verified by diffing the built `_site/index.html` against the current file: only the intended
card/alt changes may differ). `page_title` in the GA config comes from the page.

The layout does not use the primer theme. No `_config.yml` is added; `layout: app` in front matter is enough.
If `raw/` exclusion needs config, add a minimal `_config.yml` with `exclude:` and keep `theme` unchanged,
then check the privacy pages still render with primer.

## Front matter schema

```yaml
layout: app
lang: en                     # en | ko
permalink: /easyvocab/
title: "EasyVocab – English Vocabulary App | PrSeo7"       # ≤ 60 chars
description: "..."                                        # ≤ 155 chars
app_name: "EasyVocab – English Vocabulary"
slug: easyvocab               # images/apps/<slug>/
definition: "..."             # one sentence, shown in hero and used as JSON-LD description
category: EducationalApplication   # or HealthApplication
os: ["iOS", "Android"]
stores:
  ios: https://apps.apple.com/...
  android: https://play.google.com/...    # omit when not on Play
features: ["...", "..."]
steps: ["...", "..."]
premium:                      # omit when the app has no premium
  free: ["..."]
  paid: ["..."]
faq:
  - q: "..."
    a: "..."
screenshots:
  - src: /images/apps/easyvocab/screenshot-1.webp
    alt: "..."
privacy_url: /easy_vocab/PRIVACY_POLICY.html
last_updated: 2026-09-30
alternate:                    # hreflang; only EasyVocab pages
  en: /easyvocab/
  ko: /ko/easyvocab/
identifiers:                  # disambiguation (GEO), shown in the footer
  app_store_id: "6757153410"
  ios_bundle: com.prseo7.helloEnglish
  android_package: com.prseo7.hello_english
```

UI strings (section headings, badge labels, footer, cookie banner) come from `_data/app_labels.yml`
keyed by `page.lang`, so adding languages later is data-only.

Additional fields: `alternate_name` (EasyVocab en/ko cross-names), `app_languages` (JSON-LD
`inLanguage`), `screenshots[].width/height`, and `identifiers` = `app_store_id`, `ios_bundle`,
`android_package` (each optional).

## Head and structured data

- `<html lang>`, title, description, canonical (`https://prseo7.github.io` + permalink),
  og:* / twitter:* (image = app icon PNG, `summary` card), hreflang + x-default (= en) when `alternate` is set.
- JSON-LD, generated from the same front matter with `jsonify`:
  - `MobileApplication`: name, description = definition, operatingSystem, applicationCategory,
    offers `{price: 0, priceCurrency: USD}`, inLanguage, downloadUrl, image, author/publisher →
    `{"@id": "https://prseo7.github.io/#organization"}`. No `aggregateRating`.
  - `FAQPage` from `faq`.
  - `BreadcrumbList`: Home → App.
- The homepage Organization JSON-LD gets `"@id": "https://prseo7.github.io/#organization"` (only this
  change; the rest of the repositioning is out of scope).

## Other changes

- Homepage cards: title and icon link to the app page; `<i class="fas …">` replaced by the app icon
  `<img>` (webp with png fallback, width/height set); badge alt text names the app.
- `sitemap.xml`: add the five URLs with `lastmod`; EasyVocab pair gets `xhtml:link` hreflang
  (en, ko, x-default) and the `xmlns:xhtml` namespace.
- `privacy-policy/index.md`: scope sentence "the home page and this page" → covers the app pages too.
  Shown to Sangwon before saving.
- `.gitignore`: `images/apps/*/raw/`.
- Audit doc: tick 2순위 page item (and 4순위 badge alt) with the date; note which GEO 1·2 items are done.

## Verification

- `bundle exec jekyll build` using the `github-pages` gem via a Gemfile in the scratchpad (not committed).
- Each page in `_site/`: JSON-LD blocks parse as JSON; title ≤ 60, description ≤ 155; every internal
  link and image resolves (local crawl); no Font Awesome reference.
- Built `index.html` diff vs. current: only the intended changes; cookie banner accept/decline/settings
  still works (manual check in a browser via `jekyll serve`).
- Facts table: for each page, list each fact with its repo/store source, included in the handoff message.
- After Sangwon pushes: Rich Results Test per page, Search Console URL inspection + sitemap resubmit.
  These are listed in the audit doc as Sangwon's steps.

## Screenshots

The first five App Store iPhone screenshots (1290×2796) per app, copied from
`/Users/sangwon/workspace/prseo7/claude-cowork/*_screenshot/` (moved there from `~/Documents/prseo7/`
on 2026-09-30) into `images/apps/<slug>/raw/`; the Korean EasyVocab page uses the `appstore_ko` set.
