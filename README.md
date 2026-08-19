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
| `index.html` | Paginated home (10/page). |
| `archive.html` | Full archive grouped by year (by post `date`, not folders). |
| `about.html`, `404.html`, `special/` | Static pages. |
| `_config.yml` | Site config: permalink, pagination, giscus keys, post `defaults`. |
| `start.sh` | One-command local build/preview. |

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
