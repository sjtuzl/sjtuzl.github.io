---
layout: post
title: "杀还是不杀"
date: 2007-05-18 23:38:28 +0800
permalink: /20070518/symantec-false-alarm-chinese-windowsxp.html
wp_id: 661
wp_slug: "symantec-false-alarm-chinese-windowsxp"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>首先，本人是这次<a href="http://tech.sina.com.cn/focus/norton_winxp/index.shtml">诺顿病毒事件</a>的受害者。早上收到公司IT发送出来的病毒警告后，在未搞清原因的情况下主动升级了病毒库，导致中招。接下来的几个小时，IT连续发出几封紧急邮件救险，直到临下班前升级到5.17 rev 73才算告一段落。今天是星期五，将会有相当多的机器在周一上班重新开机的时候出问题。可以想像Symantec眼睁睁看着这些已经关机的机器，却什么也做不了的心情，很残忍。</p>
<p>从技术方面，我想到的是well informed decision。如果病毒分析本身的风险性在逐渐上升，依靠在单机上运行的算法匹配病毒在这次事件背景下可能需要重新思考一下。讲的俗一点，用Web 2.0的方式，病毒分析软件在找到可疑文件后也许不应该立刻采取行动，而是应该把你找到的模式上传给服务器。服务器根据一系列参数，如时间、时序、历史记录、当前改模式总的激活数量等实时的手段进行分析，以确定这的确是个问题或者是误报。每个装在客户机上的杀毒软件都像一片RFID，把它收到的数据分享给其他人，通过event driven系统最终得出结论，杀还是不杀？</p>
<p>杀毒软件也需要个虚拟论坛，杀毒前要到坛子里问问，以做出正确判断。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(5)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2007-05-19 01:06:02</time></div>
  <div class="comment-body"><p>还好我在用英文版XP。现在 Symantec AV 升到 5-18 rev.19 了.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">paulex</span><time class="comment-date">2007-05-19 03:42:33</time></div>
  <div class="comment-body"><p>呵呵，有关杀毒软件，我以前也有过从社区受益的想法，http://blog.csdn.net/paulex/archive/2006/07/19/944042.aspx，关键是如何组织好客户端/服务器/社区/插件之间的关系让用户可以方便放心的使用</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-05-19 09:42:08</time></div>
  <div class="comment-body"><p>网上提供的解决方法都是自己竞争对手最早发布的，Symantec的PR应该还在走流程、拿approval，正式声明估计要到下个礼拜了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">doggie</span><time class="comment-date">2007-05-19 20:09:29</time></div>
  <div class="comment-body"><p>只是在中文版xp才有这个问题，觉得symantec以后会更加重视本地化相关的测试工作，不能说fixpack在英文版测试通过了就可以发布了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-05-19 20:48:14</time></div>
  <div class="comment-body"><p>同意楼上，要做GVT</p></div>
</li>
</ol>
</section>
{% endraw %}
