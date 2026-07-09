---
layout: post
title: "快评kooxoo.com"
date: 2006-08-01 00:43:03 +0800
permalink: /20060801/kooxoo-comparison-shopping-search-engine.html
wp_id: 469
wp_slug: "kooxoo-comparison-shopping-search-engine"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>之所以要“快评”，因为到了该上床睡觉的时间了。</p>
<p><a href="http://www.donews.net/keso/">Keso</a>对<a href="http://www.kooxoo.com/">Kooxoo</a>(酷迅)的<a href="http://blog.donews.com/keso/archive/2006/07/30/981742.aspx">评价很高</a>。我读书的时候看过陈华关于北大天网FTP搜索引擎设计和实现的论文，印象挺深。搞技术的就需要这样上得厅堂、下得厨房的人。</p>
<p>Kooxoo应该算是个<a href="http://www.google.com/search?hl=en&lr=&newwindow=1&q=%22comparison+shopping%22&btnG=Search">比较购物</a>，与<a href="http://froogle.google.com/">Froogle</a>和<a href="http://www.mysimon.com/">Mysimon</a>很像。Mysimon这个东东我早年仔细研究过，后来XML, Web services火了以后就对通过wrapper解析HTML的技术淡了许多。</p>
<p>如果索引的最小单位是页面，那么如内容保护和page ranking相对都比较简单；Kooxoo实际上挖的是网上服务提供商的关系数据库，而且是在没有ODBC/JDBC data source的前提下通过HTML/HTTP尽可能的发现非精确接口，然后通过定制wrapper精确化后做内容提取。所以Kooxoo的研究的最小单位不是页面，而是一个HTML table的每一行tr/td数据，这些数据基本上没有reference可供rank，实时性又很强，能抓到已属不易。</p>
<p>当你要把对方数据库里的东西抓出来放到自己的搜索结果里面，会有多少问题，不知道。小网站能获得更多的关注度，可能很happy；大网站觉得注意力分流，并被匿名的参与到集体比价的行列中，也许不happy。在Kooxoo默默无闻的时候天下会很太平（其实Google的Froogle到现在也是很成功的），可在国内互联网大环境下，"借腹生子"发家会被"万人大签名"讨伐的（参见<a href="http://www.williamlong.info/archives/523.html">迅雷事件</a>）。</p>
<p>在分类信息检索的基础上，希望Kooxoo能提供论坛的实时检索，<a href="http://www.qihoo.com/">奇虎</a>们可提高的地方还有很多。
</p>
</p>
</div>
{% endraw %}
<!--more-->
