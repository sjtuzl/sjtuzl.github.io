---
layout: post
title: "最佳实践 － 从GB2312编码的WordPress博客系统升级到UTF-8编码"
date: 2006-12-06 22:24:10 +0800
permalink: /20061206/wordpress-upgrade-gb2312-utf-8.html
wp_id: 566
wp_slug: "wordpress-upgrade-gb2312-utf-8"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>本人博客网站在今年7月从blogchina移植到了租赁虚拟主机上的WordPress(WP)系统。在文章搬家的过程中，由于blogchina采用了GB2312编码，当时为了省事儿，直接写了程序自动导到WP上并把WP的缺省编码从UTF-8改成GB2312以正常显示中文字符，现在看来这个决定并不聪明。原因有3：</p>
<ul>
<li>由于GB2312页面无法混合显示多语言文字，在世界都开始变平的情况下，未能与世界接轨；</li>
</ul>
<ul>
<li>在非中文环境的操作系统中，如英文版Windows/Linux下，显示页面为乱码，而这些系统通常对Unicode字符都可以正常显示（需要相应字体）；</li>
</ul>
<ul>
<li>无法使用离线的blog软件，如<a href="http://www.zoundry.com/">Zoundry Blog Writer</a>，<a href="http://windowslivewriter.spaces.live.com/">Microsoft Live Writer</a>等，而目前现有离线blog软件支持GB2312的几乎没有。</li>
</ul>
<p>于是下决心把目前采用GB2312的”遗留系统“升级到UTF-8，并保持原有帖子正常读取、显示。 中间尝试过的方法、走过的弯路不必细说，今天该升级工作顺利完整，全部用户数据转成UTF-8，前台的PHP显示也完美支持。具体方法如下：</p>
<p><strong>1. 备份全部博客文章</strong></p>
<p>备份是所有系统升级前的必经之路，WordPress的备份功能好在不仅可以备份数据，它能连通DDL一起都保存在一个文件中，直接运行该文件中的SQL语句就能重新建表并导入数据。备份前必须前激活WP的备份插件，见图1：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/WP-backup-plugin.jpg" /><br />
<strong> 图1 激活WP备份插件</strong></p>
<p><strong>2. 文章备份</strong><br />
我3年多的帖子纯文字部分总共才1M多一点，用HTTP方式直接下载就可以了，下载后得到一个.gz的压缩包文件，内有.sql文件一个，见图2、3：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/save-blog-backup.jpg" /></p>
<p><strong>图2 保存备份文章</strong></p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/download-blog-archive.jpg" /></p>
<p><strong>图3 压缩的文章备份</strong></p>
<p><strong>3. 解压缩.sql文件并转码</strong></p>
<p>用支持编码转换的文本编辑器打开（我用的是UltraEdit），把该文件转换成UTF-8编码。在Ultraedit中的做法是选择File- >Conversions->ASCII to UTF-8 (Unicode Editing)，另存为。中文字符从GB2312转到UTF-8，存储由2个字节变成3个，所以文件将有所增大，见图4的比较（转换后的文件大了近 200KB)：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/file-size-compare.jpg" /></p>
<p><strong>图4 转码前、后备份文件大小比较</strong></p>
<p><strong>4. 修改备份文件建表语句中使用的缺省编码</strong></p>
<p>把SQL建表的default encoding，从"<strong>latin1</strong>"改成“<strong>utf8</strong>”，注意utf和8之间没有横杠。本人系统中共11张表，11个表定义全部修改替换，如图5：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/change-table-encoding.jpg" /></p>
<p><strong>图5 修改表定义缺省编码</strong></p>
<p>至此，数据准备工作完成。</p>
<p><strong>5. 删除老表</strong></p>
<p>登录到WP的数据库管理Web界面(http://mysql.yourname.com)，点击当前blog数据库显示属性，见图6：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/delete-tables.jpg" /></p>
<p><strong>图6 删除全部数据表</strong></p>
<p>依次删除全部11张表（点击红叉）。</p>
<p><strong>6. 更改数据库编码</strong></p>
<p>把当前数据库缺省的非UTF-8编码修改成"<strong>utf8_general_ci</strong>"，见图7：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/change-database-encoding.jpg" /></p>
<p><strong>图7 修改数据库编码方式</strong></p>
<p><strong>7. 执行修改后的SQL恢复数据</strong><br />
点击Web管理页面的"SQL" tab，从本地文本编辑器中copy整个备份文件并粘贴到SQL文本框内，点击Go执行SQL、导入数据。如果正确无误的话，会显示succesful。见图8：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/run-sql.jpg" /></p>
<p><strong>图8 执行SQL重新建表恢复数据</strong></p>
<p><strong>8. 修改WP系统中的wp-db.php文件</strong></p>
<p>在wp-db.php文件里，数据库建立连接的代码行后加入“<em>mysql_query("SET NAMES utf8");</em>”，这个重要环节的贡献源自<a href="http://wordpress.org/support/topic/77286">此文</a>。见图9：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2006/12/db-connection.jpg" /></p>
<p><strong>图9 修改访问数据库的编码形式</strong></p>
<p><strong>9. 修改WP的缺省locale</strong></p>
<p>OK，整个编码转换过程基本完成。重新登录系统（会发现表示乱码的"???"问号，不用管它），在"<strong>Options</strong>"->"<strong>Reading</strong>"选项中把原来的"GB2312"改成"UTF-8"，保存、属性，所有???问号字符变成正常的中文字符。</p>
<p><strong>10. 收尾</strong></p>
<p>如果对WP的header，sidebar等theme文件做过定制，进入相应管理选项手工删除其中的乱码文字，重新输入。至此，采用GB2312编码的WordPress系统顺利升级成UTF-8。
</p>
<p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(13)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-12-07 10:52:12</time></div>
  <div class="comment-body"><p>两点感受：<br>
第一，估计这篇帖子以后会跟你以前写的CS系博士毕业指南一样成为经常被搜到和引用到的帖子之一。<br>
第二，博主用的上述软件和系统中，貌似Winzip和UltraEdit有D版的嫌疑，呵呵，其他都是open source或者free software了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-12-07 12:26:50</time></div>
  <div class="comment-body"><p>都是正版的。因为这两个产品不是免费升级，所以一直用的低版本。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-12-07 12:30:08</time></div>
  <div class="comment-body"><p>其实我还真想过截屏用7-zip和VIM，不过何必要欺骗自己呢，这两个软件的确是平时频繁使用的。我很喜欢open source，但不歧视商业软件。</p>
<p>世界变了，当你用commerical software的时候，大家已经开始怀疑你的integrity了，呵呵。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-12-07 13:38:44</time></div>
  <div class="comment-body"><p>呵呵，是我心理阴暗，博主integrity木有问题，呵呵</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.javatag.com" rel="nofollow noopener">woyaokan</a></span><time class="comment-date">2007-01-22 02:34:05</time></div>
  <div class="comment-body"><p>PHP测试题<br>
   http://www.zymose.com/kaoshi/kaoti.php</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">美好时光</span><time class="comment-date">2007-02-22 21:17:05</time></div>
  <div class="comment-body"><p>文章写得干净利落，本人近来正在为转移数据库之事大感头痛。明白了，终究是水平问题...</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.hiceon.com" rel="nofollow noopener">Pisoul</a></span><time class="comment-date">2007-08-12 05:32:09</time></div>
  <div class="comment-body"><p>博主,我现在遇到的问题比较头疼.</p>
<p>正常进入后台发布,阅读是正常显示的UTF-8<br>
但是使用Windows Live Writer 发布`本地测试可以`但是在虚拟主机上就全部显示???了...</p>
<p>编码选择已经全部utf-8`数据库也整理了.还是不行.<br>
请指教</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-08-12 21:26:41</time></div>
  <div class="comment-body"><p>楼上的问题似乎是Webogger API的问题。一般情况下的Blog Client都是支持UTF-8的内容发布（而且基本上是只支持这一种）。你换其他的Blog client试过吗，比如Zoundry.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://peiqingxin.cn" rel="nofollow noopener">裴庆新</a></span><time class="comment-date">2007-11-26 01:38:06</time></div>
  <div class="comment-body"><p>请教你一个问题，是这样的，我的WP编辑器不知道怎么总是不正常显示，别人说不是副广本格式。我也找了问题但就是解决不了。请问我该怎么办？谢谢！</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-11-29 22:57:11</time></div>
  <div class="comment-body"><p>什么是副广本格式？RTE （Rich Text Editor）？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://blogpictorial.com" rel="nofollow noopener">裴庆新</a></span><time class="comment-date">2007-12-10 15:33:16</time></div>
  <div class="comment-body"><p>可以搞定了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">double</span><time class="comment-date">2008-01-03 14:44:04</time></div>
  <div class="comment-body"><p>我将我的mysql数据库中数据转化成utf8时用斑竹的方法就不行，转化完了之后另存了文件还是老样子，不知道为什么，而且mysql用ems管理时要如何把已有的数据库删除，在重新导入时不会出现数据库或表已存在的提示？我的一些代码如下：<br>
SET FOREIGN_KEY_CHECKS=0;</p>
<p>CREATE DATABASE `bugfree10`<br>
    CHARACTER SET 'gb2312'<br>
    COLLATE 'gb2312_chinese_ci';</p>
<p>USE `bugfree10`;</p>
<p>#<br>
# Structure for the `bugfile` table : <br>
#</p>
<p>CREATE TABLE `bugfile` (<br>
  `FileID` int(10) unsigned NOT NULL auto_increment,<br>
  `BugID` mediumint(7) unsigned zerofill NOT NULL default '0000000',<br>
  `FileTitle` varchar(100) NOT NULL default '',<br>
  `FileName` varchar(50) NOT NULL default '',<br>
  `FileType` varchar(10) NOT NULL default '',<br>
  `FileSize` varchar(20) NOT NULL default '',<br>
  `AddUser` varchar(30) NOT NULL default '',<br>
  `AddDate` datetime NOT NULL default '0000-00-00 00:00:00',<br>
  PRIMARY KEY  (`FileID`),<br>
  KEY `BugID` (`BugID`)<br>
) ENGINE=MyISAM DEFAULT CHARSET=gb2312;</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://5800.ac.cn" rel="nofollow noopener">5800</a></span><time class="comment-date">2009-04-28 18:27:16</time></div>
  <div class="comment-body"><p>可是现在没有gb2312版本的了</p></div>
</li>
</ol>
</section>
{% endraw %}
