---
layout: post
title: "电台DJ的传值与传引用"
date: 2006-06-29 16:35:00 +0800
permalink: /20060629/ucidjuaouoeoyoa.html
wp_id: 445
wp_slug: "ucidjuaouoeoyoa"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>105.7交通台晚上7点钟有档节目叫“<a href="http://www.smg.cn/root/radio/traffic/trafficjiemu.htm">淳子咖啡馆</a>”，每期都有个主题，淳子在伤感怀旧一番后放一首歌，叙述一段后继续放歌。我平时能在下班的公交车上听完这个节目的上半部分。</p>
<p>今天晚上听歌的时候忽然想到一个技术问题：这些直播或者非直播的音乐节目中，往往要完整的播上几首歌曲，这些节目的录音资料是仅包含主持人说话的部分呢，还是连这些完整播放的歌曲一起被重新录制进去了。比如一个小时的“咖啡馆”，主持人说话的时间加起来可能只有20分钟，剩下40分钟全是歌曲，这个1小时的节目最后存档或者未来重播的时候是保存了完整的1小时资料，还是仅仅保存主持人的部分，在重新播放的时候由电台调度当场从曲库中找歌来播。</p>
<p>这是个有关存储空间与执行效率的问题，就是by reference和by value的区别。如果是by value，每首被播出的歌会无数次的被复制到各个音乐节目声音资料中，浪费了大量的存储资源（经典热门歌曲可能被复制到成百上千卷的磁带中）；如果用by reference，虽然节省了存储空间，但在重播的时候需要有人在主持人话音结束的时候找到CD，定位track，再播放，太复杂了。不用说，电台一定用的是by value的做法，一来容量不是问题，二来资料的整理存档很容易。这好比做一个网页，要链接别人的一段内容，假如仅嵌入一个超链接的话，很难保证这个超链接未来还是否继续有效，与其这样不如copy & paste到自己的页面里，完全脱钩的自主管理和维护。</p>
<p>另外一个引起思考的问题是DJ们如何快速找到CD曲目（尤其是在直播节目中），电台内部是不是有一个可以直接供DJ使用的搜索引擎，根据歌手名、年代、曲名、歌词等搜索？？我不知道。昨天中央5套“豪门盛宴”里张路介绍了一个点球技法 － “勺子球”，让我觉得更加有趣：体育部的人如何在这么短的时间内找到了这么多“勺子球”的录像（大概有10个左右），这些录像有的来自联赛，有的来自世界杯，而且不少都上了年头。这些视频资料在电视台是如何管理、分类、标签、检索的呢？可以想到的是给每场球赛加多角度的分类，然后加入一些tag，如“乌龙球”、“误判”等供方便日后检索，但像“勺子球”这样的关键词也会被资料管理员们tagging吗？我很怀疑，难道是全靠懂球的人回忆起来的，没太可能。。。。我猜Web 2.0这些东西，放到中央台估计会被仓库管理员鄙视的。。。</p>
<p><a href="http://www.fengdingcn.org/">Ding Feng</a>曾经研究过<a href="http://dublincore.org/">Dublin Core</a>在图书馆学中的应用，现在看至少在视频的metadata标注上还是太粗粒度了。对于球赛来说，要不就把比赛解说词用语音识别转换成文字，然后把这些文字连同录像一起保存归档，文字部分供搜索之用（以后在引用06年意大利vs澳大利亚的录像资料时，只需要输入“灵魂附体”就可以了）。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">paulex</span><time class="comment-date">2006-07-20 00:28:45</time></div>
  <div class="comment-body"><p>现在好像有些旋律搜之类的技术,不知道到了什么程度. 没有web2.0众人拾柴火焰高的无偿过滤tag多半是没有什么作用的。在计算能力和算法强大到语音可以索引和匹配之前，转换成文字倒是一个办法。视频呢？能不能抽象成矢量图然后再转化成xml作为索引？</p>
<p>至于电视台，我觉得不要对它的IT技术抱太大希望，隔行如隔山，按照我对电视台的粗浅认识(曾经参观过上海数字电视的工作室，他们十几个人负责几十个频道的节目编排)，这些事情就是靠人做的。回忆10个勺子球并不困难，我这样的伪球迷都能立刻说出来3个，有些bbs上的数据库型球迷可以回忆出大概10年以前一场普通联赛的比分，进球者，和怎么进的，另外一些游戏型球迷可以瞬间说出某中游球队主力球员在足球游戏里的指数，这还都是业余的。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-07-20 08:34:08</time></div>
  <div class="comment-body"><p>上海交大图书馆以前是搞过音乐搜索的，就是用匹配声音的办法。</p></div>
</li>
</ol>
</section>
{% endraw %}
