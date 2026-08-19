#!/usr/bin/env bash
# start.sh — build and preview the blog locally with Jekyll.
#
#   ./start.sh          # serve at http://localhost:4000 with live reload
#   ./start.sh --build  # one-off build into _site/ and exit (no server)
#
# Uses the project's binstub (bin/jekyll) so it works with Ruby 4.0 /
# Bundler 4.0, where `bundle exec jekyll` is unreliable.
set -euo pipefail

cd "$(dirname "$0")"

# Install gems on first run (or after Gemfile changes).
if [ ! -d vendor/bundle ] && ! bundle check >/dev/null 2>&1; then
  echo "Installing gems (first run)…"
  bundle install
fi

# Make sure the binstub exists.
if [ ! -x bin/jekyll ]; then
  echo "Creating jekyll binstub…"
  bundle binstubs jekyll --force
fi

if [ "${1:-}" = "--build" ]; then
  exec bin/jekyll build
fi

echo "Serving at http://localhost:4000  (Ctrl-C to stop)"
exec bin/jekyll serve --livereload "$@"
