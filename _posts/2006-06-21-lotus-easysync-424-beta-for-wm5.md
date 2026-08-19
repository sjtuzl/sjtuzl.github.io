---
layout: post
title: "Lotus EasySync 4.2.4 Beta for WM5"
date: 2006-06-21 13:28:00 +0800
permalink: /20060621/lotus-easysync-424-beta-for-wm5.html
wp_id: 443
wp_slug: "lotus-easysync-424-beta-for-wm5"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>在公司内部新闻组上看到Lotus EasySync 4.2.4 for Windows Mobile 5的Beta版在内部开始提供下载。去年底我在Dell X51上装4.2.3报错，在论坛上看到很多人报这个<a href="http://www-1.ibm.com/support/docview.wss?fdoc=wplceasy&rs=465&uid=swg21220175">兼容性问题</a>，现在支持WM5的新版本终于出来了。</p>
<p>基于WM5的标准开发工具是VS.NET 2005，它用新的MFC 8.0 for Device代替了老版本的MFC 3.0 for Devices。所以用老版本eVC开发的项目如果引用了MFC 3.0的类库，在<a href="http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnppcgen/html/migrating_evc_vs2005.asp">移植到VS.NET 2005</a>后就会出现编译错误。而就目前情况看，预装了Windows Mobile 5.0的Pocket PC设备其内置的MFC类库版本仍然是3.0。</p>
<p>从Pocket PC 2003移植到Windows Mobile 5是相当痛苦的过程，尤其对developer来说。</p>
</div>
{% endraw %}
<!--more-->
