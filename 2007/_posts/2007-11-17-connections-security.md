---
layout: post
title: "Lotus Connections的安全性"
date: 2007-11-17 09:26:54 +0800
permalink: /20071117/connections-security.html
wp_id: 696
wp_slug: "connections-security"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>Lotus Connections的安全性包括以下几个方面：</p>
<p>1. 传输层安全。Connections在用户登录时强制采用SSL，用户也可以修改配置实现整个应用的SSL保护。上周我们根据一个国外客户的需求，通过定制web.xml和HTTP Server的rewriterule实现了Web访问的强制SSL保护和feed内容的强制basic authentication。</p>
<p>2. 认证安全。Connections的认证包括form based authentication（j_security_check）和basic authentication。前者是在使用浏览器访问5个模块的时候用户认证方式，后者是feed reader使用的。在Connections 1.0.2中，强制要求feed reader在做post等写操作的时候使用basic authentication over SSL，其他读feed的操作无需认证。</p>
<p>3. 第三方安全产品的支持。1.0.2增加了对Tivoli Access Manager （TAM）的支持。看似和应用无关的安全支持实际上影响了不少的代码。而为了支持AJAX, JSON等调用，TAM的配置也是很不同。举例来讲，我们尝试过的一个TAM配置会在返回的页面的末尾添加一段JS代码，这会break我们的JSON调用，必须用其他配置形式绕过。</p>
<p>4. 对Web内容的过滤。Connections使用了<a href="http://www.ibm.com/developerworks/library/wa-pz-acf/">ACF</a>对用户提交内容进行检查，去除掉一些会危害Web访问安全的代码，如Cross-site scripting （<a href="http://en.wikipedia.org/wiki/Cross_site_scripting">XSS</a>）。Blogs还会根据用户配置对上传的文件进行检测，最大程度上减少XSS的可能性。Activities甚至还提供了对<a href="http://en.wikipedia.org/wiki/Cross-site_request_forgery">CSRF</a>的防范功能。</p>
<p>天下没有免费的午餐，增加了诸多的安全性机制，会在某种程度上对系统性能产生影响，比如HTTPS相对HTTP会降低约40%的性能（仅在登录是使用可以忽略）；ACF的HTML解析的代价。好消息是大部分安全机制都是可以由用户修改配置来enable或者disable，有相当的灵活性。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Tristan Chen</span><time class="comment-date">2007-12-10 17:06:16</time></div>
  <div class="comment-body"><p>最近正在总结这个，你这篇真是及时雨啊，谢谢啦。不过号称2.0这部分会有很大的加强。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-12-11 22:44:28</time></div>
  <div class="comment-body"><p>呵呵</p></div>
</li>
</ol>
</section>
{% endraw %}
