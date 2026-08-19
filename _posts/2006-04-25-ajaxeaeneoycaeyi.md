---
layout: post
title: "Ajax让搜索引擎抓瞎"
date: 2006-04-25 14:26:00 +0800
permalink: /20060425/ajaxeaeneoycaeyi.html
wp_id: 428
wp_slug: "ajaxeaeneoycaeyi"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>如果<a href="http://www.zhuaxia.com/">抓虾</a>坚持继续使用Ajax在客户端动态生成网页的话，那么可能在Google中搜索“抓虾”大概永远只能返回1到2个链接。Ajax让搜索引擎彻底“抓瞎”。</p>
<p>由于网页在下载到客户端后由JavaScript动态生成，在用浏览器“查看源代码”是看不到当前显示的网页内容的，仅仅是一些链接和一堆included JavaScript。Crawler从主页进去后，转了几圈除了首页、“关于我们”之外将一无所获，因为几乎不会有什么Web crawler会在server端运行爬到的JavaScript代码。我猜Googlebot在抓虾的停留时间不会超过30秒（请虾米们查看一下你们的Web日志）。</p>
<p>当然，让不让crawler停留完全由网站决定，从“<a href="http://www.zhuaxia.com/robots.txt">http://www.zhuaxia.com/robots.txt</a>”可以看出抓虾的技术人员是很专业的，屏蔽了几个系统目录的访问权限。其实，由于上述原因，这个robots.txt文件目前来说略显多余，能挡住<a href="http://www.koders.com/">http://www.koders.com/</a>就很好了。</p>
</div>
{% endraw %}
<!--more-->
