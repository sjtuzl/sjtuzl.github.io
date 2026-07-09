---
layout: post
title: "YesScript - A Firefox extension to allow blocking JavaScript for web sites SELECTIVELY"
date: 2007-01-05 21:26:39 +0800
permalink: /20070105/yesscript-firefox-extension-block-javascript-selectively.html
wp_id: 597
wp_slug: "yesscript-firefox-extension-block-javascript-selectively"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>YesScript是我写的一个Firefox的扩展，允许用户有选择的屏蔽指定网站的JavaScript功能。虽然在Firefox选项对话框"Content"页面，用户通过选择"Enable  JavaScript"打开或关闭JavaScript功能，但这种改变是针对所有网站，而不能选择性的屏蔽。</p>
<p>写YesScript的主要动力来自使用Google时的不便 -  用Firefox在登录Google后进行搜索，在返回的结果页面中，如果点击某个搜索结果的链接，Google会先把请求发送给自己(收集用户的选择偏好)，然后再重定向到目的站点。由于在国内访问Google.com的不稳定性，常出现由于Google自身响应速度慢导致链接打开速度慢；实在慢的时候，我一般在搜索页面里面Copy  & Paste 搜索结果链接到另外一个tab窗口中打开，跳过Google的用户反馈收集 -  这些都是Google页面中的JavaScript代码造成的。</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/redirection1.png" /><br />
<strong>Fig.1 Redirect URLs</strong></p>
<p>好在<a href="http://kb.mozillazine.org/Allowing_only_certain_sites_to_use_JavaScript">Firefox提供了选择性过滤JavaScript的支持</a>，它同时提供了“白名单”和“黑名单”的功能，分别针对指定网址有选择的开放和关闭指定网站的JavaScript功能，但此功能并未开放给用户直接使用。<a href="http://www.noscript.net/">NoScript</a>是一个Firefox插件，它实现了JavaScript“白名单”功能，即仅允许某些网站开启JavaScript功能，其余全部禁止。有关“黑名单”的插件，我在Web上搜了一下，没找到，才决心自己写一个。为了和NoScript的名称相对应，这个插件叫做YesScript  :)</p>
<p><strong><span style="font-size: 1.5em; text-decoration: underline">功能</span></strong></p>
<p>YesScript是一个很简单的JavaScript“黑名单”插件，它的主要feature有：</p>
<ul>
<li>添加自定义“黑名单”，屏蔽名单中网站的JavaScript功能；</li>
<li>功能开关，允许打开或者关闭YesScript，以便需要时临时恢复或者关闭JavaScript屏蔽功能；</li>
<li>中、英文界面，根据Firefox语言版本自动切换。</li>
<li>部署了远程更新RDF文件，供Firefox自动发现YesScript新版本并升级。</li>
</ul>
<p>因为YesScript修改了Firefox的安全策略，所以任何改变，包括增加/删除黑名单上的站点；打开或者关闭YesScript都需要重启Firefox才能生效。</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/menu.png" /></p>
<p><strong>Fig.2 YesScript extension</strong></p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/option1.png" /><br />
<strong>Fig.3 Manage Blacklist</strong></p>
<p><strong><span style="font-size: 1.5em; text-decoration: underline">测试</span></strong></p>
<p>我在<strong>Window XP (Firefox 1.5, 2.0)</strong> 和<strong>Ubuntu 6.1.0  (Firefox 2.0)</strong>上对YesScript进行了测试，均可正常工作。</p>
<p>考虑到公司知识产权相关规章制度，YesScript无法放到公网上下载，目前仅能开放给内部员工使用。</p>
<p><strong>下载地址(IBM Internal)</strong>：<img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/down.png" /></p>
<p><a href="https://w3.webahead.ibm.com/w3ki/download/attachments/312870/yesscript.xpi"><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/yesscript32.png" />YesScript  Extension Installation</a></p>
<p>如有bug或者建议，可直接发mail找我 :)
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">dada</span><time class="comment-date">2007-01-05 23:13:03</time></div>
  <div class="comment-body"><p>眼谗,我只有on borad之后才能下载了:)</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Michael</span><time class="comment-date">2007-01-06 01:45:33</time></div>
  <div class="comment-body"><p>哈哈 我也眼馋 我mail是groundzyy◎gmail.com</p>
<p>Thx ：）</p></div>
</li>
</ol>
</section>
{% endraw %}
