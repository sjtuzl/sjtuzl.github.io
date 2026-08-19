---
layout: post
title: "Blogger API"
date: 2006-06-23 14:58:00 +0800
permalink: /20060623/blogger-api.html
wp_id: 444
wp_slug: "blogger-api"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>收到同事邮件，邀请我加入<a href="http://blog.csdn.net/group/ibmdevgroup/">CSDN IBM开发者圈子</a>。对于这个比较官方的blog，我唯一的顾虑是在选题上的谨慎，谈论的内容要会窄一些，更偏重于技术，尤其是IBM相关技术。</p>
<p>所以我打算同时维护两个博客（CSDN上的尚未开通），把有关技术的内容镜像到CSDN的圈子里；一些闲谈杂想仍旧放在此处。</p>
<p>为了简化镜像的工作量，我花了点时间考察了目前可用的blog客户端工具，这些工具可以离线的写作并自动发布到网站（多个）上而不需要用浏览器登录。blog客户端使用了一些常用的API，如Blogger API，MovableType等。</p>
<p>经研究，博客网（Bokee.com）支持的是Blogger API，其发布URL是<a href="http://publishblog.blogchina.com/xml-rpc">http://publishblog.blogchina.com/xml-rpc</a>，详细说明<a href="http://service.bokee.com/faq.html#gongshefaq08">在此</a>。</p>
<p>目前可以找到对bokee支持最好的免费工具是<a href="http://blogbuddy.sourceforge.net/">blogBuddy</a>和<a href="http://www.zoundry.com/software.html">Zoundry Blog Write</a>。blogBuddy处理Bokee很顺，没有中文编码问题，它最大不足是没有WYSIWYG编辑器和多站点配置功能。Zoundry的功能很全，可偏偏无法正确支持除UTF-8以外的编码（bokee用的是GB2312），此外其发布功能的bug也很多。</p>
<p>图：Zoundry的帐户配置和多协议支持：</p>
<p><img loading="lazy" decoding="async" align="bottom" alt=" " src="/assets/media/photos/2004_2006/zoundry_config.jpg" /></p>
<p>对于<a href="http://blog.csdn.net/">CSDN Blog</a>，我还不能确信它是否支持某种特定的Blog API（搜索了一圈也没找到）。不过凭CSDN在技术上的偏执，API的事情迟早会解决。</p>
</div>
{% endraw %}
<!--more-->
