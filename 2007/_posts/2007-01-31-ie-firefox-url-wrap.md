---
layout: post
title: "实现IE/FF的URL自动换行(隐藏)"
date: 2007-01-31 23:51:31 +0800
permalink: /20070131/ie-firefox-url-wrap.html
wp_id: 614
wp_slug: "ie-firefox-url-wrap"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>晚上花了些时间调整博客页面：主内容区被横向扩到900px；解决了烦人的URL自动换行的问题 - 这在右边sidebar里面的评论部分问题尤为严重，IE用户经常出现右边sidebar跑到了页面最下方。</p>
<p>comments里常常会贴些较长的URL，而IE在处理URL的时候由于没有空格符所以无法换行，页面被突出的URL顶出来，很难看。</p>
<p>找到了一份很实用的有关<a href="http://www.positioniseverything.net/explorer/expandingboxbug.html">IE/FF文字换行</a>的指南，利用里面提供的方法，修改了系统的style.css。现在长URL在IE中会自动换行，在FF中超出预设部分的内容会自动隐藏。</p>
<p>支持IE/FF自动换行(隐藏)的CSS定义（请尝试分别用IE和Firefox访问本贴，比较一下效果）：<br />
#wraptext {<br />
width: 170px;<br />
word-wrap: break-word;<br />
overflow: hidden;<br />
}</p>
<div id="wraptext"><strong>http://www.MySuperLongExtremelyEndlessURL.com/</strong></div>
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
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2007-02-01 22:45:17</time></div>
  <div class="comment-body"><p>谢谢分享，呵呵。不过你的Blog在FF下面看，comments的字体似乎过小。所以看你的Blog，我总是要在FF里面Ctrl++一下。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/blog" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-02-02 08:39:50</time></div>
  <div class="comment-body"><p>周末来把字搞大点</p></div>
</li>
</ol>
</section>
{% endraw %}
