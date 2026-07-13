---
layout: post
title: "Firefox书签导入IE之乱码处理"
date: 2005-08-17 10:27:00 +0800
permalink: /20050817/firefoxeecueeieoaoaeai.html
wp_id: 250
wp_slug: "firefoxeecueeieoaoaeai"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>我的绝大多数的书签都已经转移到Firefox里，IE的书签至少半年没有更新过了。刚才想把两个浏览器的书签单向同步一下，发现从Firefox导出的书签文件再导入到IE里，中文部分出现乱码。稍加研究，顺利解决。</p>
<p>1. 从Firefox导出的书签是一个HTML文件，该文件的编码是UTF-8。可以判定，从中文版IE导入此文件后，IE用GB2312进行解码，导致乱码。</p>
<p>2. 用Ultraedit打开bookmarks.html，copy然后paste到notepad里面，保存（编码选ANSI），会有警告，忽略即可。</p>
<p>3. 从IE导入修改后的书签文件，一切OK.</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(5)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Garry</span><time class="comment-date">2005-10-07 17:51:36</time></div>
  <div class="comment-body"><p>根本就不行，导入之后都是乱码，期待解决方案！</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">boo</span><time class="comment-date">2005-10-09 20:45:38</time></div>
  <div class="comment-body"><p>从Ultraedit里全部copy到notepad中，按ANSI格式保存为一个HTML文件。用IE把该HTML文件导入即可。这个方法对我有效。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jesse</span><time class="comment-date">2008-01-06 12:20:21</time></div>
  <div class="comment-body"><p>如果是IE7，该怎么办啊？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2008-01-07 22:48:13</time></div>
  <div class="comment-body"><p>IE 7还没用过</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">tdkj1247</span><time class="comment-date">2008-06-01 17:51:38</time></div>
  <div class="comment-body"><p>不用那么麻烦<br>
直接用记事本打开htm文档<br>
另存为的时候选ansi编码类型就ok了</p></div>
</li>
</ol>
</section>
{% endraw %}
