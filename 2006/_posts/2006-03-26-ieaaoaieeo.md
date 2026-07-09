---
layout: post
title: "警惕滥用客户端资源"
date: 2006-03-26 15:19:00 +0800
permalink: /20060326/ieaaoaieeo.html
wp_id: 417
wp_slug: "ieaaoaieeo"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>近来发现新浪时事评论的访问经常出现浏览器休克、系统CPU大量占用的情况。为此我对新浪用户评论系统的客户端代码稍加研究并找到了导致性能下降的原因：Ajax代码过度使用了本地计算资源。</p>
<p>新浪用户评论使用了一个JavaScript文件（<a href="http://comment4.news.sina.com.cn/comment/cmnt_xml.js">http://comment4.news.sina.com.cn/comment/cmnt_xml.js</a>），里面封装了所有通过XML与服务器通信的代码，此段代码在客户端运行，透明的和服务器交互，下载并分析评论记录。</p>
<p>和Flash, Applet和ActiveX相比，写一段拥有同样计算能力的代码，基于脚本的JavaScript会更容易，并且最不容易被用户发现，偷偷的在用户的浏览器中运行。</p>
<p>可以想象一个热门的博客作者，正企图用穷举法破解某一密码。那么他可以用JavaScript写一段ajax代码，嵌在博客页面里，所有该博客读者在阅读文章的时候会不自觉的成为该作者破解密码的计算节点。计算的中间结果可以保存在浏览器cookie中，在下次访问的时候继续工作。</p>
<p>似乎有两件工作可以考虑了：1. Ajax vulnerability&nbsp;checker; 2. Grid computing interface for Ajax.。</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(5)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">yoyo</span><time class="comment-date">2006-03-26 15:40:20</time></div>
  <div class="comment-body"><p>哈哈,有意思,学到不少东西!第一次光临,以后会时刻关注!</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">yoyo</span><time class="comment-date">2006-03-26 15:40:43</time></div>
  <div class="comment-body"><p>哈哈,有意思,学到不少东西!第一次光临,以后会时刻关注!</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">peter</span><time class="comment-date">2006-03-29 21:53:02</time></div>
  <div class="comment-body"><p>我觉得你完全可以申请这两个方面的课题，我觉得很可行，并且value很大。特别是第一个。ajax的安全问题肯定是它向前发展必须要过的砍。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">pi1ot</span><time class="comment-date">2006-03-31 14:07:21</time></div>
  <div class="comment-body"><p>客户资源也是可用资源的一部分，一切事情揽到自己身上岂不是又回到了史前unix主机时代。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">boo</span><time class="comment-date">2006-03-31 21:36:44</time></div>
  <div class="comment-body"><p>只要是合理应用而不是掠夺性侵占就没问题。</p></div>
</li>
</ol>
</section>
{% endraw %}
