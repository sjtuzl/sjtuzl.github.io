---
layout: post
title: "GMail界面响应速度为什么这么快"
date: 2004-10-07 21:51:00 +0800
permalink: /20041007/gmailcaaeiioeueieaoaai.html
wp_id: 114
wp_slug: "gmailcaaeiioeueieaoaai"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Gmail的JavaScript用的相当多，用的也很好。整个JavaScript函数的大小在150K左右，在IE的cache文件夹里可以找到。这些函数名似乎都经过了处理，均为两个字母而且毫无规律，但函数内容是可以读懂的。</p>
<p>界面响应快不仅仅全靠JavaScript，用IE访问的时候，Gmail使用了微软的XMLHTTP组件，可以直接在IE中访问远程服务器的内容而不需要刷新页面。类似于一个远程调用，通信协议是HTTP，数据协议是XML。</p>
<p>Gmail的地址簿是在加载的时候全部下载到本地的，这才有了输入对方地址时自动出现地址提示的功能。（Yahoo Mail最近也实现了此功能）。</p>
<p>用JavaScript操纵界面在目前来说，是在HTML的标准下唯一的方法。但显然不是一个好方法，其笨拙和调试的复杂性比rich client烦很多。</p>
</p>
</div>
{% endraw %}
<!--more-->
