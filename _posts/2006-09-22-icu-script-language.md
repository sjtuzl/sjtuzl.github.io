---
layout: post
title: "ICU4More"
date: 2006-09-22 22:36:18 +0800
permalink: /20060922/icu-script-language.html
wp_id: 505
wp_slug: "icu-script-language"
has_comments: true
---
{% raw %}
<div class="e-content">
<p><a href="http://www.ibm.com/software/globalization/icu ">ICU</a>是实现Unicode标准最好的开源类库（没有“之一”），目前有ICU4C和ICU4J两个主要版本。IBM作为ICU最重要的支持力量，为它多年的发展做了很大贡献。坦白说，在设计新的编程语言的时候，internationalization往往被放在相当次要的位置，被人忽略。即使像Ruby这种由日本人发明的语言，其国际化支持也十分有限（不得不承认，掌握、精通Unicode是很挑战的工作，而且需要相当的耐心与毅力）。</p>
<p>既然有了ICU这么好的实现，在为各类新兴语言打国际化补丁的时候自然成为最重要的参考，由此可以派生出ICU4A-Z来。</p>
<p>我在<a href="http://www.krugle.com/">Krugle</a>里输入"ICU" 查了一下，发现了针对Ruby和Python语言实现的ICU扩展：<a href="http://icu4r.rubyforge.org/">icu4r</a>和<a href="http://pyicu.osafoundation.org/">PyICU</a>。现在脚本语言这么多、这么热，新的ICU4?扩展随时可能出现。假如，我是说假如，JVM被越来越多的用来运行这些脚本语言，是不是有可能简化这样的扩展，充分利用JVM上可能提供的ICU服务做一层简化的映射层，实现脚本语言的globalization。当需要要添加新的脚本语言支持时，根据contract写一个特定的映射库放到JVM上跑就好了。不过说说简单，该怎么实现，没想过。</p>
<p>好消息是，更多的人开始重视国际化，这是新兴脚本语言的机会，也是ICU的机会。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(3)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2006-09-25 17:18:32</time></div>
  <div class="comment-body"><p>多希望有个ICU4Flash<br>
上礼拜拿到一些多语言支持的Defect，被迫自己在Flash里写DateFormat, NumberFormat.</p>
<p>一些脚本语言如Flash ActionScript,在其特定的虚拟机或运行环境中执行，很难与JVM通讯并leverage ICU4j之类的lib</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-09-25 17:43:16</time></div>
  <div class="comment-body"><p>就我知道的OpenLaszlo的i18n的支持也不好，它内嵌的JavaScript应该是要先翻译成ActionScript在编译成swf，所以问题的根儿在ActionScript上，Adobe需要一个lib做在Flash插件里（现在Flash应该仍不支持Bidi吧？）</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2006-09-25 20:09:26</time></div>
  <div class="comment-body"><p>不幸的是OpenLaszlo对i18n的支持比Flash还弱， 3.1.1后稍微好一点，不过外部数据还是必须用UTF-8编码。</p>
<p>这里其实问题有一堆:<br>
* 各国语言的文字是否可以在Flash中正确看到，包括静态和动态文本<br>
* 各个locale下，他们特定的数字和日期表示方式是否能很好的支持，比如德文中用点来隔开千位而用逗号来隔开小数 -____-!<br>
* 对BIDI之类的特殊语系，是否支持的特殊的布局方式，如文字从右向左输入，但遇到英文字符又从左向右。如何处理混合语言的换行。遇到水平菜单的展开方向，按钮对齐等都要反过来。</p>
<p>还好，据说BIDI里图形的表示方式还是从左向右的</p>
<p>Pure Flash ActionScript 1/2本身只支持英文格式的数字格式,所以需要自己实现各种格式的转化。Flex中有增强的lib对此支持好一些。不过说起BIDI文字，似乎Flash Player那层就不支持。确切地说动态文字不支持BIDI （不过静态的话何必用Flash呢...）<br>
http://www.quasimondo.com/archives/000217.php</p></div>
</li>
</ol>
</section>
{% endraw %}
