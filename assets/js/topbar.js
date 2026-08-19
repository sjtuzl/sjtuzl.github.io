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
