---
layout: post
title: "Mobile Sametime 7.5"
date: 2006-10-31 22:41:31 +0800
permalink: /20061031/mobile-sametime-wm5.html
wp_id: 546
wp_slug: "mobile-sametime-wm5"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>继Sametime 7.5发表后，Mobile Sametime于昨天正式release，新版的移动Sametime可以在BlackBerry，Nokia和Windows Mobile设备上运行。我下载了一份Mobile Sametime for Windows Mobile 5.0 VGA版，装在了我的PDA上。</p>
<p>与Sametime桌面版不同，移动版本并没有使用基于Eclipse RCP/eRCP的架构，而是使用了标准的J2ME类库，所以不具备桌面版的插件扩展机制。考虑到移动设备的处理能力限制，这个设计并没有什么问题（用过<a href="http://www.skype.com/download/skype/mobile/">Mobile Skype</a>的大概都知道，这个native的WinCE程序速度有多么的慢）。</p>
<p>Mobile Sametime使用了J9 VM，携带了裁剪过的一些Java类库。连JRE带程序本身一共是2.5MB。下面是用<a href="http://www.microsoft.com/technet/prodtechnol/wce/downloads/ppctoys.mspx#ELD">Remote Display Control</a>抓的几张截屏（因为RDC没有针对WM5优化，分辨率较低。正好屏蔽掉敏感个人信息，哈哈）。</p>
<ul>
<li>登录Mobile Sametime 7.5</li>
</ul>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/10/mobile_sametime_1.jpg" /></p>
<ul>
<li>聊天窗口</li>
</ul>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/10/mobile_sametime_2.jpg" /></p>
<ul>
<li>Mobile Sametime安装文件和J9</li>
</ul>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/10/mobile_sametime_3.jpg" /></p>
<ul>
<li>产品信息</li>
</ul>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/10/mobile_sametime_4.jpg" />
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(5)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://http:octalxia.blogspot.com" rel="nofollow noopener">八爪</a></span><time class="comment-date">2006-11-01 19:39:55</time></div>
  <div class="comment-body"><p>Cool</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Terry</span><time class="comment-date">2006-11-01 20:47:27</time></div>
  <div class="comment-body"><p>估计是用cldc/midp写的，才能在nokia和blackberry上都能跑。没有用eRCP真是太明智了，看来ibm里面还是有些头脑清醒的人的。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://hzhfang.spaces.live.com" rel="nofollow noopener">爱拉芳</a></span><time class="comment-date">2006-11-01 22:12:59</time></div>
  <div class="comment-body"><p>唉，Sametime V7.5 windows版的都crash不知道多少次了，气的我只能用回NoteBuddy, 这么不稳定也敢release出来真是奇怪了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-12-07 22:34:09</time></div>
  <div class="comment-body"><p>IBM is announcing support for XMPP with the release of Sametime 7.5.<br>
http://www.marketwire.com/mw/release_html_b1?release_id=192209<br>
http://googleblog.blogspot.com/2006/12/chatting-with-lotus-sametime.html</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-12-10 11:01:11</time></div>
  <div class="comment-body"><p>昨天在Ed的blog上也看到了。</p></div>
</li>
</ol>
</section>
{% endraw %}
