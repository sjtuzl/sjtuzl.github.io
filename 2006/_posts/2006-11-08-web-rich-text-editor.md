---
layout: post
title: "Web-based rich text editor"
date: 2006-11-08 23:38:14 +0800
permalink: /20061108/web-rich-text-editor.html
wp_id: 551
wp_slug: "web-rich-text-editor"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>今天和几个同事讨论Blog，wiki在线编辑器的WYSIWYG的Copy & Paste的功能是如何实现的（在Word任意拷贝一段格式化的文字或者表格，可以粘贴到Web 的rich text editor里面，而且格式基本不变），是不是通过JS库自己写程序实现的格式化功能。仔细好像又不太想，JS要做这么复杂的rendoring工作，几十k的代码肯定不够。</p>
<p>花了点时间做了研究，确定是browser本身提供了可编辑的rich text功能。如下代码显示一个文本框，可以在里面粘贴rich text，该example适用于IE 6.0和Firefox 2.0。</p>
<p><a href="/assets/media/uploads/2006/11/rich_text_editor.html">Rich Text Editor Example</a> （20行）
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
  <div class="comment-meta"><span class="comment-author"><a href="http://www.leonzhang.com" rel="nofollow noopener">leon</a></span><time class="comment-date">2006-11-09 09:29:51</time></div>
  <div class="comment-body"><p>有意思，以前还以为都是js搞的呢，<br>
但是类似google office的东西，这样搞一定还不够，还的靠js...</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Marshall</span><time class="comment-date">2006-11-09 09:37:04</time></div>
  <div class="comment-body"><p>try FCKEditor</p></div>
</li>
</ol>
</section>
{% endraw %}
