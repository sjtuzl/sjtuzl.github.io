---
layout: post
title: "折腾人的.flv视频"
date: 2006-07-15 21:10:02 +0800
permalink: /20060715/ie-flv-video-download.html
wp_id: 457
wp_slug: "ie-flv-video-download"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>近期.flv格式的视频文件忽然多了起来，热门视频分享网站<a href="http://www.6rooms.com">6rooms</a>，<a href="http://www.youtube.com">youtube</a>和<a href="http://video.google.com">Google video</a>等都在使用这种格式提供在线视频播放服务。我没看出.flv有特别多的优点，对播客网站来说就是增加了用户下载的难度，把老百姓之间的私下共享尽早的扼杀在摇篮中。</p>
<p>前两天为了从Google Video下载一个"<a href="http://video.google.com/videoplay?docid=-6459171443654125383&q=label%3Auser+interface">The Science and Art of User Experience at Google</a>"的视频，在研读了网上<a href="http://www.lifehack.org/articles/lifehack/how-to-download-google-video.html">最佳实践</a>后折腾了半天才当下来。即使下载到本地，因为.flv格式的文件无法拖放到浏览器内嵌的Flash Player播放，所以用户还必须下载Flv的播放器...</p>
<p>好了，是需要更简便方法的时候了。为了更多受众，还是分享一下在IE里下载在线播放.flv视频的下载方法。</p>
<p>1. 下载<a href="http://www.blunck.info/ieHTTPHeadersSetup.exe">ieHTTPHeaders软件</a>。这是一个IE插件，可以记录当前浏览器和服务器的全部对话内容。安装后，在IE“查看"->"浏览器栏"里可以看到"ieHTTPHeaders v1.6"的选项，选中后IE底部出现监控窗口；</p>
<p>2. 正常使用IE时，可以在下面窗口看到动态的HTTP request和response。一旦看到IE里.flv视频文件加载完成，就可以把监控窗口中的内容copy到记事本里然后搜索”.flv"就能找到这段视频文件真正的URL地址了（需要和当前浏览器URL地址拼接成绝对URL地址）。</p>
<p>下图是IE在播放6rooms里“<a href="http://www.6rooms.com/watch.php?v=22356">中国队勇夺世界杯冠军</a>”.flv视频时捕获到的URL地址：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/07/ie-flv-download.jpg" />
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(7)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-07-15 22:36:52</time></div>
  <div class="comment-body"><p>靠，这过程太geek了，绝对只适合geek使用，普通用户没法适用。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">boo</span><time class="comment-date">2006-07-16 10:23:44</time></div>
  <div class="comment-body"><p>那就用这个吧：http://www.videodl.org/</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.littlerain.net" rel="nofollow noopener">Liu Yan</a></span><time class="comment-date">2006-07-16 16:54:52</time></div>
  <div class="comment-body"><p>还是httpwatch好用。<br>
另：在杨普的blog上看到你说疯狂的石头的bt没有。在bt.ydy.com上可以找的，昨天刚下来。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-07-16 19:44:07</time></div>
  <div class="comment-body"><p>httpwatch是商业软件要200多美金，用不起啊。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.hitren.com/blog/more.asp?name=candyfloss" rel="nofollow noopener">Candyflos</a></span><time class="comment-date">2006-08-20 16:43:08</time></div>
  <div class="comment-body"><p>也不是没有办法找（下）到.flv文件，到我的blog看看，绝对惊喜<br>
http://www.hitren.com/blog/more.asp?name=candyfloss&amp;amp;id=13684</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-08-20 17:39:21</time></div>
  <div class="comment-body"><p>看了。不过这种方法对Firefox无效</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2006-08-21 12:27:54</time></div>
  <div class="comment-body"><p>好像有不少人写过自己的FLV Player, 用起来就像mpc一样</p>
<p>虽然Flash有自己的Media Server，支持流媒体,cache,流量控制等<br>
但FLV还是用的很多，相比直接把视频转成SWF，FLV不受帧数的限制，可以有自己的FPS，更好支持压缩和预加载...</p>
<p>好东西就留在网上吧，不见得都要载下来。我在YouTube就收藏了很多滑板的视频，省了不少硬盘空间 :)</p></div>
</li>
</ol>
</section>
{% endraw %}
