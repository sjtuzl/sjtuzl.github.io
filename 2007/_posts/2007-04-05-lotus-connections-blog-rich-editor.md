---
layout: post
title: "Lotus Connections Blog - Rich editor"
date: 2007-04-05 10:12:57 +0800
permalink: /20070405/lotus-connections-blog-rich-editor.html
wp_id: 646
wp_slug: "lotus-connections-blog-rich-editor"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>Lotus Conections 1.0中Blog使用了Dojo的rich editor，这个editor的基本功能比较完善，各方面大致与其他流行的editor如WordPress中使用的TinyMCE持平。由于大部分Dojo的Widget对于i18n和a11y (accessibility)支持较差，IBM对其进行了增强。目前Blog里使用的版本就提供了较好的a11y支持，比如在editor中按tab键会跳出编辑状态，把焦点转移到下一个控件上。现在这个功能可以同时在IE和Firefox里实现 (调试HTML的tabIndex是个很熬人的工作）。</p>
<p>另外，我帮目前Blog的editor添加了离开编辑模式的提示功能 - 当用户写帖子的时候如果点了其他link或者准备关掉浏览器，这个时候弹出窗口警告内容已经过编辑，是否需要离开编辑模式。</p>
<p>用户登录后写文章，如果中间间隔较长的话，会出现提交数据会话过期的情况，数据往往会丢失。根据测试team映的反应，我写了一个heartbeat脚本，在浏览器端定期ping远程的server。在WebSphere下，如果提交的link可以促使Application server访问session对象的话，当前session将会续约，这样可以保持长时间的可工作状态 (缺省为30分钟)。</p>
<p>今天在Mozilla add-on上下载<a href="http://labs.mozilla.com/2007/04/keep-track-of-your-friends-with-the-coop/">Coop</a>的时候，看到了<a href="http://scribefire.com/">ScribeFire</a>，装上后就用它写了这个帖子，还挺好使。</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/04/lotus_connections_blog_rich_editor.jpg" /></p>
<p><p class="poweredbyperformancing">Powered by <a href="http://scribefire.com/">ScribeFire</a>.</p>
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
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2007-04-05 10:34:15</time></div>
  <div class="comment-body"><p>最近也被Dojo 的Editor2组件折腾死， 各种莫名的问题<br>
比如 切换WYSIWYG和HTML code编辑模式时，文本框大小都会改变</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2007-04-05 11:07:56</time></div>
  <div class="comment-body"><p>右下角的天气预报插件是啥？呵呵，看来楼主有必要写个“我的FireFox插件”之类的帖子。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-04-05 11:35:27</time></div>
  <div class="comment-body"><p>回1楼：没错，我的感觉是要不停的试，不停的测，结果是遍历出来的。</p>
<p>回2楼：下面的天气预报是weather.com提供的插件，还能看卫星云图。至于插件，比较多， 等有空总结一下了了，呵呵</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://zhouyiyan.blogspot.com/" rel="nofollow noopener">Ian</a></span><time class="comment-date">2007-04-05 13:14:43</time></div>
  <div class="comment-body"><p>scribeFire长的像Performancer 莫非是一个地方出的？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://xiaoxia.turendui.com" rel="nofollow noopener">Sean</a></span><time class="comment-date">2007-04-05 22:43:32</time></div>
  <div class="comment-body"><p>同疑惑，Powered by 都和Performancer一摸一样。是不是Performance最新升级了？<br>
天气预报插件是Forecastfox ：）</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-04-06 03:35:53</time></div>
  <div class="comment-body"><p>是的，改名字了</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">tj</span><time class="comment-date">2008-05-21 15:06:44</time></div>
  <div class="comment-body"><p>Lotus Conections 1.0是DOMINO 8的组件吗？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2008-05-23 23:09:02</time></div>
  <div class="comment-body"><p>不是</p></div>
</li>
</ol>
</section>
{% endraw %}
