---
layout: post
title: "IBM Connections5.0新功能介绍(3) – @功能"
date: 2014-06-27 17:24:22 +0800
permalink: /20140627/ibm-connections5-mention.html
wp_id: 989
wp_slug: "ibm-connections5-mention"
has_comments: false
---
{% raw %}
<div class="e-content">
<p><strong>@功能</strong>在微博、微信中已经广为人知。Connections 4.5的CR2版本中提供了Connections个人微博和社区微博的@功能，该功能也已经在去年的<a href="http://apps.na.collabserv.com">Connections公有云版本</a>中上线。在5.0中，@功能被添加到了博客正文和评论、Wikis正文和评论、Files的评论、论坛的帖子和评论、活动的帖子、回复和待办、社区日程的正文和评论中，更大的提升了用户和Connections系统的联动。</p>
<p><a href="/assets/media/uploads/2014/06/mention.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-991" title="mention" src="/assets/media/uploads/2014/06/mention.png" alt="" width="579" height="424" /></a></p>
<p>一个被@的用户会在Connections的首页的一个Tab里看到别人@他的内容，另外一旦被@会收到邮件通知（不希望邮件打扰的话可以自行关闭@的邮件通知功能）。</p>
<p>@功能看似简单，但我们在设计的时候必须根据Connections的实际考虑更多的问题。比如说我在论坛里@的一个人（对方收到通知），而之后我重新编辑了帖子，又@了另外一个人，这个时候系统该如何处理两个@，是否需要给之前被@的人再发一遍通知？如果要避免多次发送，势必要求在保存@信息的时候需要额外存储帖子内被@过的人员列表。另外，如果用户@一个对该内容没有访问权限的人该如何处理？在Rich Text Editor里@功能的用户体验是什么样的？Connections用户的唯一ID是directory uuid（不具可读性），如何在@的时候做到数据和显示的分离？这些问题在互联网微博上都不存在，可却很大的影响了Connections产品的设计。</p>
</div>
{% endraw %}
<!--more-->
