---
layout: post
title: "谁能重现这个bug？"
date: 2009-12-22 21:42:06 +0800
permalink: /20091222/firefox-location-bar-bug.html
wp_id: 802
wp_slug: "firefox-location-bar-bug"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>FireFox 3.5.6 (其实任何的3.5.x都有问题）：在”Tools-&gt;Options-&gt;Privacy"中设定了地址栏自动提示只显示历史，但在实际输入的URL时如果和书签中某个地址相匹配，该书签也会被显示出来。</p>
<p>我机器上的FF3.5从最早的版本到现在一直可以稳定重现这个问题。有人给Firefox开了个<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=527311">defect</a>我昨天才看到，但developer还是无法重现，却在FF 3.6B4里fix了这个问题。该Bug似乎只有在满足特定条件的时候才会出现，一旦出现后就可以稳定重现。</p>
<p><a href="/assets/media/uploads/2009/12/FF_bug.PNG"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-803" title="FF_bug" src="/assets/media/uploads/2009/12/FF_bug.PNG" alt="FF_bug" width="508" height="152" /></a></p>
</div>
{% endraw %}
<!--more-->
