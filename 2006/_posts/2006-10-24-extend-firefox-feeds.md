---
layout: post
title: "扩展Firefox 2.0的Feeds订阅功能"
date: 2006-10-24 23:38:14 +0800
permalink: /20061024/extend-firefox-feeds.html
wp_id: 539
wp_slug: "extend-firefox-feeds"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>今天安装了Firefox 2.0，总的来说不太满意，安装时自动覆盖了我自己做的searchplugin（后来从备份的1.5的安装目录下拷贝回那些.src文件，可以在2.0下正常工作），很多add-on也不能用了。很像Eclispe 2.x升级到3.x时的样子。</p>
<p>2.0增加了一个Feeds订阅的功能，不过除了Live bookmark和本地安装的RSS reader程序，网络订阅缺省只有bloglines，My Yahoo和Google Reader三种，而且没有提供用户自定义功能。</p>
<p>花了点时间hack了一下，把<strong>抓虾订阅</strong>加了进去，具体方法如下：</p>
<p>1.  找到安装目录下\chrome\en-US.jar文件（英文版Firefox），用WinZip打开，提取压缩包中文件：\locale\browser-region\region.properties；</p>
<p>2. 用文本编辑器打开region.properties文件，修改如下：</p>
<p># These are the default web service based feed readers<br />
browser.contentHandlers.types.0.title=Bloglines<br />
browser.contentHandlers.types.0.uri=http://www.bloglines.com/login?r=/sub/%s<br />
browser.contentHandlers.types.1.title=My Yahoo<br />
browser.contentHandlers.types.1.uri=http://add.my.yahoo.com/rss?url=%s<br />
browser.contentHandlers.types.2.title=Google Reader<br />
browser.contentHandlers.types.2.uri=http://fusion.google.com/add?feedurl=%s<br />
<em><strong>browser.contentHandlers.types.3.title=抓虾<br />
browser.contentHandlers.types.3.uri=<br />
http://www.zhuaxia.com/add_channel.php?url=%s</strong></em></p>
<p>3. 把修改后的region.properties文件重新打回到en-US.jar压缩包内，重启Firefox即可。如下图：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/10/firefox-feeds.jpg" /><br />
目前还没找到给新添加的在线订阅提供商分配图标的方法。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(9)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-10-24 23:48:05</time></div>
  <div class="comment-body"><p>hoho 告诉徐易容和谌振宇他们做个抓虾 plugin for firefox好了</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-10-25 00:03:47</time></div>
  <div class="comment-body"><p>看到另外一个办法：http://www.bloq.cn/user1/9359/archives/2006/firefox-feeds.html</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.laoxiong.cn" rel="nofollow noopener">老熊</a></span><time class="comment-date">2006-10-25 10:51:46</time></div>
  <div class="comment-body"><p>张领的办法还是程序员的思路，不如另外一个简单，嘿嘿</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-10-25 12:33:38</time></div>
  <div class="comment-body"><p>二楼的方法昨天写完后才看到。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">purefire</span><time class="comment-date">2006-10-25 18:09:17</time></div>
  <div class="comment-body"><p>firefox的扩展有点傻乎乎的，其实大多数的插件只要把安装的配置文件的最高版本号写成2，都能安装运行了，因为API基本还稳定的 ;)</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-10-25 18:22:33</time></div>
  <div class="comment-body"><p>原来是这样。这让我想起了office 97的安装过程，只要在命令行指定一个参数就能跳过软盘激活验证。还是很和谐的。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://http:octalxia.blogspot.com" rel="nofollow noopener">八爪</a></span><time class="comment-date">2006-10-25 20:27:25</time></div>
  <div class="comment-body"><p>没插件，不升级</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://octalxia.blogspot.com" rel="nofollow noopener">Sean</a></span><time class="comment-date">2006-10-29 23:14:54</time></div>
  <div class="comment-body"><p>原来一直用bloglines，操作很容易上手，但是界面是在不敢恭维。<br>
发现google reader改版后，和Bloglines差别不多，界面好看多了。<br>
白色还是很漂亮的，有点ipod的感觉。就换坑了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jove</span><time class="comment-date">2006-10-30 13:17:01</time></div>
  <div class="comment-body"><p>我原先一直用newsgator, 不过随着Google Reader的重大升级也"换坑"了。</p>
<p>最大的好处是在Google Reader可以很方便听podcast. 他遇到mp3等音频文件会显示一个Google的音乐播放器（Flash)，免去存mp3文件-&amp;gt;等下载完-&amp;gt;听完删除的麻烦。 他对YouTube的支持也很不错(废话，都是一家人乐)。可以在Reader中直接看video</p>
<p>另外，他的AJAX UI实在做的很赞，全键盘操作</p>
<p>另外，他会把一个feed中所有条目都保留在服务器。即使你刚开始订阅某人blog的rss/atom, Google Reader也可以把这个blog最初的文章找出来。</p></div>
</li>
</ol>
</section>
{% endraw %}
