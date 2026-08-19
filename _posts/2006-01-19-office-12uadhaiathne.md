---
layout: post
title: "Office 12的新文件格式"
date: 2006-01-19 11:04:00 +0800
permalink: /20060119/office-12uadhaiathne.html
wp_id: 398
wp_slug: "office-12uadhaiathne"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>MS Office的文件格式到12之前是开放给微软合作开发商的，并不直接对外公布格式细节。早年就有国内高人自主研究Word格式并写出了杀宏病毒的工具。</p>
<p>Office 12 Word文件的扩展名是.docx，以标准zip格式压缩存储（与Java的.jar文件类似）。压缩包内包含了XML数据文件、样式表与元数据（macro可能需要单独的.vbs文件存储）。</p>
<p>打包存储在IE里已经存在多年：IE支持把一个Web页面中的所有元素，包括HTML，图片和脚本保存在.mht文件中。.mht格式实际上是一个MS Outlook可以识别的邮件格式，如果把扩展名改成".eml"，双击就可以在Outlook Express里读到完整的Web内容了。不过.mht和.docx相比，革命程度还稍弱一点。</p>
<p>开放的Office文件格式给基于数据集成的应用和它们的下游开发商提供了新的机会。就像2000年以前还有不少应用通过HTML Wrapper解析HTML文件，抽出里面的表格和数据自动填充到数据库或者其他什么地方，而2000年后，有了XML有了Web Services，这样的脏活就没人干了。</p>
<p>另外我发现目前颇流行的<a href="http://widgets.yahoo.com/">Yahoo Widgets</a>中，每个独立的widget也是用Zip压缩，打包了用来定义UI的XML描述文件和用来控制交互的JavaScript脚本。</p>
</div>
{% endraw %}
<!--more-->
