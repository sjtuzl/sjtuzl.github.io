---
layout: post
title: "Windows 7自建虚拟无线WiFi"
date: 2014-09-22 16:22:45 +0800
permalink: /20140922/windows7-virtual_wifi.html
wp_id: 1143
wp_slug: "windows7-virtual_wifi"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>升级到iOS8后， Cisco LEAP协议不支持，无法连到公司内部无线网，中国移动GPRS实在太慢。找到几篇文章，使用Windows 7自带的虚拟WiFi在笔记本上自建AP，让移动设备上网，步骤简化如下：</p>
<p>1. 在管理员权限下运行命令行cmd；</p>
<p>2. 运行命令<span style="color: #0000ff;"><em> netsh wlan set hostednetwork mode=allow ssid=<strong>&lt;your_ap_name&gt;</strong> key=<strong>&lt;password&gt;</strong></em></span></p>
<p>其中<em>&lt;your_ap_name&gt;</em>是无线AP的ssid，用手机找WiFi可以发现；<em>&lt;password&gt;</em>是这个AP的连接密码；</p>
<p>3. 接着运行<span style="color: #0000ff;"><em> netsh wlan start hostednetwork</em></span>，这样在网络连接可以看到该虚拟WiFi连接：</p>
<p><a href="/assets/media/uploads/2014/09/virtual_wifi.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1145" src="/assets/media/uploads/2014/09/virtual_wifi.png" alt="virtual_wifi" width="536" height="239" /></a></p>
<p>4. 把一个实际网络连接的流量共享给该虚拟WiFi。方法是右键选择当前可用网络连接的‘属性’，然后在共享里分享给虚拟WiFi。</p>
<p>最后，如果你装了防火墙如Symantec Endpoint Protection，需要添加一条过滤规则放行移动设备对此虚拟WiFi适配器的访问。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(5)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Sean Qiu</span><time class="comment-date">2014-09-22 17:20:41</time></div>
  <div class="comment-body"><p>Operation不让自建热点，需要走流程。。。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2014-09-22 23:27:20</time></div>
  <div class="comment-body"><p>会有IBMVISITOR的新AP，不知道什么时候能布好。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vincent</span><time class="comment-date">2014-11-04 14:49:15</time></div>
  <div class="comment-body"><p>之前通过申请证书的方式可以上网<br>
然后没过多久就被封杀了<br>
不过之前申请证书的话还可以继续使用</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">chenzhi</span><time class="comment-date">2015-04-09 16:25:38</time></div>
  <div class="comment-body"><p>有新办法，去下个Apple configuration,然后可以给IOS8新建一个wifi LEAP的profile，导入到手机之后就可以上公司网络了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Ling Zhang</span><time class="comment-date">2016-06-03 10:04:52</time></div>
  <div class="comment-body"><p>现在都是证书认证了，包括移动和桌面</p></div>
</li>
</ol>
</section>
{% endraw %}
