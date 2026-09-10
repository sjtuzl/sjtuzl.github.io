#!/bin/bash
# xhs.sh — generate Xiaohongshu (小红书) draft material for a blog post.
#
# Produces, under xhs-output/<slug>/ : a paste-ready copy.txt (<=20-char title,
# opening hook, CTA, hashtags) and a set of 1080x1440 theme cards (cover +
# opening + CTA). Nothing is posted — you upload the cards and paste the text
# into Xiaohongshu yourself and save it as a draft.
#
# Usage:  ./xhs.sh _posts/2026-09-03-Why-Greatness-Cannot-Be-Planned.md
set -e
cd "$(dirname "$0")"

if [ -z "$1" ]; then
  echo "usage: ./xhs.sh <path/to/_posts/YYYY-MM-DD-slug.md>"
  echo "example: ./xhs.sh _posts/2026-09-03-Why-Greatness-Cannot-Be-Planned.md"
  exit 1
fi

exec python3 xhs.py "$@"
