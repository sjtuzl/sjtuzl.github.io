---
layout: post
title: "n-tier应用的profiling"
date: 2006-07-24 23:46:12 +0800
permalink: /20060724/n-tier-web-application-profiler.html
wp_id: 462
wp_slug: "n-tier-web-application-profiler"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>近来在分析一个三层架构Web应用的性能问题。由于应用响应速度慢，需要分析出耗时的瓶颈到达在哪里，所以在数据库起了监控服务、在Application server写了log、甚至还分析了HTTP server的log。因为性能瓶颈可能出现在1)浏览器到Application Server的网络连接；2)Application server的用户代码；3)Application server到数据库服务器的网络连接;4)数据库服务器上运行的SQL和各种存储过程、触发器等。</p>
<p>很需要一个工具可以简单的从浏览器发出请求后，一路钻到web server，application server和database server里面，看看分别在各处消耗了多少时间，在路上花了多少时间，并且能图示化的显示请求和响应一来一回的profiling的全过程。</p>
<p>在不插入定制代码的情况下，要实现这样的功能难度很大。在DB这端可以在JDBC上加层wrapper捕获对数据库的请求；在application server这端可以在container级别捕捉到对DB的请求，然后分别记录并跟踪。“捕捉”似乎有些AOP的意思，如果对资源的访问都可以映射到有限的API上的话，AOP应该是个合理的解决方法。</p>
<p>如果有人知道有这样的整合式profilier，能免去那些debug的"System.out"和在应用、数据库服务器各处设置的绊马索，就太好了。
</p>
<p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(4)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">paulex</span><time class="comment-date">2006-07-26 14:57:49</time></div>
  <div class="comment-body"><p>Application Server应该有个监控console可以看到JSP/Servlet/EJB/线程的资源占用和响应时间的吧？应该可以用来找到hotspot和bottleneck在哪里。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-07-26 18:42:03</time></div>
  <div class="comment-body"><p>可以动态的针对当前请求吗？我去看看。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Andy</span><time class="comment-date">2006-08-08 12:57:50</time></div>
  <div class="comment-body"><p>有这样的：）。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-08-08 20:59:25</time></div>
  <div class="comment-body"><p>在TSS上看到jKool，一个可以monitor多层应用的performance tool。</p></div>
</li>
</ol>
</section>
{% endraw %}
