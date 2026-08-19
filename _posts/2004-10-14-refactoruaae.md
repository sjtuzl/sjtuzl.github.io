---
layout: post
title: "refactor的粒度"
date: 2004-10-14 19:44:00 +0800
permalink: /20041014/refactoruaae.html
wp_id: 115
wp_slug: "refactoruaae"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>我现在正在做一个refactor的项目。其实我自己并不怎么用eclipse的refactor，因为怕被re后的代码自己又要去重新理解。所有人都喜欢自己能够理解的东西，即使这个东西不怎么样。refactor要做的就是把一个被公认不高的代码转换成质量高的代码。我在想的一个问题是：refactor的粒度如何设定？<br />
<br><br />
<br>现在eclipse上的refactor工具基本上还比较简单，如更改类名、变量名、方法抽取等，经它们更改后的代码都比较容易理解，因为没有结构和设计上的改动，refactor做的事仅仅事帮助你自动的完成相关部分的更新（比如更改一个类名后其它代码中引用改类的地方要相应修改）。<br />
<br><br />
<br>目前有人在研究更深层次的问题，就是代码结构和设计的修改，意在把bad code经refactor转换成符合design pattern的新代码。先不说技术上如何实现，想想一个刚出道的程序员，一共写了10了类，50个方法，经这个工具一转成了15个类，70个方法，而且还都符合design pattern。这样的代码让这个程序员怎么理解？如此一来，新手哪里敢用？结构再好、再完善的东西，不能理解也白搭，最终还是要这个初级程序员完成编程工作，而他无法在自己不能理解的代码上工作。<br />
<br><br />
<br>我想，现在refactor的工具还是会侧重于局部代码的修葺，能促使大家都能主动使用这样的功能已经是很了不起了。</p>
</div>
{% endraw %}
<!--more-->
