/* topbar.js — reveal the sticky bar's mini avatar+title only after the full
   banner has scrolled out of view, so the avatar never shows twice at once.

   Pages with a full banner (home/archive/about) start with the mini brand
   hidden via CSS (body:not(.layout-post) .site-topbar .brand). We watch the
   banner with an IntersectionObserver and add .is-visible to the brand once
   the banner leaves. The top rootMargin (~ the sticky bar's height) makes
   the swap happen exactly as the banner disappears behind the bar, leaving
   no gap where neither avatar shows. Post pages have no banner, so nothing
   here runs and their brand stays visible. */
(function () {
  "use strict";
  var banner = document.querySelector(".site-header");
  var brand = document.querySelector(".site-topbar .brand");
  if (!banner || !brand) return; // no banner (e.g. post pages): leave as-is

  if (!("IntersectionObserver" in window)) {
    brand.classList.add("is-visible"); // fallback: just show it
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    // banner still (partly) visible -> hide mini brand; banner gone -> show it
    brand.classList.toggle("is-visible", !entries[0].isIntersecting);
  }, { rootMargin: "-56px 0px 0px 0px", threshold: 0 });

  io.observe(banner);
})();

/* feed-clamp — on the home feed, crop over-tall post bodies so long articles
   show only a preview with a fade + "Read more" link, while short ones stay
   whole. We compare each entry's natural body height (scrollHeight, which
   ignores the later max-height crop) to the CSS clamp height (22rem) plus a
   buffer, so a body only slightly over the limit isn't cropped to a stub.
   Adding .is-clamped triggers the crop/fade/link in CSS. We measure now and
   again after images load (final heights). Non-home pages have no .feed-entry,
   so this is a no-op there. */
(function () {
  "use strict";
  var entries = document.querySelectorAll(".feed-entry");
  if (!entries.length) return;

  function clampAll() {
    var fs = parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
    var threshold = 22 * fs + 3 * fs; // clamp height (22rem) + buffer (3rem)
    for (var i = 0; i < entries.length; i++) {
      var content = entries[i].querySelector(".post-content");
      if (!content) continue;
      if (content.scrollHeight > threshold) {
        entries[i].classList.add("is-clamped");
      }
    }
  }

  clampAll();
  window.addEventListener("load", clampAll); // re-measure once images settle
})();
