---
layout: post
title: "Lost in Translation"
date: 2005-09-12 15:14:00 +0800
permalink: /20050912/lost-in-translation.html
wp_id: 259
wp_slug: "lost-in-translation"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>星期六晚上去了浦东联洋社区的<a href="http://www.papajohns.cn/">Papa John's</a>吃匹萨。自大拇指广场开张后，是第一次来参观。几个篮球场大小的范围内聚集了KFC、MAC、PizzaHut、Papa John's、味千、避风塘、许留山、Starbuck等餐饮店。这里老外人数不少，拖家带口的，我隔壁的一桌是老说中、少说英；人走撤掉后新来的一对又开始说日本话。在这里当服务员不容易。</p>
<p>传说中的Papa John's的双味pizza感觉也就一般，可能期望值比较高，价格方面和PizzaHut基本相当。倒是结帐时的收据引起了我的注意：在收银条的最下方写着“变化：10.0 RMB”。一共110块的餐费付了120块，这10块显然是找零，也就是change了。据此可以猜想Papa John's的POS系统的本地化是这么完成的：</p>
<p>1. 把英文版系统中所有硬编码的英文字符串抽取出来，放到一个文本文件中；</p>
<p>2. 把该文本文件交给翻译提供商进行中文翻译；</p>
<p>3. 把翻译好的字符串重新放回到程序中。</p>
<p>可惜在翻译的时候，由于缺少了上下文环境，单看一个“change”，谁来翻都得翻成“变化”。对于用餐的人来说，自然“迷失在翻译中”了。以前还曾经在一本IBM白皮书中文版里面看到过“登台服务器”这个名词，觉得非常纳闷，参照原文一看，原来是“staging server”，跑的太远了。</p>
<p>不知道技术翻译行业里面有没有context awareness translation一说，让翻译者看到被翻译文字所处的上下文不应该是optional，而是must。</p>
</div>
{% endraw %}
<!--more-->
