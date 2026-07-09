---
layout: post
title: "被破解的大闸蟹"
date: 2005-10-25 13:38:00 +0800
permalink: /20051025/aeaeauaoocdh.html
wp_id: 280
wp_slug: "aeaeauaoocdh"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>我怀疑自己从来没吃过正宗的阳澄湖大闸蟹，尤其是看了电视里假冒大闸蟹的新闻之后。大闸蟹像软件一样需要保护。蟹毕竟是实物，不能在蟹壳敲开后弹出一个蟹爪要你输入序列号，也不能在下锅前打电话给阳澄湖大闸蟹管理中心去激活。我所知道的保护方法，前两年是用激光标签，还有什么带“戒指”的方法。刚出来就破解了，铜仁路上到处都是带标签、带戒指的螃蟹。周末看电视，今年的做法有点技术含量了，上了短信验证。每个阳澄湖大闸蟹上印个标签，上面一个唯一序列号。向指定号码发送短信并附上该唯一号就可以知道是不是正宗阳澄湖出品的，如果是有人曾经查询过该号码则会发出警告。这个solution的成本不低，需要SP提供短信平台；所有大闸蟹的ID号需要输入到数据库；然后开发一个不太复杂的数据库访问程序。又是message queue，又是database。其实盗版大闸蟹也可以搞这么一个系统，DB用<a href="http://db.apache.org/derby/">Cloudscape</a>；Message 用<a href="http://activemq.codehaus.org/">ActiveMQ</a>；下载JRE用Eclipse开发个数据库访问程序，到网上买个硬件短信猫外加SDK，也差不多齐了。这个“盗螃蟹不盗软件”的方案除了短信猫外都是免费。蟹贩们把短信猫上的GSM卡号和序列号印在自制小商标上，破解版就能上市了。</p>
<p>阳澄湖大闸蟹自我保护的故事，是现实生活中<a href="http://www.ibm.com/news/us/en/2005/08/2005_08_04.html">Business Performance Transformation Services</a>活生生的应用，没有中间件、没有网络、没有商业模式改造，螃蟹都卖不好。是不是可以说，IT即使在一个缺乏诚信的市场里面，也是用用武之地的。</p>
</div>
{% endraw %}
<!--more-->
