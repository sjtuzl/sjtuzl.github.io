---
layout: post
title: "IBM Connections5.0新功能介绍(1) - 内、外部用户协作"
date: 2014-06-26 16:29:16 +0800
permalink: /20140626/ibm-connections5-1.html
wp_id: 957
wp_slug: "ibm-connections5-1"
has_comments: true
---
{% raw %}
<div class="e-content">
<p><strong>IBM Connections 5.0 - 内/外部协作</strong></p>
<p>Connections在应用部署场景上基本有两种。一是企业内部部署，供员工使用，另一种在公网部署，供网民使用 (如<a href="https://www.ibm.com/developerworks/community/groups/service/html/allcommunities">IBM developerWorks交流区</a>)，如果客户需要同时拥有两种协作模式并存的话，在5.0之前只能部署两套单独的环境。</p>
<p>在5.0中，我们增加了内、外部用户协作的功能，希望解决的应用场景是在单一部署下既允许员工内部正常的使用，又可以邀请外部用户登录和员工协作，如在社区共享信息、上传文件等。要解决的关键问题有两个：1) 为Connections用户添加角色以区分不同用户类型；2)保证外部用户在受限外网内工作，比如禁止查看共有信息（公共博客、社区、论坛...)、禁止搜索员工目录、限制社区管理权限等等。在5.0中我们引入了两类用户（内部用户和外部用户）和三种角色（<strong>employee, employee.extended, visitor</strong>)。其中employee和employee.extended是内部用户，employee是缺省用户角色，如果从Connections 4.x升级上来的全部用户都是employee。employee.extended和employee相比，多出的权限是允许创建‘外部内容’。在5.0中，‘外部内容‘指的是可以被<strong>受邀请的</strong>外部用户（visitor）访问到的内容。</p>
<p>visitor角色是外部用户，在5.0中是支持的唯一的外部角色。哪visitor能做哪些事呢？可以来看看一个visitor登录后的界面：</p>
<p><a href="/assets/media/uploads/2014/06/visitor.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-961" title="visitor" src="/assets/media/uploads/2014/06/visitor.png" alt="" width="754" height="370" /></a></p>
<p>可以看到visitor登录后在导航条内只有社区和文件。visitor可以在文件中自由上传文件，而他在社区中的权限，概况一下：</p>
<p>1)visitor不能成为社区管理员；</p>
<p>2)visitor只能被邀请到外部私有社区；</p>
<p>3)只有employee.extended角色创建的外部私有社区才可以邀请visitor；</p>
<p>4)一旦visitor成为外部私有社区成员，它的权限基本上与employee角色的社区成员一致，可以任意在社区内创建内容，在有些功能点如员工目录浏览、完整电子名片、导出社区成员列表等上受到限制。</p>
<p>一个visitor要登录Connections，必须为他在LDAP和Profiles里创建记录。LDAP记录用来登录验证用户名和密码，Profiles记录用来保存其角色信息和个人的其他信息（所以要求如果客户需要使用外部用户功能时，必须要安装Profiles并且打开WPI设置 - 位于LotusConnections-config.xml内，用Installer安装后缺省打开）。在LDAP中标记一个用户是外部用户有多钟方法 - 分支、属性和Javascript，通过TDI利用LDAP上的这些值可以把外部用户导入到Profiles中。在完成了TDI外部用户导入以后，系统中会存在两类用户：employee（之前存在的用户，或者LDAP中不具备外部用户标记的用户）和visitor。如果要添加employee.extended用户，或者要改变某个用户的角色该怎么做？答案是使用Profiles MBean命令行，或者是Profiles administrative REST API。MBean命令行还支持批量更新用户角色。</p>
<p>在UI方面，为了醒目的标示出一个社区、文件是外部用户可参与的内容，我们在界面上用黄色的提示条、图标和用户头衔装饰的方法，时刻提醒用户这是一个外部用户可以访问到的内容：提醒用户发帖的时候，仔细拿捏一下。</p>
<p style="text-align: center;"><a href="/assets/media/uploads/2014/06/visitor_deco.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-963" title="visitor_deco" src="/assets/media/uploads/2014/06/visitor_deco.png" alt="" width="797" height="421" /></a></p>
<p>安装配置上，Connections 5.0并没有为外部用户引入额外的配置文件和参数，也就是说当安装好后，系统既可以用作纯内部员工使用，也可以混合使用。一旦引入了外部用户，为了保证信息隔离，我们要求完成两个额外配置：</p>
<p>1) 禁止匿名访问。因为visitor不可以访问内公共内容，所以必须强制用户登录。禁止匿名访问功能在前几个版本就已经实现了，是通过在WebSphere管理控制台把‘reader’映射为All Authenticated。</p>
<p>2) 禁止公开缓存 (public cache)。为了提高HTTP性能，Connections会在公共资源如公共博客、论坛的HTTP response中加入publich cache control header，它们可以被cache proxy所缓存住，当有其他用户访问被cache住的link的时候可以直接从缓存服务器返回。但在启用外部用户的情况下，这些缓存会带来信息泄露的问题，因为一个visitor可以请求一个本不允许访问的公共资源链接，绕过后台应用的权限检查而读到该内容。要禁止公共缓存，需要在LotusConnections-config.xml中加入一个属性 ：</p>
<p><em><strong>&lt;genericProperty name="publicCacheEnabled"&gt;false&lt;/genericProperty&gt;</strong></em></p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(6)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">匿名</span><time class="comment-date">2014-06-26 16:42:59</time></div>
  <div class="comment-body"><p>wonderful!</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">匿名</span><time class="comment-date">2014-06-26 16:44:07</time></div>
  <div class="comment-body"><p>cool</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Liuxiaoping</span><time class="comment-date">2014-06-26 17:46:52</time></div>
  <div class="comment-body"><p>Cool!</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Qi wei</span><time class="comment-date">2014-06-27 08:31:49</time></div>
  <div class="comment-body"><p>"publicCacheEnabled"最后是怎么实现的？filter吗？然后之前讨论的server-side cache，后来怎么样了？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Qi wei</span><time class="comment-date">2014-06-27 08:33:31</time></div>
  <div class="comment-body"><p>这儿博客评论的时间显示有问题啊，"  at "，time信息重复了 :-)</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2014-06-27 10:49:57</time></div>
  <div class="comment-body"><p>@Qi Wei - 重复时间修复了。</p>
<p>server-side cache没法儿条件性缓存，所以这个参数控制所有response的cache头，不区分用户类型。</p></div>
</li>
</ol>
</section>
{% endraw %}
