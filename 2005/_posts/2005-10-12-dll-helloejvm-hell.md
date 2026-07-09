---
layout: post
title: "DLL hell与JVM hell"
date: 2005-10-12 13:50:00 +0800
permalink: /20051012/dll-helloejvm-hell.html
wp_id: 273
wp_slug: "dll-helloejvm-hell"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>DLL hell太出名了，以至于wikipedia也有<a href="http://en.wikipedia.org/wiki/DLL-hell">专门注解</a>。鄙视那些动不动就往\SYSTEM32里面拷一堆链接库的安装程序，还有就是在\Documents and Settings下乱开目录的程序，虽然很多软件都这么做。我比较喜欢把程序文件和用户数据文件保存在同一安装目录下的做法，让我很容易的知道它们到底干了些什么。</p>
<p>&quot;JVM hell&quot;，先这么叫着，越来越严重的侵蚀着我的电脑。刚刚遍历了一遍硬盘，我的机器里一共安装了<strong><font size="3">18</font></strong>份JDK和JRE，除了手工安装的J2SE 1.4.2和J2SE 1.5外，WebSphere有1份；DB2有1份；RSA有1份；Lotus Notes有1份；ICT有1份...还有䷥些不知道怎么装进去的。按每份JDK/JRE 30MB大小算，500多兆的硬盘空间就没了。</p>
<p>每个Java程序都有理由解释为什么要单独安装一份JRE，要么是JDK API兼容性，要么需要特殊security package。有些商业Java程序使用Install Shield打包安装，IS似乎并不检测当前用户是否已经安装符合要求的JRE，硬生生的再塞一份copy进来，拽的很。</p>
<p>应该向Eclipse学习，不要浪费资源随意redistribute JRE，多搞点“绿色”Java软件，大家省心。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(1)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">lixian</span><time class="comment-date">2005-10-12 09:55:39</time></div>
  <div class="comment-body">的确时间长了硬盘里会塞无数的jdk，要么是不同的软件自己附带进来的，要么是自己留的不同版本的jdk。什么时候有个jdk manager就好了呵呵<br></div>
</li>
</ol>
</section>
{% endraw %}
