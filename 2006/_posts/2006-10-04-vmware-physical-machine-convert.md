---
layout: post
title: "VM update"
date: 2006-10-04 20:27:42 +0800
permalink: /20061004/vmware-physical-machine-convert.html
wp_id: 512
wp_slug: "vmware-physical-machine-convert"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>本周一刚放出的<a href="http://www.vmware.com/products/beta/converter/">VMWare Converter Tool</a>又向前迈进了一步：它可以把一台物理机器转换成一个virtual machine，重新部署到其他VM环境中去。我对VMWare下两步的期望包括：</p>
<p>1. 把一个VM转换成一台物理机器，实现测试环境到生产环境的快速转换；</p>
<p>2. 把一个“活”的VM备份下来，从数据角度看，不仅仅是文件系统，还包括内存snapshot、磁盘交换数据、寄存器等等，完完整整的把一个运行中的系统镜像到另外一个系统中去，像休眠和苏醒一样。调试，性能分析、负载均衡等多个应用都可能是受益者。</p>
<p>Virtualization是个越来越热门的话题，当然还有来自IBM的virtualization技术与相关产品（<a href="http://www-03.ibm.com/systems/virtualization/">IBM Virtualization</a>）。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(3)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Terry</span><time class="comment-date">2006-10-04 21:58:01</time></div>
  <div class="comment-body"><p>1已经被实现了，几年前尝试把gpim部署到demo net去的时，对方提到他们能把vm转到物理机上，不知道他们用什么软件来搞这个。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-10-05 09:18:02</time></div>
  <div class="comment-body"><p>VMWare下面好像没有这样的工具。会不会在VM跑的时候做个ghost镜像什么的装在物理机上？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Terry</span><time class="comment-date">2006-10-07 20:39:03</time></div>
  <div class="comment-body"><p>有可能，用ghost镜像来做应该还是可行的，加上一些手动的步骤。</p></div>
</li>
</ol>
</section>
{% endraw %}
