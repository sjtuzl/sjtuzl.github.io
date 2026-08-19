---
layout: post
title: "GAIM与cygwin冲突解决方法"
date: 2005-09-13 13:28:00 +0800
permalink: /20050913/gaimoecygwinaiao.html
wp_id: 260
wp_slug: "gaimoecygwinaiao"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>上周五为了在Eclipse CDT下编译调试C/C++程序，安装了<a href="http://sourceware.org/cygwin/">Cygwin</a>。随后发现<a href="http://gaim.sourceforge.net/">GAIM</a>无法正常工作，启动后GAIM进程保留但界面消失。</p>
<p>讨论组证实了该问题，给出的解决方法是在system path中去掉cygwin/bin，虽然可以解决GAIM的问题， 但由于路径丢失Eclipse中无法调用g++。综合多方线索，找到的最佳解决方案为：保留系统路径中cygwin/bin目录，将cygwin/bin目录下的tcl84.dll和tclpip84.dll改名禁用即可。</p>
<p>以上解决方案在GAIM 1.5, Cygwin 2.51下验证通过。</p>
</div>
{% endraw %}
<!--more-->
