---
layout: post
title: "隐藏、再隐藏"
date: 2006-06-08 13:01:00 +0800
permalink: /20060608/othocouotho.html
wp_id: 439
wp_slug: "othocouotho"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>本来想去<a href="http://www.6rooms.com/">6rooms.com</a>上看看胡戈最新的“鸟笼山剿匪记”，发现正式的视频版还没出，只有Flash。在顺便点击其他视频的时候，我注意到6rooms对自己的视频文件进行了特殊保护，防止用户使用下载工具下载并离线观看。</p>
<p>6rooms的手段其实很简单，当用户要观看视频的时候，首先下载一个Flash，这是个Flash版的媒体播放器支持.flv格式的视频文件。当该Flash在浏览器上初始化后，它发送HTTP请求给Web server以获取真正的视频文件。由于这个过程用户无法控制并得到真正的完整URL，所以只有等视频文件通过Flash下载后“准”在线的观看。一旦关闭浏览器，想再看的话只能重新刷新页面，重新下载视频。</p>
<p>我用了一个HTTP proxy捕获下了Flash播放器和Web server间的对话，实际上当Flash播放器请求文件的时候6rooms服务器返回一个HTTP 303并提供了重定向的绝对URL - 真正的视频文件。</p>
<p>这让人联想到最近的迅雷事件。如果网络资源的URL任意传播，会伤害内容提供商，因为不会有人想看那些在线广告和花花绿绿的banner。其实可以用临时sessionID的方法确保用户是通过浏览器访问，保证广告商和自身利益，同时允许用户在建立session后下载需要的东西。6rooms这样的做法虽然可以保护文件，但对用户来说极其不方便，无形中是在驱赶用户。以我自己为例，我基本上不在线看Flash和视频，都是“View Source”后抓文件URL，然后扔到下载工具里慢慢爬，以后想什么时候看都行。</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(2)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Chuyue</span><time class="comment-date">2006-09-21 13:22:24</time></div>
  <div class="comment-body"><p>在线看速度很快啊 本来时间也不长的</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-09-21 18:52:01</time></div>
  <div class="comment-body"><p>有时候需要保存，给别人share</p></div>
</li>
</ol>
</section>
{% endraw %}
