---
layout: post
title: "CSDN论坛stylesheet的路径问题"
date: 2006-07-15 12:51:40 +0800
permalink: /20060715/csdn-forum-stylesheet-path.html
wp_id: 456
wp_slug: "csdn-forum-stylesheet-path"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>FF访问CSDN论坛遇到困难，XML数据无法被render（见下图）。IE访问一切正常。</p>
<p><img loading="lazy" decoding="async" src="/assets/media/photos/uploads/2006/07/csdn-forum-xslt.gif" /></p>
<p>View source后看到XML中对XSLT的引用是这样写的：<em><span class="pi">href='/expert/Xsl/2.xsl'</span></em></p>
<pre id="line1"><span class="pi" /></pre>
<p><span class="pi"> FF无法正确解释相对URL，IE则没问题。把两个文件下载到本地，修改href为绝对地址FF正确render出XML。</span></p>
<p>用FF访问CSDN的人按说很多啊，怎么就没修复呢？</p>
<p>PS: 现在美女作家都已经渗透到程序员的队伍中了（一直听说孙卫琴的名字，以为是个阿姨呢）</p>
<p><a href="http://www.dearbook.com.cn/2006/javaobjectcoding/index.htm">http://www.dearbook.com.cn/2006/javaobjectcoding/index.htm</a></p>
</div>
{% endraw %}
<!--more-->
