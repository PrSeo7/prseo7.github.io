#!/usr/bin/env bash
# Builds the web images for the app landing pages under images/apps/<slug>/:
#   icon.png + icon.webp (256x256) from each app repo's 1024px iOS icon, and
#   screenshot-<n>.webp (390px wide) from images/apps/<slug>/raw/*.png, in name order.
# raw/ is git-ignored. Prints each screenshot's size for the page front matter.
# Requires ImageMagick 7 and cwebp. _tools/ is not published by Jekyll.
set -euo pipefail

cd "$(dirname "$0")/.."

APPS=/Users/sangwon/workspace/prseo7
ICON=ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-1024x1024@1x.png

icon() {  # <slug> <app repo>
  local out=images/apps/$1
  mkdir -p "$out"
  magick "$APPS/$2/$ICON" -resize 256x256 -strip -define png:compression-level=9 "$out/icon.png"
  cwebp -quiet -q 90 "$out/icon.png" -o "$out/icon.webp"
  magick identify -format '%f %wx%h %b\n' "$out/icon.png" "$out/icon.webp"
}

screenshots() {  # <slug>
  local out=images/apps/$1 n=0 f
  [ -d "$out/raw" ] || return 0
  rm -f "$out"/screenshot-*.webp
  for f in "$out"/raw/*.png; do
    [ -e "$f" ] || continue
    n=$((n + 1))
    cwebp -quiet -q 82 -resize 390 0 "$f" -o "$out/screenshot-$n.webp"
    magick identify -format "$out/screenshot-$n.webp %wx%h %b\n" "$out/screenshot-$n.webp"
  done
}

icon jlpt-vocab-master jlpt_n3_words
icon easyvocab hello_english
icon provocab pro_vocab
icon tabata-timer tabata_timer
icon easyvocab-ko hello_english   # the Korean page's own image dir

for slug in jlpt-vocab-master easyvocab easyvocab-ko provocab tabata-timer; do
  screenshots "$slug"
done
