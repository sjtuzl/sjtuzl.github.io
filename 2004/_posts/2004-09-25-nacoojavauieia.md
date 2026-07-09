---
layout: post
title: "惭愧，一个Java基本问题"
date: 2004-09-25 19:39:00 +0800
permalink: /20040925/nacoojavauieia.html
wp_id: 112
wp_slug: "nacoojavauieia"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Java对所有对象型参数的传递都是传引用的（by reference），在传入的函数体内修改该对象会对指向该对象的所有instance进行修改。但如果是创建一个新instance给该对象呢？如：</p>
<p><font color="#0000ff">Vector v = new Vector();</font></p>
<p><font color="#0000ff">v.addElement("a");</font></p>
<p><font color="#0000ff">change(v);</font></p>
<p><font color="#0000ff">System.out.println(v.size());</font></p>
<p>..</p>
<p><font color="#0000ff">private void change(vector v) {</font></p>
<p><font color="#0000ff">v= new Vector();</font></p>
<p><font color="#0000ff">}</font></p>
<p><font color="#000000">最后的打印结果是1，即在函数内创建新实例的话并不影响函数体外的变量。这个sample是我在Fowler的Refactor一书里看到的，当时就写了个例子验证，果然。惭愧，写了这么多年程序，这个问题居然到今天才发现。</font></p>
</p>
</div>
{% endraw %}
<!--more-->
