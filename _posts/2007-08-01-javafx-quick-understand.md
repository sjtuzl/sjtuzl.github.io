---
layout: post
title: "JavaFX的愿景"
date: 2007-08-01 19:52:26 +0800
permalink: /20070801/javafx-quick-understand.html
wp_id: 682
wp_slug: "javafx-quick-understand"
has_comments: true
---
{% raw %}
<div class="e-content">
<p><a href="http://java.sun.com/javafx/">JavaFX</a>，最简单的理解（本人理解）就是用脚本语言开发swing应用，部署在网络上，通过JNLP加载，最后用客户计算机上的<a href="http://java.sun.com/developer/technicalArticles/javase/consumerjre/">Consumer JRE</a>运行该应用（或者是在移动设备上的JavaFX Mobile）。当然用JavaFX开发普通桌面应用也可以。</p>
<p>用脚本语言写UI早已不是新东西了，不过JavaFX的.fx文件到字节码的<a href="https://openjfx-compiler.dev.java.net/">编译器</a>似乎是给进阶人士的选配（除了可以脱离JavaFX runtime外，没有想到其他的value add）。在不使用JavaFX编译器的情况下，.fx文件在运行时被加载、解释、执行。</p>
<p>如果JavaFX利用网络发布的话，我希望有这样一个功能，即用户通过HTTP访问一个.fx文件，可以在服务器端生成一个可以执行的应用（applet, JNLP包裹的jar file, etc)并立即在客户端显示出来。这个功能在Openlaszlo里面有很好的实现，它可以在server端动态的编译.lzx文件并生成一个Flash文件（.swf格式），并且此flash可以离线播放。这个转变实际是以用户界面为中心的设计：窗体，而不是main class，将作为交互式应用程序的入口点。</p>
<p>把用户搞的很累的Java applet在浏览器兼容性、安全设置、签名、证书等问题上阻止了applet被广泛的采纳成为Web交互应用的标准。JavaFX能否打赢这个翻身仗，似乎不在JavaFX script language，而是那个consumer JRE。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(3)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://blog.csdn.net/paulex" rel="nofollow noopener">paulex</a></span><time class="comment-date">2007-08-02 00:19:56</time></div>
  <div class="comment-body"><p>我最直观的印象是，它网站上那几个demo我第一次尝试都没run起来，从此就没试第二次。而silverlight的都run的很好....我觉得问题不仅仅是JRE, 至少还有IDE。</p>
<p>JavaFX编译到字节码，也许只是为了赶现在多语言运行时的时髦吧，呵呵。</p>
<p>关于.fx文件通过网络发布，我没去看JavaFX现在怎么做的，难道.fx文件不能脱离浏览器单独在javaFX runtime上离线运行？为啥还要转化成另外一种形式？Mozilla的XUL就可以既在服务器端又可以在客户端运行，只要有个Gecko就可以了。</p>
<p>还有， 相比PC市场，JavaME在手机的普及率还是压倒性的，从市场角度我觉得把力气花在这上面翻本的可能性更大些。看起来至少Sun的CTO也是这么想: http://www.infoq.com/cn/news/2007/05/javafx-brewin</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://blog.csdn.net/paulex" rel="nofollow noopener">paulex</a></span><time class="comment-date">2007-08-02 00:32:10</time></div>
  <div class="comment-body"><p>还有一点，他们为了实现一个并非很新的技术又搞出一门脚本语言来...绕过了JCP和作为JSR之一的groovy，尽管是开源的，却又一次破坏了Java的游戏规则，也许他们并不在乎JCP渐渐边缘化...如果他们都不在乎，谁在乎呢？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-08-02 08:31:58</time></div>
  <div class="comment-body"><p>.fx目前需要被package到jar中，通过WebStart下载jar再运行。对用户来说，单独的.fx是被完全封装的，对外暴露的是由一个main class。</p></div>
</li>
</ol>
</section>
{% endraw %}
