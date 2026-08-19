---
layout: post
title: "看一个房产论坛敏感词过滤功能的实现"
date: 2004-10-29 18:43:00 +0800
permalink: /20041029/oouauiaodheyaeauuaeuio.html
wp_id: 95
wp_slug: "oouauiaodheyaeauuaeuio"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>房产之窗： <a href="http://bbs.ehomeday.com/list_2.htm" target="_blank">http://bbs.ehomeday.com/list_2.htm</a></p>
<p>用浏览器打开后，选择"查看代码"(View source)，在HTML代码的上面有一段JavaScript，大家好好研究研究。</p>
<p>我对其中有个词感到疑惑，就是这个"靠"字。因为它可以和很多词搭配使用，如依靠，靠近，等。把它单独拎出来过滤会影响不少短语和句子，而且发贴人看到帖子不被系统接受也不知道是什么原因。</p>
<p>把敏感词放在客户端的做法实在是很古怪，让人觉得很不聪明，这等于暴露出自己的审查逻辑。这就好比在招聘网上提交简历的时候让用户看见：if (学历 != 硕士) { resume.sendToTrash();}</p>
<p>我前几天在搜房网的论坛上发了一个帖子，被系统据收，说有不妥词语，检查半天没发现。后来研究发现句子里面包含了"篱笆网"三个字。<a target="_blank" href="http://www.51tuangou.com/bbs">篱笆网</a>是上海很有名的房屋装修论坛，而搜房也有自己的装修论坛，显然是想屏蔽竞争对手，而采用这种手段实在是不光彩。</p>
</div>
{% endraw %}
<!--more-->
