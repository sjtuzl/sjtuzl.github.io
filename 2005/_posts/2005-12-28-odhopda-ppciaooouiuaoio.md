---
layout: post
title: "有关PDA (PPC)五种\"关机\"状态的分析"
date: 2005-12-28 14:32:00 +0800
permalink: /20051228/odhopda-ppciaooouiuaoio.html
wp_id: 300
wp_slug: "odhopda-ppciaooouiuaoio"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>此原创贴发在bbs.pdafans.com论坛：</p>
<p><a href="http://bbs.pdafans.com/viewthread.php?tid=158465&extra=page%3D1">http://bbs.pdafans.com/viewthread.php?tid=158465&extra=page%3D1</a></p>
<p><span style="FONT-SIZE: 12px">由于WM5.0的引入，使PDA关机问题变得更复杂。下面是我分析的五种关机状态，欢迎指正：</p>
<p>1. 常按开关3秒钟（适用于大多数PDA），此时屏幕变暗，电源消耗降低。此状态为五种"关机"状态电能消耗最高的一种；</p>
<p>2. 当还有应用程序运行时，按开关关闭机器。此时屏幕显示关闭，但RAM/ROM中数据均保存，运行中的程序继续保持状态。此为挂起状态，电源消耗仅次于1；</p>
<p>3. 人工杀死运行的所有程序，按开关关闭机器。此时屏幕显示关闭，RAM中的数据仅剩安装的应用程序（WM5.0之前）和操作系统占用的临时空间。此为挂起状态，电源消耗仅用来维护RAM中安装的应用程序（WM5.0之前版本,WM5.0则电能用来维护RAM中的临时变量）。对于PPC 2002/2003，这是最标准的关机状态；</p>
<p>4.软关机（对WM5.0之前的系统来说称为硬关机）。此状态下RAM中数据全部清空，操作系统未启动。对PPC 2002/2003来说，这种状态只会在电池完全耗尽或者电池被拔掉的情况下发生。对WM5.0来说，"软关机"不会删除安装的应用程序因为WM5.0会把程序自动安装在ROM，不再对RAM做分割。对WM5来说，这是最标准的关机状态；</p>
<p>5. WM5.0系统的硬关机。Dell X51V在同时按开关并用指点笔按reset按钮时，系统同时清空RAM和ROM。安装的应用程序全部消失，仅剩原始的操作系统。这种状态即使在电池完全耗尽或者被拔掉的状态下也不会发生，完全靠硬件实现。</span></p>
<p><span style="FONT-SIZE: 12px"><span style="FONT-SIZE: 12px">&nbsp;请问目前市面上的哪款关机软件可以支持上述各种关机状态？</span></span></p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(1)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.up2ugg.com" rel="nofollow noopener">uggs</a></span><time class="comment-date">2009-05-11 20:08:09</time></div>
  <div class="comment-body"><p>这是什么东东是程序的问题吗？</p></div>
</li>
</ol>
</section>
{% endraw %}
