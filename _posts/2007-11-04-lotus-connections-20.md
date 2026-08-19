---
layout: post
title: "奔2"
date: 2007-11-04 20:47:44 +0800
permalink: /20071104/lotus-connections-20.html
wp_id: 694
wp_slug: "lotus-connections-20"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>过去的三个星期，是Lotus Connections 1.0.2和2.0并行开发的三周，一边解bug，一边考虑实现新功能，ClearCase里面两条stream来回切换，不亦乐乎。1.0.2到这个周末算正式结束，进入最终release。1.0.2 Blogs除了修复了从1.0里遗留的30多个bug外，在性能方面也做了诸多调整；另外根据客户反映，恢复了MetaWeblog API的支持（与ATOM API共存）。Connections整体功能方面则支持Tivoli Access Manager，强制的ATOM basic authentication over HTTPS （写入部分，读取依然保持HTTP）；增加了AIX平台和MS SQL Server数据库的支持等一系列的改进。</p>
<p>目前正紧锣密鼓开发的Connections 2.0将基于Java 5构建，此前1.0.x基于JDK 1.4，虽然包含了部分1.5的代码，但使用了retroweaver保证这些1.5的代码运行在1.4的VM之上。2.0版的Blogs会在1.0.x基础上增加新的功能，UI方面也会有相当程度的改进与提高，这些工作目前都在紧张的进行中，不久就能看到阶段性成果。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(3)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Tristan Chen</span><time class="comment-date">2007-11-05 10:17:10</time></div>
  <div class="comment-body"><p>1.另外根据客户反映，恢复了MetaWeblog API的支持（与ATOM API共存）</p>
<p>Comments: TAP上的MetaWeblog API支持一直都是有的啊，我可以通过ScribeFire通过MetaWeblog API来发布Entry啊。</p>
<p>2。 此前1.0.x基于JDK 1.4，虽然包含了部分1.5的代码，但使用了retroweaver保证这些1.5的代码运行在1.4的VM之上。</p>
<p>目前Connections运行在WAS 6.1.0.3上面，里边的jdk默认就是1.5.0_SR2.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-11-05 11:28:52</time></div>
  <div class="comment-body"><p>1. TAP是定制过的，所以有这个功能；</p>
<p>2. 虽然WAS 6.1跑的是JVM 1.5，但Connections 1.0.X的规范是1.4，为了实现可能的兼容性（比如支持WAS 6.0)。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://blog.csdn.net/richard_liang" rel="nofollow noopener">Richard</a></span><time class="comment-date">2007-11-06 23:57:37</time></div>
  <div class="comment-body"><p>张博，很久没更新了，呵呵</p></div>
</li>
</ol>
</section>
{% endraw %}
