# PrSeo7

Source of <https://prseo7.github.io>, the website for PrSeo7's iOS and Android
apps. Served by GitHub Pages, which builds it with Jekyll (primer theme).

## Layout

| Path | What it is |
|---|---|
| `index.html` | Home page. Standalone (`layout: null`); uses the shared includes. |
| `jlpt-vocab-master/`, `easyvocab/`, `provocab/`, `tabata-timer/`, `ko/easyvocab/` | App landing pages. All content lives in each `index.html` front matter and is rendered by `_layouts/app.html`. |
| `_layouts/app.html`, `_data/app_labels.yml` | App page template and its per-language UI labels. |
| `_includes/` | Shared head, GA4 (loaded only after cookie consent) and the cookie banner. |
| `easy_vocab/`, `jlptn3word200/`, `neko_japanese/`, `pro_vocab/`, `tabata_timer/` | Each app's `PRIVACY_POLICY.md`, published at `/<folder>/PRIVACY_POLICY`. These are copies: edit the policy in the app's own repo, then copy it here. Their meta descriptions are in `_config.yml`, not in the files. |
| `_config.yml` | Only per-folder `defaults` (policy meta descriptions). GitHub Pages supplies the theme and plugins; re-check the build before adding `theme:` or `plugins:`. |
| `privacy-policy/` | Privacy policy for this website. |
| `images/`, `assets/` | Store badges, app icons and screenshots, OG image, CSS. |
| `sitemap.xml`, `robots.txt`, `app-ads.txt` | Crawler and ad-network files. |
| `google*.html`, `naver*.html` | Search Console / Naver Search Advisor verification. Do not delete. |
| `_tools/` | `check-site.py` (validates a built `_site/`), `make-app-images.sh`, `make-og-image.sh`. |
| `_docs/` | SEO audit notes, design specs and plans. |

Folders starting with `_` are not published.

## Checking a change

Build with the `github-pages` gem, running from the directory that holds its
Gemfile (otherwise the gem's GitHub Pages defaults are not applied):
`PAGES_REPO_NWO=PrSeo7/PrSeo7 JEKYLL_ENV=production bundle exec jekyll build -s <repo> -d <out>`,
then run `_tools/check-site.py <out>`. Without a GitHub API token the local
build uses `https://github.com/pages/PrSeo7/PrSeo7` as the site URL, so the
checker reports broken `style.css` links on the primer pages; compare against
a build of the previous commit rather than expecting zero failures.
