---
layout: post
title: "我对code review的几点理解"
date: 2006-09-19 21:21:43 +0800
permalink: /20060919/code-review-static-analysis.html
wp_id: 504
wp_slug: "code-review-static-analysis"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>Code Review就是通过审查代码，发现代码中可能存在的问题并给予纠正，这些问题可能包括设计上的、实现上的或者编程风格等多方面。目前做code review一是靠人读代码，二是借助于一些工具。人工阅读效率慢，但有深度，可以解决设计上的问题；工具利用模式匹配做静态分析找到不合适函数调用，速度快但缺乏context无法进行深层分析。目前Rational的“Code Review"插件提供了上百条规则对Java代码进行分析。</p>
<p>有关人工review和机器review的关系，可以讨论好几天。两者相同之处都是发现问题，不同之处是人工review侧重内在逻辑和实现方法，避免框架性质的错误（宏观＋部分微观）；机器review关注细节、可重现，对于典型错误的处理很有帮助（微观）。</p>
<p>我喜欢用现实生活的例子来解释技术，尤其是在从去年build了装修的domain knowledge后。基本上可以说，人工review好比房屋设计、机器review好比选材。选材很重要，装修过的人都知道开关选“西蒙”、“梅兰日兰”，水管选“皮尔萨”、龙头选“高仪”，水槽选“皇冠”、“弗兰卡”、水泥选“象"牌、电线选“熊猫“、刷子选“大师”...“没有好材，再好的戏也出不来”。选材容易之处在于从不知道变成知道门槛很低，久而久之就会慢慢熟起来，变得有经验，象我现在这样。设计则不然，就是同一套房子，两次设计也是会有差别，而且没法定量评价 - 人对美与和谐的追求无止境。出好的设计需要时间和经验磨练，与之相关的知识的传递比起checklist形式的静态分析规则更难。同样，没有好的设计（譬如在马桶对面的墙上镶一面镜子会怎么样？这是装修里常见的一个bad practice），再好的材料堆砌在一起也是无用的。</p>
<p>没有经过静态分析的程序可能跑起来不错，而实际上可能像一块奶酪一样，满身是漏洞，问题一出现就很严重而且直接面对问题的是可能是最终用户；没有经过人工review的代码跑起来也可能不错，只是潜在的问题，如性能、扩展性能会在需求变更的时候显现出来，直接面对麻烦的可能是程序员。</p>
<p>上周面试实习生的时候，我问了一个问题，.NET平台上存在多种语言，如果你来设计一个静态分析工具的话，该怎么做，需要考虑哪些因素？（参考：<a href="http://www.gotdotnet.com/team/FxCop/">FxCop</a>） 其实现在的Java也开始支持其他脚本语言，为了适应JVM之上的多种语言，未来基于Java平台的代码分析工具也会从源代码转向bytecode的分析，那是JVM唯一能听懂的语言。
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
  <div class="comment-meta"><span class="comment-author">Sean</span><time class="comment-date">2006-09-20 23:42:22</time></div>
  <div class="comment-body"><p>sun刚把jruby的负责人招安了。<br>
看来现在.net相对java在支持多语言有先天的优势。<br>
踏着前人的尸体前行？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Suxer</span><time class="comment-date">2009-05-21 10:32:12</time></div>
  <div class="comment-body"><p>项目做完了，最近正要对项目做codereview。希望给些建议～</p></div>
</li>
</ol>
</section>
{% endraw %}
