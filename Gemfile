source "https://rubygems.org"

# Local development uses modern Jekyll 4.x, which runs on current Ruby (4.0).
# The LIVE site is built by classic GitHub Pages ("Deploy from a branch") in
# GitHub's own server environment, which ignores this Gemfile — so the two are
# decoupled. Our plugins are all on the GitHub Pages safelist, so the server
# build produces the same output.
gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-paginate"
  gem "jekyll-feed"
  gem "jekyll-sitemap"
end

# Standard-library gems unbundled from Ruby 3.4+ (needed by the toolchain).
gem "webrick"
gem "csv"
gem "bigdecimal"
gem "base64"
gem "logger"
