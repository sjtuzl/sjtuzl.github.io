---
layout: post
title: "第三方ESB"
date: 2006-08-07 23:21:52 +0800
permalink: /20060807/amazon-enterprise-esb.html
wp_id: 476
wp_slug: "amazon-enterprise-esb"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>“企业不想买基础软件，已经很久了”。不是吗，几年前的ASP (Application Service Provider)，现在的<a href="http://www.salesforce.com/">Salesforce</a>们。企业信息化的最高境界就是没有IT，可能吗？不可能，至少在现在，至少那些依靠IT运行核心业务的组织，IT的基础设施不在自己的手里，晚上觉都睡不好。</p>
<p>但选择也越来越多，市中心的房子买不起，就买外环、郊环，只要轨道交通能跟上。而Amazon，正在修自己的地下铁。</p>
<p>我是在公司内部博客看到这条消息的，Amazon开放了一个类似ESB的东西，提供有偿的服务供使用者开发基于XML/Web services的消息应用，允许创建消息队列、访问和管理消息，而Amazon不仅仅是网上卖打折书的商人，它在卖IT基础设施、在卖数据、在卖服务。</p>
<p>这是一个更虚拟化的应用，amazon不再出现在网页里，而是隐藏在一个个的函数调用中。来研究一下两个小企业（或者企业内部）做数据交换的过程，在没有IT系统的情况下最简单的方法就是发email，一个报价单或者支出信息写成文本，正规点的用excel做张表，发给对方；对方收到好把里面和数据相关的信息抓出来，放在自己的文本文件或者excel表格里，从而完成一个非常典型的交互过程。如果有了第三方的ESB，发数据的一方使用浏览器访问Amazon的消息队列，添加新消息；接受方同样使用浏览器下载新消息，在消息规范和格式预先定义的情况下，这个过程可以相当程度的自动化，数据的生成、保存都能更结构化一些，况且我们还可以使用RIA, fat client去消费这些消息。</p>
<p>消息仅仅是共享总线的一个表现形式，blog、RSS何尝不是，再松一点甚至贴吧、QQ群都能算上，只要满足下面这些条件：</p>
<p>1. 第三方的通信中介和存储中介；</p>
<p>2. 可编程的访问接口；</p>
<p>3. 最大限度的开放标准和协议。</p>
<p>现在的问题是，谁来解决寻址的问题，需要另一个ESB的UDDI吗？那些智能的agent、collaboration tool和workflow是不是也要闻风而动了呢？创新让每个人都激动起来，的的确确是件好事。</p>
<p>参考阅读：</p>
<p><a href="http://www.amazon.com/b/ref=sc_fe_l_2/102-7175372-2120905?ie=UTF8&node=13584001&no=15879911&me=A36L942TSJ2AJA">Amazon Simple Queue Service (Amazon SQS)<br />
</a></p>
<p><span class="small" /></p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">老熊</span><time class="comment-date">2006-08-09 11:51:51</time></div>
  <div class="comment-body"><p>amazon玩玩可以，小公司玩这个东西搞不好就成为先烈了，尤其是国内环境。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-08-09 22:42:10</time></div>
  <div class="comment-body"><p>嗯，国内是两包花生米，一瓶啤酒，哈哈</p></div>
</li>
</ol>
</section>
{% endraw %}
