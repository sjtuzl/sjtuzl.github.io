---
layout: post
title: "Make life easier: Mylar and Eclipse Spy"
date: 2006-11-06 22:45:07 +0800
permalink: /20061106/eclipse-user-interactive-study-spy.html
wp_id: 550
wp_slug: "eclipse-user-interactive-study-spy"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>Mylar和Eclipse Spy是为了解决不同问题而独立开发的两个插件，相同的是它们使用了类似的方法达到最终目的。</p>
<p><a href="http://www.eclipse.org/mylar/">Mylar</a>可以用作一个Eclipse平台上用户行为分析的工具，它可以将用户与Eclipse交互的过程记录下来，进而分析在一段交互过程中用户的访问习惯和潜在模式，从而为优化workspace设计提供依据。Mylar的输出文件包括了交互过程中调用过的插件信息。 <a href="http://www.cs.ubc.ca/~murphy/papers/mylar/software-eclipse-usage.pdf">这篇文章</a>介绍了用Mylar做用户使用习惯分析的过程。</p>
<p>虽然我没用过<a href="http://www.cumminsonline.com.ar/eclipse/eclipse-spy/index.htm">Eclipse Spy</a>，从它的文档可以看出它想到Eclipse plugin开发者的心坎儿里去了。该插件把用户的交互行为所产生的插件调用细节做实时的输出。想知道如何写一个refactoring wizard，只需要跑一个样例然后看spy的输出就知道哪些插件被使用到了，在什么方法上，ID是什么，然后到<a href="http://www.eclipse.org/newsgroups/">Eclipse newsgroup</a>上搜一下，开发效率大大提升。</p>
<p>无论产品还是开发工具，向用户隐藏一些细节是必要的；在用户真正需要细节的时候，可以高效、便捷的拿的出来也是很牛的本事。</p>
<p>从另一个角度看，API, 文档, sample project这些传统意义上提供的开发辅助资料，在系统变得日益复杂和庞大的时候（你几乎要成为一个哲学家才能在J2EE技术讨论会上插上话）显得粒度过细，要映射到用户要实现的实际问题，搭积木式搜索、组合、拼凑API显得过于耗时耗力。一些特殊的途径会显得与众不同，这些方法对快速解决问题颇有帮助，尤其是当你绝望的在搜索引擎结果里一页页点下去的时候。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(1)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">paulex</span><time class="comment-date">2006-11-08 07:42:19</time></div>
  <div class="comment-body"><p>似乎可以归结为那个老掉牙的数据和信息的区别问题，这些数据一直就在那里，对不需要的人是垃圾，对需要但是不能有效获取的人是可望不可及的奢求，对有心的人是客户价值...立刻就想起了Google的Adsense和分众的电梯广告，呵呵。最近在为一些测试/debug的事情心烦，平常看起来很烦的Excpetion stacktrace此刻显得非常不够用...要是我能方便的得到更多的JVM runtime信息该有多好啊...最绝的是，IBM JDI(J9)提供的-Xtrace选项，可以根据设置输出方法的log信息，满怀希望以为找到了自己要的东西，结果发现它输出的居然是对象的地址(就像这个Ljava/lang/String@12345678)，绝对正确又完全无用的IBM(微软)风格...对信息的暴殄天物令人发指...</p></div>
</li>
</ol>
</section>
{% endraw %}
