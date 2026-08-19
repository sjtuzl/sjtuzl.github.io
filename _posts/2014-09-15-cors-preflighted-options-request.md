---
layout: post
title: "CORS (Cross-Origin Resource Sharing) preflighted OPTIONS request"
date: 2014-09-15 14:16:13 +0800
permalink: /20140915/cors-preflighted-options-request.html
wp_id: 1136
wp_slug: "cors-preflighted-options-request"
has_comments: false
---
{% raw %}
<div class="e-content">
<p><a title="cors" href="http://www.w3.org/TR/cors/" target="_blank">CORS</a>提供了安全访问跨域请求的方案，目前主流的浏览器都支持CORS。其中CORS preflighted request中提到浏览器需要先发出一个OPTIONS的请求在服务器端获得通过后（利用HTTP response中的CORS header进行审批）才可以进行后续的访问。根据<a href="https://dvcs.w3.org/hg/cors/raw-file/tip/Overview.html#preflight-request" target="_blank">规范</a>，此HTTP OPTIONS请求中<strong>不允许携带任何cookie</strong>。</p>
<p>我很想知道这样的设计是出于什么考虑？如果是出于安全考虑，那么当前用户session如果已经登录此跨站网站并且有cookie，这些cookie对所访问的跨域服务器来说是没有个人信息泄露的问题，因为本来这些cookie就是服务器产生并返回给浏览器的，你送不送不存在安全隐患。Chrome之前有个<a href="https://code.google.com/p/chromium/issues/detail?id=377541" target="_blank">bug</a>就是在OPTIONS请求里面带了cookie，最近刚刚修复，而Chrome并没有质疑规范的设计是否合理。</p>
<p>不允许带Cookie在采用了如TAM, Siteminder等统一认证的环境下很麻烦，因为这样的request还没有机会到达应用本身就被前端reverse proxy（或web server agent）拦住了，而它们都不具备判断目标应用是否会放行此跨域请求的能力（一般情况下应用程序负责维护一个信任网站的白名单），所以还得通过配置放行此无cookie的请求到目标应用。</p>
</div>
{% endraw %}
<!--more-->
