---
layout: post
title: "Redbooks: WebSphere Application Server V6.1: Classloader Problem Determination"
date: 2007-07-24 22:04:33 +0800
permalink: /20070724/websphere-class-loading-redbook.html
wp_id: 680
wp_slug: "websphere-class-loading-redbook"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>这本昨天发布的<a href="http://www.redbooks.ibm.com/abstracts/redp4307.html">红皮书</a>在我最近的阅读列表中。Container环境下的classloading是无数诡异问题的根源。以Lotus Connections 1.0.1来说，我们用了<a href="http://www.icu-project.org/index.html">icu4j</a>来提供一个时区列表，icu4j本身自带了这些列表的翻译，比JRE自带的要全。但在测试的时候发现WAS 6.1.0.3下的时区列表繁体中文的显示有问题，混入了大量简体中文字符。其原因在于WAS自带了一份icu4j并且早于webapp下的lib被container加载，而这份icu4j自带的时区翻译存在问题。</p>
<p>对于长期从事WAS应用开发的IT工作者，这是本必读书。
</p>
</div>
{% endraw %}
<!--more-->
