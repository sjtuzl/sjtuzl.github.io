---
layout: post
title: "关于借腹生子的再次思考"
date: 2006-08-04 00:30:57 +0800
permalink: /20060804/zhuxia-rss-self-contained-comments.html
wp_id: 472
wp_slug: "zhuxia-rss-self-contained-comments"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>前两天刚提到Kooxoo的比较购物把别人的数据库匿名搬了过来，提供增值服务。今天又读到关于抓虾新功能允许用户在抓虾自己的系统中写博客评论的<a href="http://iyee.cn/post/zhuaxia-will-decrese-readers.html">评论</a>，大致上是说抓虾把别人RSS的内容拿过来，却把评论功能搭在自己系统上，抢了原始作者的流量、广告、注意力。</p>
<p>我翻了一下以前写过的<a href="http://www.zhangling.org/blog/20060418/yiio.html">一篇帖子</a>，提到抓虾可能的评论功能，摘抄如下：</p>
<p>“<em>如果Blog和RSS的本质是这样的话，对每个blog的回帖按理说只要点击RSS客户端的“Reply All”就能实现，不需要重定向到源网页。现实可能是每个Blog系统处理用户登录和评论的方式都不太一样，API也没有统一规范，实现起来难度很大。我给抓虾贡献一个点子：在“我的频道”里面，在每条文章的底部加一个评论按钮，当用户点击的时候自动把对应的URL加载到一个弹出式iFrame中，让用户自己处理登录和留言（顾虑：对于内容的所有者来说，是不是显得有些霸道？？）。</em>”</p>
<p>今天抓虾实现的功能应该是进了一步，也是有争议的一步。</p>
<p>我稍微想了一下，这件事可以这么做个类比。开源软件的开发者在网上公布了自己的作品（写博客），供大家免费下载（发布RSS）。有人看到了这个软件，下载了，然后根据自己的要求修改了部分源码（写了评论）。于是问题变成了，外部用户改进的源代码是否应该贡献给原始作者，还是可以任意修改独立使用进而进行商业行为而不需要让作者知道（前者在作者博客网站写评论；后者在抓虾提供的评论系统里写评论）。问题的本质，似乎还是个license的问题。</p>
<p>开源软件的多样性，产生了很多的license，每种license都有自己的特点和适用范围。对于开源软件的消费者来说，对各种license是有不同偏好的，比如商业用户一般不喜欢GPL，因为传染性太强，等等。</p>
<p>现在的博客，内容上还不具备这么多可供操作的选项，从知识产权的角度看， 知识的自由表达形式所受到的内容控制和监管不如逻辑化的程序代码 － 程序可以直接作用产生一定后果，而知识的价值不是一个exe，它需要挖掘和分析。这么看来，抓虾是在这块领域内的吃螃蟹的人（螃蟹、虾都齐了），棍棒少吃不了。</p>
<p>如果在技术上不能实现原始系统评论和抓虾系统评论的整合（YR，看到了吧，业务搞大了就需要integration了，哈哈），是不是要extend <a href="http://blogs.law.harvard.edu/tech/rss">RSS的规范</a>，加入类似license的概念 － 我看是不需要的，做了再说，等着被“万人大签名”了 :)</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(3)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhuaxia.com/blog" rel="nofollow noopener">看到了吧</a></span><time class="comment-date">2006-08-04 09:01:24</time></div>
  <div class="comment-body"><p>张兄, 收到. 看把你给乐的, 呵呵. 那就来北京请你吃螃蟹和虾! :)</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">gaim</span><time class="comment-date">2006-08-04 09:42:59</time></div>
  <div class="comment-body"><p>更新的够快，gaim的源码研究过没？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-08-04 12:50:35</time></div>
  <div class="comment-body"><p>gaim的源码？gaim一直在用，可从没想看它的源码。</p></div>
</li>
</ol>
</section>
{% endraw %}
