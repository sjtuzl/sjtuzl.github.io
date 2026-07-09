---
layout: post
title: "Lotus Connections Blog - Feed cache"
date: 2007-05-11 21:38:42 +0800
permalink: /20070511/lotus-connections-blog-feed-cache.html
wp_id: 657
wp_slug: "lotus-connections-blog-feed-cache"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>Lotus Connections 1.0中的Blog实现了两层的缓存机制试图更好的解决性能问题。第一层是Application Server对某些访问频繁数据的缓存；另外一层是在HTTP reverse proxy上，对特定URL资源的本地缓存。缓存对改善性能，尤其是对实时性要求相对较低的Atom feed来说，性能改善的效果更明显。</p>
<p>考虑对数据实时性，Connections Blog缺省关闭了application server的缓存，这样用户在发贴或者回帖后刷新页面立刻可以看到更新，否则从数据写入到reload会有一段时间间隔，容易造成用户困惑。</p>
<p>这里想谈的是HTTP cache。</p>
<p>Blog的典型配置是用DB2数据库，WebSphere appserver，前端是network dispatcher和edge。edge实际是一个HTTP reverse proxy，实现URL转发和内容缓存的功能。 为了实现对Atom feed访问的缓存，Blog会在每个feed的http response的头上面缺省加上max-age=600，response首先到达edge，edge收到后知道需要将该feed缓存600秒。当下次用户通过浏览器、各类feed reader或者是抓虾这样的server端访问的时候，edge首先看feed的10分钟缓存期是否到期，如果还在10分钟内，edge之间把它的cache返回给用户而不再访问appserver；如果已经超过10分钟，edge会向appserver发一个HTTP conditional get的命令，看application server端是不是有新的feed内容。Application server收到feed的请求后，如果有新的feed内容，则向edge返回新feed内容，response code置成200；如果没有更新，则不返回任何内容；response code置成304。无论是否有更新，edge在重新收到appserver的返回后，将重新缓存该feed 10分钟。依次类推。</p>
<p>当在没有edge的情况下， 可以用浏览器来模拟。当在10分钟间隔内，如果在地址栏之间回车的话，浏览器甚至不会与服务器建连（可通过LiveHTTPHeader或者ieHTTPHeaders之类的browser插件观察）。目前Firefox和IE对max-age都可以很好的支持。</p>
<p>在实际情况下，大部分feed源本身并没有类似edge这样的模块，而是直接把appserver暴露给client。从实现上看，很多feed reader对<em>last modified</em>时间戳的管理都很弱，会导致每次都迫使appserver重新加载数据。另外，在server端有些feed server也没有实现对<em>if modified since</em>的管理，无论什么请求都重新进行数据访问，这样都增加了额外的负载。</p>
<p>这是Connections Blog的tech lead <a href="http://robubu.com/">Rob</a>在调试feed cache的时候发给我的<a href="http://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers">一篇文章</a>，写的很详细。另外来自IE team的这份<a href="http://blogs.msdn.com/ie/archive/2006/06/01/613132.aspx">A Caching Issue in IE7 Beta 2</a>也很有帮助。</p>
<p>从Feed出发，此类提高性能的缓存方法可以常态的运用在如REST等基于HTTP，以URL来映射资源的应用上，来帮助克服传统Web Server/Web browser多年前已经完美解决了的、而重新在Web 2.0环境下产生的数据生产者和消费者之间产生的老矛盾。
</p>
<p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(3)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://shangwx.blogspot.com" rel="nofollow noopener">shangwx</a></span><time class="comment-date">2007-05-26 16:51:07</time></div>
  <div class="comment-body"><p>在上海做项目的时候从Peter Pan那里知道你的博客，写的很不错，在我的必看列表之内，只不过没有冒过泡。似乎上海的同事写博的多些 :) <br>
希望有机会能多交流，很想认识更多志同道合的朋友。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-05-26 18:58:08</time></div>
  <div class="comment-body"><p>彼得潘，谢谢你的推荐</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Peter Pan</span><time class="comment-date">2007-06-09 07:19:04</time></div>
  <div class="comment-body"><p>哈哈，shangwx终于冒泡啦：）</p>
<p>大家都不要客气，好东西要分享的：）</p>
<p>另外，shangwx的博客也写得很好的：）</p></div>
</li>
</ol>
</section>
{% endraw %}
