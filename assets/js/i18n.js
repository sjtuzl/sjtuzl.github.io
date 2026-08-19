/* =====================================================================
   i18n.js — client-side UI language switch (English default / 简体中文).

   The page HTML ships in English (so English readers and no-JS visitors
   get a correct default). When the visitor picks 中文, this script swaps
   every labelled UI string to Chinese. It translates the site *chrome*
   only — nav, headings, footer, pagination, section labels — never the
   blog post bodies, which keep their original language.

   Two hook mechanisms:
     * [data-i18n="key"]      -> innerHTML replaced from DICT[lang][key]
     * [data-i18n-tpl="key"]  -> DICT template with {1},{2} filled from
                                 the element's data-n1 / data-n2 (keeps
                                 Liquid-rendered numbers, allows word
                                 reordering between languages)
   Archived-comment labels live inside 300+ generated posts and can't
   carry attributes, so they are translated by class selector instead.
   ===================================================================== */
(function () {
  "use strict";

  var DICT = {
    "nav.home":      { en: "Home",    zh: "首页" },
    "nav.archive":   { en: "Archive", zh: "归档" },
    "nav.about":     { en: "About",   zh: "关于" },

    "brand": { en: "Ling Zhang's Blog", zh: "张岭的博客" },
    "name":  { en: "Ling Zhang",        zh: "张岭" },

    "bio.role1": { en: "Director of AI Lab (current), CHINT GROUP",
                   zh: "正泰集团｜人工智能研究院院长（现任）" },
    "bio.role2": { en: "VP of Engineering, Cloudwalk Technology",
                   zh: "云从科技集团｜AI平台中心｜研发副总裁" },
    "bio.role2b": { en: "VP of Technology, Transfar Zhilian",
                    zh: "传化智联｜技术副总裁" },
    "bio.role3": { en: "IBM Senior Technical Staff Member &amp; Member of IBM Academy of Technology",
                   zh: "IBM资深技术专家 &amp; IBM技术院院士" },

    "footer.allposts": { en: "All posts", zh: "全部文章" },
    "footer.migrated": {
      en: "Migrated from the original WordPress blog at zhangling.org &middot; Hosted on GitHub Pages",
      zh: "内容迁移自原 WordPress 博客 zhangling.org &middot; 由 GitHub Pages 托管" },

    "index.readmore":    { en: "Read more",   zh: "阅读全文" },
    "index.andcomments": { en: " &amp; comments", zh: " 及评论" },
    "index.newer":       { en: "← Newer posts", zh: "← 更新的文章" },
    "index.older":       { en: "Older posts →", zh: "更早的文章 →" },
    "page":              { en: "Page {1} of {2}", zh: "第 {1} / {2} 页" },

    "archive.heading": { en: "All Posts",  zh: "全部文章" },
    "archive.count":   { en: "{1} posts",  zh: "共 {1} 篇" },

    "year.heading": { en: "Posts from {1}", zh: "{1} 年的文章" },
    "backarchive":  { en: "← Archive", zh: "← 全部归档" },

    "about.p1": {
      en: "This is the personal blog of <strong>Ling Zhang</strong>, with notes on technology, work, and life. The earliest posts date back to 2004.",
      zh: "这是 <strong>张岭</strong> 的个人博客，记录关于技术、工作与生活的随笔。最早的文章可追溯到 2004 年。" },
    "about.p2": {
      en: "This site's content was migrated in 2026 from the original DreamHost WordPress blog (<a href=\"https://www.zhangling.org/blog/\">zhangling.org/blog</a>) to GitHub Pages.",
      zh: "本站内容于 2026 年从原 DreamHost WordPress 博客（<a href=\"https://www.zhangling.org/blog/\">zhangling.org/blog</a>）迁移至 GitHub Pages。" },
    "about.linkedin": { en: "LinkedIn:", zh: "领英：" },

    "notfound.msg":    { en: "Sorry, this page could not be found.", zh: "抱歉，未找到该页面。" },
    "notfound.home":   { en: "Home",             zh: "首页" },
    "notfound.browse": { en: "Browse all posts", zh: "浏览全部文章" },

    "special.heading": { en: "Featured Collection", zh: "特辑收藏" },
    "special.note": {
      en: "Image collection migrated from the original site's /special/ directory",
      zh: "迁移自原站点 /special/ 目录的图片收藏" },

    "giscus.heading":  { en: "Leave a comment", zh: "发表评论" },

    /* archived (migrated) comment labels — applied by class selector */
    "comments.word": { en: "Comments", zh: "评论" },
    "comments.note": {
      en: "These comments were migrated from the original blog and are archived read-only.",
      zh: "以下评论迁移自原博客，仅作存档只读展示。" }
  };

  var STORE_KEY = "blog-lang";

  function getLang() {
    try {
      var q = new URLSearchParams(location.search).get("lang");
      if (q === "zh" || q === "en") return q;
      var s = localStorage.getItem(STORE_KEY);
      if (s === "zh" || s === "en") return s;
    } catch (e) {}
    return "en"; // default English
  }

  function t(key, lang) {
    var e = DICT[key];
    return e ? (e[lang] != null ? e[lang] : e.en) : "";
  }

  function fill(tpl, el) {
    return tpl.replace("{1}", el.getAttribute("data-n1") || "")
              .replace("{2}", el.getAttribute("data-n2") || "");
  }

  function apply(lang) {
    // 1. plain labelled elements
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      el.innerHTML = t(el.getAttribute("data-i18n"), lang);
    });
    // 2. templated elements (numbers stay, word order may change)
    document.querySelectorAll("[data-i18n-tpl]").forEach(function (el) {
      el.innerHTML = fill(t(el.getAttribute("data-i18n-tpl"), lang), el);
    });
    // 3. archived comment labels living inside post bodies
    document.querySelectorAll(".archived-comments .comments-title").forEach(function (h) {
      var cnt = h.querySelector(".comment-count");
      h.textContent = t("comments.word", lang) + " ";
      if (cnt) h.appendChild(cnt);
    });
    document.querySelectorAll(".archived-comments .comments-note").forEach(function (p) {
      p.textContent = t("comments.note", lang);
    });

    document.documentElement.setAttribute("lang", lang === "zh" ? "zh-CN" : "en");

    // reflect active state on the toggle(s)
    document.querySelectorAll("[data-set-lang]").forEach(function (a) {
      a.classList.toggle("active", a.getAttribute("data-set-lang") === lang);
    });

    // best-effort: retheme the giscus widget language if present
    var frame = document.querySelector("iframe.giscus-frame");
    if (frame && frame.contentWindow) {
      frame.contentWindow.postMessage(
        { giscus: { setConfig: { lang: lang === "zh" ? "zh-CN" : "en" } } },
        "https://giscus.app");
    }
  }

  function setLang(lang) {
    try { localStorage.setItem(STORE_KEY, lang); } catch (e) {}
    apply(lang);
  }

  function init() {
    document.querySelectorAll("[data-set-lang]").forEach(function (a) {
      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        setLang(a.getAttribute("data-set-lang"));
      });
    });
    apply(getLang());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
