---
layout: post
title: "permalink和302"
date: 2008-01-05 20:58:16 +0800
permalink: /20080105/feed-reader-http-302-support.html
wp_id: 700
wp_slug: "feed-reader-http-302-support"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>permalink是Blogs 2.0里新添加的功能，和WordPress的”slug“很类似，允许博客作者为自己的帖子指定一个有意义的、永久的URL。</p>
<p>对于客户端来说，permalink的存在，只有在支持HTTP 302的前提下才更有价值。因为很多的permalink或者一些feed的订阅地址，会像public API一样，一旦发布出去就应该长时间保持有效，即使需要修改也必须同时用302重定向的方法支持老的URL。最近我在整理ThunderBird里订阅的feed列表，发现有不少feed（都是一些大牌儿网站的feed）已经失效了，而用浏览器访问这些feed则可以正常阅读，究其原因就在于ThunderBird不支持HTTP 302重定向，人家feed地址一改就歇菜了。</p>
<p>对于企业内部用户，feed  reader面对的是配置了各种策略（包括安全策略）的部署环境，重定向几乎不能避免，对它的支持格外重要。
</p>
<p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(6)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://wecoma.spaces.live.com" rel="nofollow noopener">张岭</a></span><time class="comment-date">2008-01-21 04:44:16</time></div>
  <div class="comment-body"><p>哈哈，居然真有这么多同名同姓的家伙。你好！我的同名人。搜文章搜到你这儿来了。呵呵，真有意思。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2008-01-21 22:15:44</time></div>
  <div class="comment-body"><p>搜自己名字的人真多啊，呵呵</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zzyjs.net.cn" rel="nofollow noopener">在职研究生</a></span><time class="comment-date">2008-03-01 16:02:57</time></div>
  <div class="comment-body"><p>只有在支持HTTP 302的前提下才更有价值。因为很多的permalink或者一些feed的订阅地址，会像public API一样，一旦发布出去就应该长时间保持有效，即使需要修改也必须同时用302重定向的方法支持老的URL。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.e63.cn" rel="nofollow noopener">校园网</a></span><time class="comment-date">2008-03-08 15:01:30</time></div>
  <div class="comment-body"><p>校园网http://www.e63.cn/index/top/</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.onjobedu.com" rel="nofollow noopener">在职研究生</a></span><time class="comment-date">2008-03-17 21:23:06</time></div>
  <div class="comment-body"><p>很技术的文章</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.solidworks3d.cn" rel="nofollow noopener">sipmsoft</a></span><time class="comment-date">2008-03-19 20:07:00</time></div>
  <div class="comment-body"><p>很技术的文章<br>
http://www.sipmsoft.cn <br>
http://www.solidworks3d.cn</p></div>
</li>
</ol>
</section>
{% endraw %}
