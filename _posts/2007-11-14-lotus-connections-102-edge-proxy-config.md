---
layout: post
title: "Connections 1.0.2 edge server配置"
date: 2007-11-14 21:04:05 +0800
permalink: /20071114/lotus-connections-102-edge-proxy-config.html
wp_id: 695
wp_slug: "lotus-connections-102-edge-proxy-config"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>这几天在帮助Connections的客户配置edge reverse proxy，下面是目前使用到的全部配置列表（安装了Blogs，dogear和Activities）：</p>
<p>ServerInit C:\Progra~1\IBM\edge\cp\lib\plugins\mod_rewrite\mod_rw.dll:modrw_init Transmogrifier</p>
<p>Transmogrifier C:\Progra~1\IBM\edge\cp\lib\plugins\mod_rewrite\mod_rw.dll:modrw_open:modrw_write:modrw_close:modrw_error</p>
<p>SSLEnable       On</p>
<p>SendRevProxyName      yes</p>
<p>Enable PUT<br />
Enable DELETE</p>
<p>Map /blogs/* /connections/blogs/*<br />
Map /dogear/* /connections/dogear/*<br />
Map /activities/* /connections/activities/*</p>
<p>JunctionRewrite on</p>
<p>Proxy /connections/* http://wasserver/* :80<br />
Proxy /connections/* https://wasserver/*:443</p>
<p>ReversePass    http://wasserver/* http://myserver.com/connections/*<br />
ReversePass    https://wasserver/*    https://myserver.com/connections/*</p>
<p>JunctionReplaceUrlPrefix http://wasserver/* http://myserver.com/connections/*<br />
JunctionReplaceUrlPrefix https://wasserver/* https://myserver.com/connections/*</p>
<p>MaxContentLengthBuffer   5M</p>
<p>KeyRing C:\Progra~1\IBM\key.kdb</p>
<p>KeyRingStash C:\Progra~1\IBM\key.sth</p>
<p>最后两项的key database文件需要利用ikeyman导入WebSphere for IBM HTTP Server （IHS） plugins的证书以建立edge server和IHS之间的SSL连接。</p>
<p>此文专为搜索引擎供稿。
</p>
</p>
</div>
{% endraw %}
<!--more-->
