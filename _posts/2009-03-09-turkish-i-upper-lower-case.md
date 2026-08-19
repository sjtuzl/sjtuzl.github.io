---
layout: post
title: "Turkish-i"
date: 2009-03-09 22:23:47 +0800
permalink: /20090309/turkish-i-upper-lower-case.html
wp_id: 736
wp_slug: "turkish-i-upper-lower-case"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>土耳其语的字符i有四种形式：i, I, ı 和 İ。 如果使用Java语言进行这四个字符间大小写的转换，会有意想不到的结果（见下图）。</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2009/03/turkish-i.PNG" /></p>
<p>在土耳其locale下，进行字字符i的大小写转换，可以看到潜在的危险：想像一下如果字符i(I)出现在文件路径、HTML标签、电子邮件地址、URL等，那么转换后将导致严重的问题。一个没有在设置了土耳其locale的操作系统环境下进行过GVT(Globalization Verification Test)的软件，暴露出此类问题的可能性相当之大。</p>
<p>因此，在我们处理土耳其i的大小写时，需要区分字符使用的上下文环境：如果使用在用户不可见的系统相关的地方，如上述几个例子，那么在做大小写转换的时候必须使用英文的locale；如果字符出现的用户界面上且和土耳其locale相关，则需要使用土耳其locale进行转换。不过在有些情况下，如何选择转换方案并非如此容易，甚至是无法事先预测的。个人认为，处于安全的考虑，在无法正确判断上下文的情况下，可以使用英文locale来进行处理，在进行GVT或者TVT的时候如果发现存在问题，则case by case的来解决。</p>
</div>
{% endraw %}
<!--more-->
