---
layout: post
title: "Lotus Connections - 搜索"
date: 2009-04-18 10:31:17 +0800
permalink: /20090418/lotus-connections-search-omnifind.html
wp_id: 740
wp_slug: "lotus-connections-search-omnifind"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>从07年第一个版本开始，Lotus Connections就提供了搜索功能 - 很明显这应该是social software的最基本功能。2.0版本以前的实现是每个模块使用Lucene来做全文索引（索引调度也由各模块独立实现）。  从2.0开始，我们开始支持global search，也就是用户登陆到“主页”后，可以在一个独立的搜索界面中同时搜索多个模块（如博客、书签等）。从实现角度看，global search机制稍有不同。首先，与各模块的索引调度类似，它也会定期的到各个模块爬内容，不同的是它的“爬”是通过发出一个HTTP请求（通过basic authentication指定搜索管理员帐号信息），收到请求的模块将返回一个XML格式的数据结果（我们称之为“seedlist”）。Global search在收到seedlist的结果后在本地重新构建索引（一个经过IBM扩展过的Lucene实现），并提供统一界面的搜索。这样用户可以不用在多个模块之前切换就能实现统一搜索。由此带来的一个新问题是，用户在模块内搜索的结果和在global search中搜索的结果不一致，产生的原因一个是因为使用的索引模块实现不一样；另外一个原因是如果在索引周期内用户数据发生了变化，独立索引和全局索引也会产生数据不一致。</p>
<p>从2.5开始，Lotus Connections搜索的一个最大变化是放弃了各个模块内自己的索引而统一使用全局索引。通过调用EJB或者REST API，用户即可以在单一模块进行上下文相关搜索（如在Dogear里只搜书签），也可以做跨模块索引。所有的索引任务（爬、构建索引、查询服务和API ）全部由global search负责。这样，各模块省去了独立实现搜索的任务，而搜索结果也实现了统一。</p>
<p>最近有不少做客户项目的同事问用OmniFind对Lotus Connections进行搜索的可能性。答案是：可以。这个功能从Lotus Connections 2.0就已经提供。具体在OmniFind上的配置方法见：<a href="http://www-01.ibm.com/support/docview.wss?uid=swg27013527&aid=1">http://www-01.ibm.com/support/docview.wss?uid=swg27013527&aid=1</a>。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Toyoo</span><time class="comment-date">2009-08-12 21:47:16</time></div>
  <div class="comment-body"><p>上午看到邮件,有说到内网的Workforce Directory已经更新,会包含更多的信息.链接过去了,的确比原来的包含了更多的内容.下午,工作间隙,花了点时间explore里面的一些新功能,才知道是基于Lotus connection.更像一个社区,可以更新自己的资料,可以开小组,甚至可以建立自己的blog.不过不知道,公司是否会official的announce大家可以使用里面的一些功能,提供一个给全球各个国家的同事交流的平台.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2009-08-21 22:23:50</time></div>
  <div class="comment-body"><p>TAP上的就是。Profiles最新版增加了microblog的功能，可以update自己的状态。</p></div>
</li>
</ol>
</section>
{% endraw %}
