---
layout: post
title: "折腾"
date: 2009-11-04 22:37:03 +0800
permalink: /20091104/wordpress_upgrade.html
wp_id: 777
wp_slug: "wordpress_upgrade"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>昨天发贴后，发现右边的sidebar跑到了屏幕底部，本来以为是贴图太大撑开了，但缩小后还没解决，而且在view source的时候看到了很多隐藏的SPAM link。Dreamhost早就发邮件提醒我老版本的WordPress有安全漏洞，索性一把升级到2.8.5。</p>
<p>升级后首先是显示乱码，折腾了一段PHP总算搞定；接着发现SPAM的link不仅存在于贴子里，在&lt;body&gt;后面也有，不知来自何处。接着就折腾MySQL，在700多条帖子中发现50多条被感染 - 手工铲除SPAM link。然后再解决&lt;body&gt;的问题，根源是PHP文件被感染，很多文件头加入如eval(base64_decode('aW..的方法，SPAM link被Base64编码，一一清除后页面内所有的隐藏SPAM。</p>
<p>最后是修改了一下缺省的Theme，换了白底，banner的图片改了一下，去掉了灰边，增加了页面的宽度毕竟已经是宽屏时代了。最后测试IE, Firefox兼容性。</p>
<p>几个小时就这么容易的折腾掉了。</p>
</div>
{% endraw %}
<!--more-->
