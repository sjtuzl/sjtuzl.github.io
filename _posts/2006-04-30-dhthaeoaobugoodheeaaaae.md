---
layout: post
title: "修复了这个bug后，有人流泪了"
date: 2006-04-30 09:40:00 +0800
permalink: /20060430/dhthaeoaobugoodheeaaaae.html
wp_id: 429
wp_slug: "dhthaeoaobugoodheeaaaae"
has_comments: false
---
{% raw %}
<div class="e-content">
<p><a href="http://www.javalobby.org/java/forums/t70864.html">楼主</a>为了Javadoc中的这个<a href="http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=5034036">bug</a>，受尽了煎熬(..had to reboot...)，每次看到到它一切立刻变的一团糟(...everything got messed up...)。两年后，Sun终于在Java 6中修复了这个bug。</p>
<p>啥也别说了。。。眼泪哗哗的。。。</p>
<p>附：</p>
<pre>EXPECTED VERSUS ACTUAL BEHAVIOR :<br />
EXPECTED -<br />
"Note: Disabling a component does not disable <strong><font color="#0000ff" size="2">its</font></strong> children."</p>
<p>ACTUAL -<br />
"Note: Disabling a component does not disable <strong><font color="#ff0000" size="3">it's</font></strong> children."<br />
(Incident Review ID: 254969) </pre>
</p>
</div>
{% endraw %}
<!--more-->
