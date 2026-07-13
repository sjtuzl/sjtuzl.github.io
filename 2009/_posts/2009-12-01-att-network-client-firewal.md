---
layout: post
title: "关闭AT&T Network Client内置防火墙"
date: 2009-12-01 21:55:54 +0800
permalink: /20091201/att-network-client-firewal.html
wp_id: 784
wp_slug: "att-network-client-firewal"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>家里一台电脑，能ping通网关和其他电脑，但其他电脑无法ping通该机器，上面的FTP服务也连接不上。关闭了安装的防火墙问题仍旧。后来发现因为安装了AT&amp;T Network Client VPN，而其自带的防火墙将屏蔽ICMP和某些端口的访问。</p>
<p>关闭AT&amp;T Network Client内置防火墙方法如下：</p>
<p>1. 到安装目录，找到并运行‘NetFW.exe’；</p>
<p>2. 点击‘Turn OFF’，关闭防火墙，执行后效果如下：</p>
<p><a href="/assets/media/uploads/2009/12/ATT_Firewall.PNG"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-785" title="ATT_Firewall" src="/assets/media/uploads/2009/12/ATT_Firewall.PNG" alt="ATT_Firewall" width="480" height="344" /></a></p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(5)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">匿名</span><time class="comment-date">2010-03-04 02:03:07</time></div>
  <div class="comment-body"><p>太有用了。。我碰到的问题是upnp不能自动端口映射，关掉就好了</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">ripley</span><time class="comment-date">2010-04-13 20:34:18</time></div>
  <div class="comment-body"><p>嗯，这个东西隐蔽的太好了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">feng hong</span><time class="comment-date">2010-04-14 21:36:15</time></div>
  <div class="comment-body"><p>iphone怎么样可以连到AT&amp;amp;T的VPN里面呢?要是可以就方便了撒</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2010-04-26 20:31:09</time></div>
  <div class="comment-body"><p>iphone上的VPN方案已经有了，可以上Traver了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Luojingw</span><time class="comment-date">2010-05-19 05:41:37</time></div>
  <div class="comment-body"><p>iPhone 上具体怎么弄呢？愿闻其详哦！:)</p></div>
</li>
</ol>
</section>
{% endraw %}
