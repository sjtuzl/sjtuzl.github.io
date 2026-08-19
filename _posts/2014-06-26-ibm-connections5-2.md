---
layout: post
title: "IBM Connections5.0新功能介绍(2) – 社区"
date: 2014-06-26 17:20:48 +0800
permalink: /20140626/ibm-connections5-2.html
wp_id: 971
wp_slug: "ibm-connections5-2"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>与Connections 4.5相比，5.0中社区(Communities)在管理和可用性方面有了很多提升，一一道来。</p>
<p><strong>1. 社区搬家</strong></p>
<p>这个功能是很多客户需要的，在内部我们也听到了相同的反馈。用户需要把一个社区放在另外一个社区下成为子社区，或者把已有的子社区升级为父社区。5.0中社区搬家功能可以允许用户自由移动子、父社区。不过该功能并没有在Web界面上提供（计划中），管理员可以公共社区的MBean命令行通过指定源、目标社区 uuid来实现搬家。搬家后Connections会根据原先和现在的社区权限和成员进行自动数据合并。</p>
<p><strong>2. 社区回收站</strong></p>
<p>在5.0之前，删除社区就意味着社区下的数据被物理删除，无法恢复。5.0中引入的回收站的功能，被删除的社区首先被放在回收站中，社区管理员可以在指定时间内恢复。被软删除的社区无法被用户访问到，社区内包含的应用数据如博客、活动、wikis等数据也被隐身禁止访问。</p>
<p><strong>3. 社区缺省应用</strong></p>
<p>如果社区内某应用是绝大多数社区用户一进来就会使用的功能，可以把它定义为缺省应用，这样在社区列表中点击一个社区链接的时候，被直接被定向到该社区应用了，导航被简化了。</p>
<p><a href="/assets/media/uploads/2014/06/comm_starter.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-972" title="comm_starter" src="/assets/media/uploads/2014/06/comm_starter.png" alt="" width="649" height="265" /></a></p>
<p><strong>4. 一键加入子社区和其父社区</strong></p>
<p>在5.0中，当加入一个公共子社区的时候可以同时加入父社区，而之前必须先加入父社区，然后才能加入其子社区。</p>
<p><strong>5. 外部社区</strong></p>
<p>在上篇文章提到过employee.extended角色可以创建外部社区并邀请外部用户成为社区成员。</p>
<p><a href="/assets/media/uploads/2014/06/external-comm.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-974" title="external-comm" src="/assets/media/uploads/2014/06/external-comm.png" alt="" width="665" height="256" /></a><strong></strong></p>
<p><strong>6. 社区新应用 - Gallery和Survey</strong></p>
<p>Gallery取代了之前版本的Media Gallery（仍可以使用），虽然都是用Files作为后台文件存储和管理但用户体验不同。现在可以把一个folder当做一个gallery的目录，支持图片、视频的预览和播放，如果安装了IBM Docs Viewer还可以预览MS Office/OpenOffice文件。Survey的后台是IBM Forms，安装配置好后可以在社区内提供投票功能。有关IBM Forms的安装配置，可以在IBM Connections5.0在线文档中找到。</p>
<p><a href="/assets/media/uploads/2014/06/comm-apps.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-976" title="comm-apps" src="/assets/media/uploads/2014/06/comm-apps.png" alt="" width="742" height="274" /></a></p>
</div>
{% endraw %}
<!--more-->
