---
layout: post
title: "实时视频(压缩)存储?"
date: 2006-10-23 23:14:48 +0800
permalink: /20061023/realtime-video-compress.html
wp_id: 537
wp_slug: "realtime-video-compress"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>这是看到CSDN这则“<a href="http://prj.csdn.net/projdetail.aspx?pointid=1225">监狱聊天系统</a>”招商项目的要求后想到的问题。视频聊天软件多如牛毛，但支持实时的视频存储的方案大概凤毛麟角。保存实时视频，有两个问题需解决：磁盘空间和CPU处理能力。如果不压缩，半个小时的聊天视频可能就需要几个GB的空间，这边犯人还在痛哭流涕的反省，那边磁盘空间不够了；如果用实时压缩的方案，可能一个定期执行的病毒扫描程序就能毁了整个记录过程，就像我刻录光盘一样，按下了“Burn”按钮，键盘、鼠标便都不敢轻举妄动了。</p>
<p>我没做过测试，不知道目前双核的CPU是不是可以很流畅的支持MPEG视频的实时压缩，同时留出足够的CPU时间完成其他任务；否则就要考虑带视频压缩的硬件视频采集卡的方案了。</p>
<p>其实IBM有个专门针对听力残疾人士设计的教学软件：老师带麦克风讲课，教室有摄像机，系统把语音信号经识别后转换成文字信息，最终软件生成整个讲课过程的电子讲义，通过<a href="http://www.w3.org/AudioVideo/">SMIL</a>集成视频、声音、自动识别的文字，在RealPlayer里回放。这套solution就是IBM <a href="http://www-306.ibm.com/able/solution_offerings/ViaScribe.html">ViaScribe</a>。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(4)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-10-24 00:29:42</time></div>
  <div class="comment-body"><p>我以前还真的和别人讨论过监狱聊天系统的项目，当时我一个朋友说是新疆什么监狱提出的需求，是犯人和希望远程就能探监的亲友之间通过互联网聊天，但干警要作为第三方能监视或必要情况下干预。光从技术层面考虑，似乎也不是很简单的。hoho</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.laoxiong.cn" rel="nofollow noopener">老熊</a></span><time class="comment-date">2006-10-25 10:06:43</time></div>
  <div class="comment-body"><p>恰好最近接触了视频监控等这样的项目，基本上，也就是硬件形式的会比较稳定可靠。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jet</span><time class="comment-date">2006-10-28 17:28:24</time></div>
  <div class="comment-body"><p>清晰度应该不是很高，我感觉应该跟十字路口的监控差不多。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vogel</span><time class="comment-date">2006-11-16 17:13:20</time></div>
  <div class="comment-body"><p>清晰度无法确定。跟压缩的比率以及算法有关。软件进行视觉（图音视）处理本身就有问题。做过测试，用Matlab来处理图片而已，就是一种漫长的等待。即使用效率最高的C来进行相应的处理，也不尽人意。</p></div>
</li>
</ol>
</section>
{% endraw %}
