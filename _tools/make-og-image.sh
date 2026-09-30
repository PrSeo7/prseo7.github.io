#!/usr/bin/env bash
# Builds images/prseo7-og-image.png (1200x630), the link-preview image that
# index.html's og:image and twitter:image point to. Requires ImageMagick 7.
# Re-run after changing the logo or the text, then refresh the preview caches
# (Kakao sharing debugger, Facebook Sharing Debugger).
# _tools/ starts with an underscore, so Jekyll does not publish it.
set -euo pipefail

cd "$(dirname "$0")/.."

LOGO=images/screen.png
OUT=images/prseo7-og-image.png
FONT_BOLD="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR="/System/Library/Fonts/Supplemental/Arial.ttf"
ACCENT="#667eea"   # theme-color in index.html
TEXT="#1f2937"
MUTED="#6b7280"

magick -size 1200x630 xc:white \
  \( "$LOGO" -fuzz 8% -fill white -opaque white -resize 440x440 \) -geometry +80+95 -composite \
  -font "$FONT_BOLD" -fill "$TEXT" -pointsize 96 -annotate +580+270 "PrSeo7" \
  -fill "$ACCENT" -draw "rectangle 584,300 704,308" \
  -font "$FONT_REGULAR" -fill "$TEXT" -pointsize 38 -annotate +580+370 "Backend & Mobile App" \
  -annotate +580+418 "Development" \
  -fill "$MUTED" -pointsize 30 -annotate +580+490 "prseo7.github.io" \
  +dither -colors 128 -strip -define png:compression-level=9 "$OUT"

magick identify -format '%f %wx%h %b\n' "$OUT"
