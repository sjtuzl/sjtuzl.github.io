---
layout: post
title: "RIA(Flash)不能做的几件事情"
date: 2005-01-07 15:54:00 +0800
permalink: /20050107/riaflashauouatheace.html
wp_id: 303
wp_slug: "riaflashauouatheace"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>这里RIA (Rich Internet Application)专指基于Flash并运行于浏览器上的应用，如Macromedia Flex和Laszlo：</p>
<p>1. 不支持书签。Flash程序对UI的封装粒度比HTML页面大很多，若干个window<br />
form可以被塞到一个SWF文件中，由于消除了页面跳转和刷新，令程序的响应程度提高，用户体验得到改善。不过它的缺点是用户不能保存某个应用状态（如<br />
HMTL页面级别的），做一件事情只能一气呵成，否则回到原始状态就需要编程实现特定的状态维持机制了。</p>
<p>2. 点击流丢失。很多Web应用利用Web<br />
log日志文件分析用户访问模式，监测异常。高级的应用还包括数据挖掘，点击流时序分析等。由于Flash是一次下载，UI的更新和切换不需要和Web<br />
server通信，也不再有点击流这个概念。当然，从Flash利用HTTP协议可以拿一些XML格式的数据，不过这些数据已不再反映用户对内容的偏好<br />
了。</p>
<p>3. 文件上传。由于Flash player的安全考虑，Flash<br />
只能访问有限的本地文件（类似cookie），要实现一套完整的Flash商务应用，HTML的东西还是免不了的。除非Flash<br />
player放开对文件系统的限制（类似签名applet），不过这样做的话估计Flash病毒要满天飞了。</p>
<p>4. 无法保存资源。从这个角度看，到是一个保护版权的好办法。在Web上保存文本、图像、音频和视频都是很简单的事情，所有资源保持各自原有的状态，通过超链接集成到了一起；而Flash把这些资源编译成二进制格式放到SWF中，所有的东西都是能看不能拿的。</p>
<p>5. 不支持右键。我不能肯定这是不是Flash的一个限制，从我自己的实践发现右键点Flash就是一个菜单，有about什么的。缺少右键，UI的设计会比较生硬，呆头呆脑，和Win 3.1一样了。</p>
</p>
</div>
{% endraw %}
<!--more-->
