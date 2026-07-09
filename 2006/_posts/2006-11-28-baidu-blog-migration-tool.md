---
layout: post
title: "百度博客搬家服务"
date: 2006-11-28 22:43:44 +0800
permalink: /20061128/baidu-blog-migration-tool.html
wp_id: 563
wp_slug: "baidu-blog-migration-tool"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>百度开出<a href="http://hi.baidu.com/sys/bmove">博客搬家服务</a>，我一点不觉得奇怪，倒是它提供的无需密码验证的“搬家”让我觉得很新奇。</p>
<p>在我写了<a href="http://www.zhangling.org/blog/20060710/bokee-migration-wordpress-howto.html">blogChina搬家到WordPress攻略</a>不久，就收到百度工程师的邮件讨论博客搬家的话题。现在看来百度提供的对MSN Space和新浪博客搬家手段可能是完全基于HTML的extract和parsing，而不是blogger API（写入到百度自己的博客系统可以用blogger API或者直接写DB），这就能解释它不仅支持搬自己的家，连别人的家一样搬。来自百度空间的说明基本能证实这一猜测：</p>
<p>“<em>       <a href="http://www.baidu.com/search/move_help.html#8">在搬家过程中有可能会有部分文章、评论丢失、文章格式发生变化。如有少部分文章丢失、格式变化，您可手工将其搬入空间内进行调整</a></em><a href="http://www.baidu.com/search/move_help.html#8">。</a>”</p>
<p>百度的crawler这么强，到网上搬点东西实在易如反掌。我猜百度内部应该有一个generic的Web crawler和多份customized crawlers，各个instance独立运行。博客搬家crawler跑到MSN,Sina上下载页面，抽取页面，扔掉所有外部链接，用广度优先的方法递归爬行，然后导数据。搜索引擎就是这样用别人的数据给自己赚钱，当然前提是提供了内容增值（数据可访问性），不好说这样以披着搜索引擎的外衣拷贝博客文章到自家的做法外人有没有想法，不过过去的众多经验表明粘着点原罪的第一枪往往会成为成功的催化剂。
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
  <div class="comment-meta"><span class="comment-author">andy</span><time class="comment-date">2006-12-04 12:54:34</time></div>
  <div class="comment-body"><p>百度搬家只要求用户提供一个把blog url, 并且需设置文章为public, 由此可见它的crawler并没有爬到用户的管理端，其实进入管理端可能效率更高，因为界面比较固定，页面相对统一，不像普通的浏览方式，用户一旦改了显示的模板，crawler可能就难于应付.....</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-12-04 13:16:04</time></div>
  <div class="comment-body"><p>yes, make sense</p></div>
</li>
</ol>
</section>
{% endraw %}
