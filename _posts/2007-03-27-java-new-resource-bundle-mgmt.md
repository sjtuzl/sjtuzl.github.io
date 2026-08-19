---
layout: post
title: "新式Java本地化资源管理"
date: 2007-03-27 12:30:33 +0800
permalink: /20070327/java-new-resource-bundle-mgmt.html
wp_id: 643
wp_slug: "java-new-resource-bundle-mgmt"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>John Conner服务于Sun公司，是Java globalization专家。如果在Google groups搜索一下的话，可以发现他解答Java i18n的帖子随处可见。</p>
<p>John的新文章<a href="http://www.joconner.com/2007/03/20/international-enhancements-in-java-se-6/">谈到了Java 6的国际化新功能</a>，和新的Java properties相关类的增加，如动态管理等。在Eclipse 3.1后，Eclipse推荐采用另外<a href="http://help.eclipse.org/help32/index.jsp?topic=/org.eclipse.platform.doc.isv/reference/misc/message_bundles.html">一种改良的properties文件加载方法</a>本地化资源文件，IBM Zurich实验室为Eclipse写了一个相应实现。</p>
<p>resource bundle, XML, XLIFF，satellite DLL (Win32)，本地化文件的格式在多元化，文件管理方式也在多元化。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(2)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">paulex</span><time class="comment-date">2007-03-27 17:44:27</time></div>
  <div class="comment-body"><p>Eclipse那个方法挺有趣，Harmony的邮件列表上讨论过这个方案，但是大多数人认同的观点是: 这种方法更适合GUI使用的资源文件，因为它们基本上需要一次性load出来，而对于其他的一些应用比如Harmony, 资源文件更多用于exception的信息，是on demand的load的，所以传统的ResourceBundle性能更好。</p>
<p>我在Eclipse那个方法的基础上有另外一个想法，就是利用Java 5 instrument的redefine class功能，将不同的本地化信息编译成同一个资源类的不同实现，如果指定了一个新的locale, 就将那个locale对应的类实现的字节码load进来，redefine成为资源类的当前实现。我记得我试过这种想法，是可行的，但是没有比较过与Eclipse的方法相比哪个性能更好。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2007-03-27 21:40:09</time></div>
  <div class="comment-body"><p>这种方法和Portal里的MessageCode类似, 至少两三年前的Portal5就是大量用这种方式<br>
当messageKey比较多时,一般需要用code generation工具根据Property文件生成Java文件 (我为此还写过一个eclipse plug-in)</p>
<p>想起来, 你看到DB2启动时控制台的那些文字, 基本上也应该是MessageCode<br>
最前面几个字符表示产品名和组件名, 然后是一个编号, 然后是一个字符表示Message级别, 最后是数字表示带多少参数</p>
<p>IBM向来喜欢这种笨重的解决方案</p></div>
</li>
</ol>
</section>
{% endraw %}
