---
layout: post
title: "Why localization"
date: 2005-10-30 12:34:00 +0800
permalink: /20051030/why-localization.html
wp_id: 281
wp_slug: "why-localization"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>在商店买东西的时候，我常常会去瞄一眼收银员用的终端系统，看看上面跑的是什么应用程序。今天下午去了浦东龙阳路百安居旁边的<a href="http://www.decathlon.com.cn/site/cn/corporate/New/chinese%20index/en%20index.htm">迪卡侬</a>体育用品专卖店。与宜家类似，迪卡侬也在货架周围放一些售货员用的终端。在LP试衣服的时候，我站在一个售货员后面，偷偷看他操作电脑，并有幸看到一次系统重启。经观察，迪卡侬的客服终端架构基本如下：</p>
<p>1. 终端使用Windows 2000 Professional；</p>
<p>2. 系统启动后不需输入用户名密码自动登录到桌面，然后自动运行3个扩展名为cmd的脚本程序。在其中一个console中看到有映射远程驱动器的操作。</p>
<p>3. 脚本运行完毕，自动弹出IE窗口（桌面上没有“开始”菜单和工具条，无桌面图标）。此IE窗口无地址栏，在工具栏上增加了一个红色按钮。(可能被<a href="http://www.microsoft.com/technet/prodtechnol/ie/ieak/default.mspx">IEAK</a>定制过)。之后连接首页，是内部的货品管理系统。在IE的窗口栏上，看到标题是“Jakarta<br />
Jetspeed”，可知使用了开源的<a href="http://portals.apache.org/jetspeed-1/">Jetspeed Java<br />
server</a>。在首页上摆放了很多的链接和图标。</p>
<p>4. 售货员点了浏览器页面里的一个图标，居然弹出了一个客户端应用程序，就像Java<br />
Webstart一样，很神奇，没搞明白。按道理说应该是一个对话框，指示是否要保存或者执行，这个是不是就是传说中的Windows smart<br />
client？我猜想这个客户端程序是在远程服务器上，通过驱动器映射到本地，并用超链接的方式挂在了首页上。</p>
<p>5. 客户端程序应该是Delphi写的，因为看到了那个带绿色大勾和红色大叉图标的按钮。登录窗口后是一个导航窗口，下面有一个checkbox是&quot;Show<br />
Help Buddy&quot;。可惜没看到这个Help Buddy长什么样，和MS<br />
Office的回形针、小海豚、孙悟空有什么区别。主窗口最顶端是一排工具栏，只有图标没有文字，最后一个图标是&quot;Euro<br />
calc&quot;。迪卡侬是法国店，有这个需要。其他没有什么特别的，很普通的Windows程序，整个程序的界面都是英文的。</p>
<p>为什么不汉化这个客户端程序？也许招懂英文的服务员所多支付的薪水比汉化程序更便宜，风险更小。且不说在外国人的商店工作懂英文已经是很基本的要求了，就是用中文的POS机，看不懂&quot;price,<br />
receipt&quot;的也不容易混下去了。给knowledge<br />
worker使用的内部工具汉化的需求比较弱，就像万用表上用英文刻度一样没问题，但换成微波炉洗衣机的面板，还是中文的为好。</p>
</p>
</div>
{% endraw %}
<!--more-->
