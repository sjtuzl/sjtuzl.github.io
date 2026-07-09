---
layout: post
title: "卸了Firebug"
date: 2009-07-10 23:09:28 +0800
permalink: /20090710/firebug-bug.html
wp_id: 755
wp_slug: "firebug-bug"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>在用Firebug测试HTTP conditional GET的时候，发现304和200的响应头交替出现，百思不得其解，以为是Firefox的缓存策略以及代码造成。结果在网上找到了这个：<a title="firebug bug" href="https://bugzilla.mozilla.org/show_bug.cgi?id=456996">https://bugzilla.mozilla.org/show_bug.cgi?id=456996</a></p>
<p>卸了Firebug，用Fiddler一测，连续304响应，一切正常。</p>
</div>
{% endraw %}
<!--more-->
