---
layout: post
title: "一天一行"
date: 2007-04-13 09:13:29 +0800
permalink: /20070413/one-line-of-code-per-day.html
wp_id: 650
wp_slug: "one-line-of-code-per-day"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>过去的两天，我只写了两行代码。</p>
<p>这两行代码分别解决了Lotus Connections Blog中的两个bug，平均一行代码耗时10小时。</p>
<p>其中一个Blog编辑器中的bug，是通过几十次的blog发贴，用<a href="http://www.mozilla.org/projects/venkman/">Venkman的Firefox JavaScript Debugger</a>抓到的，该错误源自Firefox和Dojo自身的缺陷。因为一天中发测试贴太多，现在在自己博客发贴也有点心理障碍了。</p>
<p>另外一个是Blog的Theme切换问题，为此还动用了<a href="http://www.microsoft.com/technet/sysinternals/FileAndDisk/Filemon.mspx">Filemon</a>这样的工具，监测javaw.exe对文件系统的修改，在追踪到数据库文件被修改后，进而跟踪DB表变化，加上Eclipse debugger，最后才确信需要把else后面那个"}"提前一行。</p>
<p>在involve到Lotus Connections的开发后，最大的一个变化居然是自己发贴、看social bookmark的兴趣降低了- 搞伤了，就像我现在看到早餐的炒蛋和薯角一样，刚闻到味儿，就半饱了。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(8)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Cindy</span><time class="comment-date">2007-04-13 10:32:52</time></div>
  <div class="comment-body"><p>是的，大厨一般回家都不做饭。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Richard</span><time class="comment-date">2007-04-13 10:35:00</time></div>
  <div class="comment-body"><p>Dr.zhang, 不应该啊。像你这样的修为，不应该这么容易就被击倒啊 :-)</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Richard</span><time class="comment-date">2007-04-13 10:35:55</time></div>
  <div class="comment-body"><p>(灌水)晚一步就从沙发变板凳了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.laoxiong.cn" rel="nofollow noopener">老熊</a></span><time class="comment-date">2007-04-13 12:01:47</time></div>
  <div class="comment-body"><p>最近在评价ajax framework，想挑一个长期使用。你给评价一下Dojo？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://hzhfang.spaces.live.com" rel="nofollow noopener">爱拉芳</a></span><time class="comment-date">2007-04-13 22:46:50</time></div>
  <div class="comment-body"><p>呵呵，看来US的早餐在哪里吃起来都一样啊！标准化商业化了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Alan Cui</span><time class="comment-date">2007-04-25 17:06:48</time></div>
  <div class="comment-body"><p>Ah~~~~, Filemon都用到了？天，真是强～～～。呵呵</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-04-27 11:25:46</time></div>
  <div class="comment-body"><p>没办法，硬办法，但很有效。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-04-27 11:26:55</time></div>
  <div class="comment-body"><p>回老熊。对dojo，我现在是只见树木不见森林，等我积累了一些心得，再来分享吧。</p></div>
</li>
</ol>
</section>
{% endraw %}
