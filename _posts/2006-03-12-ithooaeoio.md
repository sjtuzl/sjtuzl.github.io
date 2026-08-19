---
layout: post
title: "动态二进制分析"
date: 2006-03-12 09:56:00 +0800
permalink: /20060312/ithooaeoio.html
wp_id: 414
wp_slug: "ithooaeoio"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>静态代码分析扫描源代码；静态二进制分析在不运行编译好的代码情况下，对这些二进制码或字节码进行解析；动态源代码分析在预编译时插入指令然后重新编译运行；动态二进制分析是在程序运行的时候，动态的分析程序在内存中的结构并加入特定指令进行程序监控和测试。</p>
<p>对于使用VM的字节码，动态分析一般由VM提供接口实现；而对native code来说，则需要更复杂的技术实现。</p>
<p><a href="http://valgrind.org/">Valgrind</a>就是一个动态二进制分析工具，提供对C/C++二进制码的运行时解析和检测。Valgrind的作者来自剑桥大学，并在2004年发表了博士论文"<a href="http://valgrind.org/docs/phd2004.pdf">Dynamic Binary Analysis and Instrumentation</a>".</p>
</div>
{% endraw %}
<!--more-->
