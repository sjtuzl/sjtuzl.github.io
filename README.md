# Ling Zhang's Blog — sjtuzl.github.io

Static blog on GitHub Pages, migrated from the WordPress site at
`zhangling.org/blog`. Built with Jekyll and deployed by **classic GitHub Pages
("Deploy from a branch")** — the server builds its own copy on push; the local
`Gemfile`/`_site` are only for local preview and are not deployed.

## Structure

| Path | Purpose |
|------|---------|
| `_layouts/`, `_includes/` | Global page chrome (header/topbar, footer, giscus). **Restyle the whole blog by editing these + `assets/css/style.css` only** — posts carry no styling of their own. |
| `assets/css/style.css` | Single global stylesheet (Twenty Twenty look). |
| `assets/js/i18n.js` | Client-side EN/中文 UI toggle (see below). |
| `assets/js/topbar.js` | Reveals the sticky bar's mini avatar once the banner scrolls away. |
| `assets/media/` | Migrated images & attachments (`uploads/`, `photos/`, `files/`, `special/`, `images/`). |
| `_posts/*.md` | All posts, in one folder (`YYYY-MM-DD-slug.md`). |
| `index.html` | Paginated home (10/page); can hide pre-cutoff posts (see *Hiding old posts*). |
| `archive.html` | Full archive grouped by year (by post `date`, not folders); respects the legacy toggle. |
| `about.html`, `404.html`, `special/` | Static pages. |
| `_config.yml` | Site config: permalink, pagination, giscus keys, post `defaults`, and the `show_legacy` toggle. |
| `start.sh` | One-command local build/preview. |
| `admin/index.html` | Browser-based post editor — publish from any device with no local tools (see *Publishing from a browser*). |
| `xhs.sh`, `xhs.py` | Generate Xiaohongshu (小红书) draft material for a post (see *Xiaohongshu cards*). |

Posts get their URL from their `date` + the global
`permalink: /:year:month:day/:title.html` rule — **not** from their folder, so
every post lives directly in `_posts/`. Migration scripts live outside this repo
in `../migrate/`.

## Writing a new post

Create one file `_posts/YYYY-MM-DD-slug.md` — no directories, minimal front
matter (`layout`/`has_comments` come from `_config.yml` `defaults`):

```markdown
---
title: My new post title
date: 2026-08-19 15:30:00 +0800
---
Write the body in Markdown…

<!--more-->   <!-- optional: cut the home-feed excerpt here -->
```

The URL becomes `/20260819/slug.html` automatically. You can also create the
file directly on github.com — committing to the default branch auto-deploys.

## Publishing from a browser (`/admin/`)

`admin/index.html` is a self-contained page (no server, no third-party service)
for writing a post from **any device's browser** — a phone or a borrowed PC with
no VS Code or git. Open `https://sjtuzl.github.io/admin/`, paste a GitHub
**fine-grained token** once (scope: this repo only, **Contents: Read and write**),
then fill a form (title / date / slug / body) and upload images. On *发布* it
creates `_posts/YYYY-MM-DD-slug.md` (and commits any images to `assets/`) through
the GitHub Contents API. Currently supports **creating** posts, not editing old
ones.

The token is stored in the browser's `localStorage` and never leaves the device;
a repo-scoped token limits the blast radius to this one repo. Use the
*退出/清除钥匙* button to wipe it on a shared machine.

## Xiaohongshu cards (`xhs.sh`)

`./xhs.sh _posts/<file>.md` turns a post into ready-to-post Xiaohongshu (小红书)
material — a paste-ready `copy.txt` (≤20-char title, opening hook, CTA, tags) and
a set of 1080×1440 theme cards (cover + opening + CTA) rendered from the blog's
beige theme via headless Chrome. Output lands in `xhs-output/<slug>/`
(git-ignored). Nothing is posted; you upload the cards and paste the text into
Xiaohongshu yourself. Tunable constants (title/body limits, card count) are at the
top of `xhs.py`.

## Hiding old posts (`show_legacy`)

Two keys in `_config.yml` control whether pre-cutoff posts appear on the **home
feed and archive**:

```yaml
show_legacy: false   # false = hide old posts; true = show everything
legacy_before: 2026  # a post whose year is < this is "legacy"
```

With `show_legacy: false`, the home feed and archive show only posts from
`legacy_before` onward (and the home pager is hidden, since only recent posts
remain). Flip to `true` to bring everything back — post URLs are unchanged
throughout (each post pins its own `permalink`). Takes effect on the next
build/push.

This is **list-level filtering only**: hidden posts' individual pages are still
generated (reachable by direct URL) and still appear in `feed.xml` and
`sitemap.xml`. It declutters browsing, not search-engine/RSS discoverability.

## Local preview

Local dev uses modern Jekyll 4.x (works on current Ruby). The **live** site is
built separately by classic GitHub Pages, which ignores this Gemfile, so the two
are decoupled.

```sh
./start.sh          # build + serve at http://localhost:4000 (live reload)
./start.sh --build  # one-off build into _site/ and exit
```

`start.sh` installs gems on first run and uses the `bin/jekyll` binstub rather
than `bundle exec jekyll` (a Bundler 4.0 quirk can fail to resolve the
executable; the binstub is reliable). `_site/` is generated output and is
git-ignored.

## Language toggle (English / 简体中文)

The page HTML ships in **English** (correct default for English readers and
no-JS visitors). `assets/js/i18n.js` swaps the site *chrome* (nav, headings,
footer, pagination, section labels) to Chinese when the visitor clicks
**中文** in the top bar; the choice is stored in `localStorage` and also
settable via `?lang=zh`. Blog post bodies keep their original language.

Translatable UI carries `data-i18n` / `data-i18n-tpl` attributes; the EN/ZH
strings live in the `DICT` map in `i18n.js`. Archived-comment labels baked into
posts are translated by class selector, so adding a post needs no i18n edits.

## Comments

Historical comments are baked into each post as read-only static HTML. New
comments use [giscus](https://giscus.app) (GitHub Discussions): enable repo
**Discussions**, register giscus, fill the `giscus.*` keys in `_config.yml`, and
set `enabled: true`.
