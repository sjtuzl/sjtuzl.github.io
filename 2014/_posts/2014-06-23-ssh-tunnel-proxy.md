---
layout: post
title: "利用SSH Tunnel实现一键翻墙"
date: 2014-06-23 15:30:09 +0800
permalink: /20140623/ssh-tunnel-proxy.html
wp_id: 921
wp_slug: "ssh-tunnel-proxy"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>首先，’一键翻墙‘并不是真正的’一键‘，在Firefox用此方法至少需要三键，而且这个方法的门槛不低，不仅需要一个可以提供SSH访问的中继服务器，客户端的设置也比较麻烦，所以本方法不适用非IT人士。</p>
<p>步骤：</p>
<p>1. 首先你需要一个提供SSH的中继服务器，这里以dreamhost.com为例。如果购买过dreamhost的虚拟主机服务的用户，在<a href="https://panel.dreamhost.com/">https://panel.dreamhost.com</a> 上创建可以使用访问SSH的用户账户，利用该账户可以SSH到服务器:</p>
<p style="text-align: center;"><a href="/assets/media/uploads/2014/06/dreamhost.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-923" title="dreamhost" src="/assets/media/uploads/2014/06/dreamhost.png" alt="" width="640" height="300" /></a></p>
<p>2. 用Putty(一个Windows 上的SSH客户端软件)创建一个SSH Tunnel，以在客户端创建一个可供浏览器使用的代理服务器。首先，输入dreamhost的主机名、端口号，然后到Connections -&gt; SSH -&gt; Tunnels窗口，选择’Dynamic'，然后输入一个本机端口号，如9999，然后点'Add'，完成后把该配置在Putty内保存成一个‘Saved Session’： 注意保存后的配置名在之后的配置中会使用到。</p>
<p style="text-align: center;"><a href="/assets/media/uploads/2014/06/putty.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-924" title="putty" src="/assets/media/uploads/2014/06/putty.png" alt="" width="640" height="300" /></a></p>
<p>3. 安装两个Firefox插件。</p>
<p><strong>插件1</strong>： Proxy Selector - <a href="https://addons.mozilla.org/en-US/firefox/addon/proxy-selector/">https://addons.mozilla.org/en-US/firefox/addon/proxy-selector/</a>。这个插件允许在Firefox上配置多个备选proxy，并快速切换。这里我们配置一个本地localhost的代理服务器，其端口号为上步在putty的Tunnels中配置的9999端口。注意需要把代理类型设置为‘Socket 4’。</p>
<p style="text-align: left;"><a href="/assets/media/uploads/2014/06/proxy_config.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-926" title="proxy_config" src="/assets/media/uploads/2014/06/proxy_config.png" alt="" width="500" height="420" /></a><strong></strong></p>
<p style="text-align: left;"><strong>插件2</strong>：External application Button - <a href="https://addons.mozilla.org/en-US/firefox/addon/external-application-button">https://addons.mozilla.org/en-US/firefox/addon/external-application-button</a>/ 这个插件的作用是在Firefox上创建运行本地应用程序的快捷方式，用来快速启动putty命令行方式（可预先配置好用户名和密码）。</p>
<p style="text-align: left;"><a href="/assets/media/uploads/2014/06/extapp_config.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-928" title="extapp_config" src="/assets/media/uploads/2014/06/extapp_config.png" alt="" width="600" height="400" /></a></p>
<p style="text-align: left;">这里我们建立了一个快捷方式，指向了一个bat文件<em><strong>startPuttySilent.bat</strong></em>。此bat文件内容如下：</p>
<p><em>start "" c:\app\putty.exe -load "tournemire.dreamhost.com" -l &lt;USERNAME&gt; -pw &lt;PASSWORD&gt;</em></p>
<p>注意这里带了双引号的tournemire.dreamhost.com并不代表一个服务器，而是你在步骤2中在Putty上定义的‘Saved Session’名字，你可以取如 'My proxy server’这样的名字，它实际指向了putty中该配置中定义的SSH服务器地址。</p>
<p>-l和-pw分别为用户名和密码。如果担心安全问题，可以不指定，而是在每次启动SSH连接的时候手工输入。命令行前使用了‘start...’ 的目的在于启动后只保留putty的命令行窗户，而原始的Windows命令行窗口关闭，否则会显示两个黑窗口。</p>
<p>现在需要的配置都完成了，当你需要启动代理翻墙的时候只需要：</p>
<p><strong>1. 在Firefox中Proxy Selector插件选项定义好的本地代理(2键)；2) 在Firefox点击定义好的外部putty应用快捷方式 (1键) - 最快3键可以完成代理切换。</strong></p>
</div>
{% endraw %}
<!--more-->
