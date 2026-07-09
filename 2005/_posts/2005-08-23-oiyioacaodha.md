---
layout: post
title: "家庭网络连接小结"
date: 2005-08-23 10:51:00 +0800
permalink: /20050823/oiyioacaodha.html
wp_id: 157
wp_slug: "oiyioacaodha"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>周末花了两个小时把家里的网络彻底搞定，安装在房间里的5个网络接口终于可以正常工作：在无线信号弱的地方可以使用有线连接克服掉线和重新分配IP地址带来的延迟。</p>
<p>我家的家庭网络基本情况如下：</p>
<p>1. Subscribe上海电信的FTTB服务，一根网线进户；</p>
<p>2. 每个房间设置一个有线网络接口，一共5个；</p>
<p>3. 利用无线路由器(TP-Link)组家庭局域网。方法如下：</p>
<p>&nbsp;&nbsp; 3.1 进户线用568B的接法接入路由器的进户端；</p>
<p>&nbsp;&nbsp; 3.2 5个墙上网口线一端连接网络面板盒（西蒙50系列），一段用568B接法接水晶头插入路由器有线端口；</p>
<p>&nbsp;&nbsp; 3.3 网络面板盒的解法很容易，按照面板里面的颜色指示把8根线分开成章鱼状，按照568B接法把每根线嵌入到卡线槽中，用专用工具压紧（我用的是刀片，要很用力才能把导线绝缘皮划开并与面板联通）。</p>
<p>测试：</p>
<p>使用一台笔记本电脑接一根网线，依次插入到墙上面板上。接入后Windows system tray提示网络连接成功，但这并不意味着该网口可以正常工作。如果使用了DHCP动态分配IP地址的话，用ipconfig测试是否得到IP地址，如果20秒内无法得到IP地址证明要么某几根连线错接，要么接触不良。昨天测试时发现4个网络面板中有一个电工接线错误，2个接触不良。翘开面板，卸下接线盒重新压线-&gt;回归测试，最终所有网口正常工作。</p>
<p>My home network:</p>
<p><img loading="lazy" decoding="async" alt="My home network" src="/assets/media/photos/2004_2006/my-home-network.jpg" align="baseline" /></p>
</div>
{% endraw %}
<!--more-->
