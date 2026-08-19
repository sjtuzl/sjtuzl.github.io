---
layout: post
title: "把Fiddler配置成reverse proxy"
date: 2014-08-01 17:30:37 +0800
permalink: /20140801/config-fiddler-as-reverse-proxy.html
wp_id: 1027
wp_slug: "config-fiddler-as-reverse-proxy"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Fiddler是用作Web调试的工具，因为一个需求想自己搭一个简单的reverse proxy，试了几个工具都不太好用。做了些功课发现可以把Fiddler配置成reverse proxy。大致步骤如下：</p>
<p>1) 配置成Fiddler的侦听端口</p>
<p>这个很容易，在平时用作调试的时候就已经有了。需要注意的是要允许其他电脑访问Fiddler服务；</p>
<p><a href="/assets/media/uploads/2014/08/fiddler1.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1028" src="/assets/media/uploads/2014/08/fiddler1.png" alt="fiddler1" width="558" height="371" /></a></p>
<p>2) 侦听HTTPS端口</p>
<p>侦听HTTS端口在界面上没有办法配置，需要在Fiddler QuickEexc命令行里输入：<strong><em>!listen 443 proxy.mycompany.com</em></strong></p>
<p><a href="/assets/media/uploads/2014/08/fiddler2.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1030" src="/assets/media/uploads/2014/08/fiddler2.png" alt="fiddler2" width="505" height="49" /></a></p>

<p>3) 定制HTTP  response处理脚本</p>
<p>Reverse proxy最重要的一个功能是对返回的HTTP response进行预处理，之后再返回给浏览器。比如把嵌入在HTML中的所有绝对URL的hostname变成reverse proxy自己的hostname，这样才能保证用户后续的访问可以指向正确的服务器地址。Fiddler提供了脚本支持来完成对HTTP response的修改。</p>
<p>你可以使用Fiddler的菜单调出脚本用文本编辑器进行编辑，或者安装FiddlerScript插件进行开发（有代码提示功能）。</p>
<p><a href="/assets/media/uploads/2014/08/fiddler3.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1032" src="/assets/media/uploads/2014/08/fiddler3.png" alt="fiddler3" width="717" height="338" /></a></p>
<p>你可能需要定制的地方包括：</p>
<p><strong>3.1）对所有HTTP 302进行截获，把重定向地址改成reverse proxy自己的地址，代码大致如下：</strong></p>
<p><em>static function OnBeforeResponse(oSession: Session) {</em></p>
<p><em>..</em></p>
<p><em>if (oSession.HostnameIs("server.mycompany.com")){</em><br />
<em>            var redirect = oSession.oResponse.headers.AllValues("Location");</em><br />
<em>            if (redirect != "") {</em><br />
<em>                redirect = redirect.replace("server.mycompany.com", "proxy.mycompany.com");</em><br />
<em>                oSession.oResponse.headers.Remove("Location");</em><br />
<em>                oSession.oResponse.headers.Add("Location", redirect);</em><br />
<em>            }</em></p>
<p><em>...</em></p>
<p><strong>3.2) 对所有HTTP response 200的正文进行扫描，替换掉里面嵌入的绝对URL：</strong></p>
<p><em>  if (oSession.oResponse.headers.ExistsAndContains("Content-Type","text/html")){</em><br />
<em>                oSession.utilDecodeResponse();</em><br />
<em>                oSession.utilReplaceInResponse("server.mycompany.com","proxy.mycompnay.com"); </em><br />
<em>            }</em><br />
<em>            </em><br />
<em>        }</em></p>

<p>现在可以启动你的本地浏览器来访问用Fiddler搭成的reverse proxy了: http://proxy.mycompany.com/</p>
<p><strong>附</strong>：Fiddler配置为reverse proxy的官方文档（不详细，要结合本文内容）- <a href="http://docs.telerik.com/fiddler/configure-fiddler/Tasks/UseFiddlerAsReverseProxy">http://docs.telerik.com/fiddler/configure-fiddler/Tasks/UseFiddlerAsReverseProxy</a></p>
</div>
{% endraw %}
<!--more-->
