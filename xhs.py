#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xhs.py — turn a blog post into Xiaohongshu (小红书) draft material.

Strategy (agreed with the author): "开头引流" — the note shows only the
opening of the article as a hook and points readers to the full text on the
blog. For each post this produces, under xhs-output/<slug>/ :

  * copy.txt   — paste-ready note: <=20-char title, hook body, CTA, hashtags.
  * card-NN.png — a cover card + 1-2 opening cards + a CTA card, rendered from
                  the blog's beige theme at 1080x1440 (Xiaohongshu 3:4).

Cards are HTML rendered to PNG via the installed headless Google Chrome, so
Chinese type uses the system PingFang SC and looks native. Nothing is posted
anywhere — the author saves the draft by hand (Xiaohongshu has no personal
publishing API), keeping full editorial control and zero account risk.

Usage:  python3 xhs.py _posts/2026-09-03-Why-Greatness-Cannot-Be-Planned.md
        (normally invoked through ./xhs.sh)
"""

import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# ---- theme (mirrors assets/css/style.css :root) --------------------------
BG = "#f4ecdd"        # beige reading surface
TEXT = "#202020"
MUTED = "#6d6d6d"
ACCENT = "#cd2653"
FONT = ('-apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", '
        '"Microsoft YaHei", sans-serif')

# ---- Xiaohongshu limits / layout -----------------------------------------
TITLE_MAX = 20        # note title display limit (full-width chars)
BODY_MAX = 900        # keep the whole note comfortably under the ~1000 cap
CARD_W, CARD_H = 1080, 1440
CARD_CHARS = 200      # rough CJK chars per opening card
MAX_OPENING_CARDS = 2 # "开头引流": show only the opening, not the whole piece

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# ---- parsing -------------------------------------------------------------
def load_post(path: Path):
    raw = path.read_text(encoding="utf-8")
    title, body = "", raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[3:end]
            body = raw[end + 4:]
            m = re.search(r'(?m)^\s*title:\s*(.+?)\s*$', fm)
            if m:
                title = m.group(1).strip().strip('"').strip("'")
    return title, body


def opening_text(body: str) -> str:
    """Clean the article's opening into plain text suitable for Xiaohongshu."""
    # Only the intro (before the excerpt separator) is the natural "opening".
    body = body.split("<!--more-->", 1)[0]
    # Chinese audience: drop an English-translation section if present.
    body = re.split(r'\*{0,2}English\s+[Tt]ranslation', body, maxsplit=1)[0]
    # Strip HTML, markdown images, and turn links into their text.
    body = re.sub(r'<[^>]+>', '', body)
    body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', body)
    body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    # Drop emphasis / heading / quote / list markers, keep the words.
    body = re.sub(r'(?m)^\s{0,3}#{1,6}\s*', '', body)
    body = re.sub(r'(?m)^\s{0,3}>\s?', '', body)
    body = re.sub(r'(?m)^\s{0,3}[-*+]\s+', '• ', body)
    body = body.replace("**", "").replace("__", "").replace("`", "")
    paras = [re.sub(r'\s+', ' ', p).strip()
             for p in re.split(r'\n\s*\n', body) if p.strip()]
    return "\n\n".join(paras)


def clip_chars(text: str, limit: int) -> str:
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "…"


def chunk_paras(text: str, size: int, max_chunks: int):
    """Pack paragraphs into cards of ~size chars; split any over-long one."""
    cards, cur = [], ""
    for para in text.split("\n\n"):
        while len(para) > size:                       # a very long paragraph
            cut = para.rfind("。", 0, size) + 1 or size
            piece, para = para[:cut], para[cut:]
            if cur:
                cards.append(cur); cur = ""
            cards.append(piece)
        if not cur:
            cur = para
        elif len(cur) + 1 + len(para) <= size:
            cur += "\n\n" + para
        else:
            cards.append(cur); cur = para
    if cur:
        cards.append(cur)
    return cards[:max_chunks]


# ---- card HTML -----------------------------------------------------------
def page_html(inner: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{CARD_W}px;height:{CARD_H}px;overflow:hidden}}
body{{background:{BG};color:{TEXT};font-family:{FONT};
  padding:96px 90px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;
  color:{MUTED};font-size:30px;letter-spacing:.02em}}
.brand{{font-weight:600}}
.dot{{color:{ACCENT}}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.title{{font-size:76px;font-weight:700;line-height:1.28;
  letter-spacing:.01em}}
.date{{margin-top:28px;color:{MUTED};font-size:34px}}
.body{{font-size:44px;line-height:1.75;white-space:pre-wrap}}
.body p{{margin-bottom:28px}}
.cta-big{{font-size:60px;font-weight:700;line-height:1.4}}
.cta-big .u{{color:{ACCENT}}}
.cta-sub{{margin-top:36px;font-size:38px;color:{MUTED};line-height:1.6}}
.foot{{color:{MUTED};font-size:30px;display:flex;
  justify-content:space-between;align-items:center}}
.rule{{width:64px;height:6px;background:{ACCENT};border-radius:3px;
  margin-bottom:40px}}
</style></head><body>{inner}</body></html>"""


def cover_card(title, date, n):
    return page_html(f"""
<div class="top"><span class="brand"><span class="dot">●</span> 张岭的博客</span>
  <span>1 / {n}</span></div>
<div class="mid"><div class="rule"></div>
  <div class="title">{html.escape(title)}</div>
  <div class="date">{html.escape(date)}</div></div>
<div class="foot"><span>全文见主页链接 →</span><span>sjtuzl.github.io</span></div>""")


def body_card(paras, idx, n):
    ps = "".join(f"<p>{html.escape(p)}</p>" for p in paras.split("\n\n"))
    return page_html(f"""
<div class="top"><span class="brand"><span class="dot">●</span> 张岭的博客</span>
  <span>{idx} / {n}</span></div>
<div class="mid"><div class="body">{ps}</div></div>
<div class="foot"><span>全文见主页链接 →</span><span>sjtuzl.github.io</span></div>""")


def cta_card(title, url, n):
    return page_html(f"""
<div class="top"><span class="brand"><span class="dot">●</span> 张岭的博客</span>
  <span>{n} / {n}</span></div>
<div class="mid">
  <div class="cta-big">想读全文？<br>点主页链接看 <span class="u">《{html.escape(title)}》</span></div>
  <div class="cta-sub">🔗 {html.escape(url)}<br>📌 链接在个人主页简介 / 评论区</div></div>
<div class="foot"><span>关注 张岭的博客</span><span>技术 · 工作 · 生活</span></div>""")


# ---- render --------------------------------------------------------------
def render(cards_html, out_dir: Path):
    if not Path(CHROME).exists():
        sys.exit(f"error: Google Chrome not found at:\n  {CHROME}\n"
                 "Install Chrome or edit CHROME in xhs.py.")
    pngs = []
    with tempfile.TemporaryDirectory() as td:
        for i, doc in enumerate(cards_html, 1):
            src = Path(td) / f"card-{i:02d}.html"
            src.write_text(doc, encoding="utf-8")
            out = out_dir / f"card-{i:02d}.png"
            subprocess.run([
                CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--window-size={CARD_W},{CARD_H}",
                f"--screenshot={out}", src.as_uri(),
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pngs.append(out)
    return pngs


def blog_url() -> str:
    cfg = Path(__file__).with_name("_config.yml")
    if cfg.exists():
        m = re.search(r'(?m)^\s*url:\s*["\']?([^"\'\s]+)', cfg.read_text("utf-8"))
        if m:
            return m.group(1).rstrip("/")
    return "https://sjtuzl.github.io"


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 xhs.py <path/to/_posts/YYYY-MM-DD-slug.md>")
    post = Path(sys.argv[1])
    if not post.exists():
        sys.exit(f"error: no such file: {post}")

    title, body = load_post(post)
    if not title:
        title = post.stem
    date = ""
    m = re.match(r'(\d{4}-\d{2}-\d{2})', post.stem)
    if m:
        date = m.group(1)

    opening = opening_text(body)
    if not opening:
        sys.exit("error: could not extract any opening text from the post.")

    url = blog_url().replace("https://", "").replace("http://", "")
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', post.stem)
    out_dir = Path(__file__).with_name("xhs-output") / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    # ---- copy.txt (paste-ready note) ----
    xhs_title = clip_chars(title, TITLE_MAX)
    hook_budget = BODY_MAX - 120  # leave room for the CTA + tags block
    hook = clip_chars(opening, hook_budget)
    copy = (
        f"{xhs_title}\n\n"
        f"{hook}\n\n"
        f"—\n"
        f"📖 这只是开头，全文见我的博客\n"
        f"🔗 {url}（链接在主页简介 / 评论区）\n\n"
        f"#张岭的博客 #读书笔记 #个人成长 #在这里改成你的话题"
    )
    (out_dir / "copy.txt").write_text(copy, encoding="utf-8")

    # ---- cards ----
    opening_cards = chunk_paras(opening, CARD_CHARS, MAX_OPENING_CARDS)
    total = 1 + len(opening_cards) + 1  # cover + openings + cta
    docs = [cover_card(title, date, total)]
    for i, chunk in enumerate(opening_cards, start=2):
        docs.append(body_card(chunk, i, total))
    docs.append(cta_card(xhs_title, url, total))
    pngs = render(docs, out_dir)

    # ---- report ----
    rel = out_dir.relative_to(Path(__file__).parent)
    print(f"✓ Xiaohongshu draft material for: {title}")
    print(f"  folder : {rel}/")
    print(f"  copy   : {rel}/copy.txt   ({len(copy)} 字)")
    print(f"  cards  : {len(pngs)} 张 (1080×1440)")
    for p in pngs:
        print(f"           {p.name}")
    if len(title) > TITLE_MAX:
        print(f"  ⚠ 标题原文 {len(title)} 字，已截断到 {TITLE_MAX} 字，建议手动精简。")
    print("\n下一步：小红书创作后台/App → 新建图文 → 上传 cards → 粘贴 copy.txt → 存草稿。")


if __name__ == "__main__":
    main()
