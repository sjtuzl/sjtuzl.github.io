---
layout: post
title: "上手Bluemix (2)"
date: 2014-08-15 15:41:39 +0800
permalink: /20140815/bluemix-get-started-2.html
wp_id: 1087
wp_slug: "bluemix-get-started-2"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>上次说到在Bluemix新建一个简单的Java webapp，现在这个Java应用需要访问数据库服务来存取数据，我们来看看在Bluemix上该如何使用和管理数据库服务。首先，Bluemix上有多种数据库服务供选择，有传统的关系型数据库也有NoSQL (包含了IBM收购的Cloudant)，因为Connections本身支持包括DB2， Oracle和SQL Server，所以我们选择基于IBM DB2的数据服务。</p>
<p>可以从Dashboard的Service tab或者直接从Catalog进入服务选择界面，选择Data Management -&gt; SQL Database：</p>
<p><a href="/assets/media/uploads/2014/08/database.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1089" src="/assets/media/uploads/2014/08/database.png" alt="database" width="635" height="373" /></a></p>
<p>创建时需要指定服务名（注意这个名字既不是数据库名也不是schema名，仅仅是个标示符），同时如果应用已经创建好，可以在创建数据库服务的时候直接绑定应用。</p>
<p><a href="/assets/media/uploads/2014/08/create-db-instance.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1091" src="/assets/media/uploads/2014/08/create-db-instance.png" alt="create-db-instance" width="786" height="417" /></a></p>
<p>创建好数据库服务后回到Dashboard，可以看到名下有一个应用和一个服务 - APPS(1) &amp; SERVICES(1) - 移植Connections Blogs需要的全部组件都齐了。</p>
<p><a href="/assets/media/uploads/2014/08/db-service.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1092" src="/assets/media/uploads/2014/08/db-service.png" alt="db-service" width="800" height="400" /></a></p>
<p>在创建并绑定数据库服务后，点击应用的Runtime选项，可以看到新生成的环境变量。这里包含了有关数据库连接的全部信息 - 注意所有的配置信息都无法更改，一旦重新创建数据库服务，数据库名、用户名、密码等都会随之改变。这些所谓’环境变量‘实际上是保存在Liberty的server.xml中，这样app在启动的时候可以正确的找到JNDI data source。</p>
<p><a href="/assets/media/uploads/2014/08/env_variable.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1105" src="/assets/media/uploads/2014/08/env_variable.png" alt="env_variable" width="800" height="400" /></a></p>
<p>接下来，我们需要创建数据库schema，tables，indexes...点击进入添加好的数据库服务，点'Launch'按钮会打开一个数据库管理界面，点击‘Work with Database Objects'就可以开始创建数据对象了。Bluemix的数据库服务不支持用本地的数据库客户端直接连接，所有的数据管理操作都必须在Web界面上完成。</p>
<p><a href="/assets/media/uploads/2014/08/schema.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1097" src="/assets/media/uploads/2014/08/schema.png" alt="schema" width="800" height="400" /></a></p>
<p>大家注意到上图有个名叫‘REUNOBRW'的schema，它和上上图里的环境变量中的数据库用户名是一致的。之所以要手工创建‘REUNOBRW' schema的原因在于我们要移植的Blogs早期版本（1.0.2）里，所有的数据库访问代码是仅有table名，不带schema名的，如下：</p>
<p><em>&lt;select id="getWebsiteById" parameterClass="string" resultMap="Website" &gt;</em><br />
<em>      SELECT * FROM website WHERE id = #value#</em><br />
<em> &lt;/select&gt;</em></p>
<p>在Bluemix环境中，这样的调用会自动在前面以用户名作为schema名。除非我们修改全部的SQL把它们都带上schema名，否则只能创建一个和用户名同名的schema。这个做法虽然可以工作，但一旦数据库服务重建schema也必须要重建，作为测试可以但作为生产环境的开发这样是不可取的。创建好schema后，可以创建table等对象了，点击Run DDL来指行数据库命令(注意不是所有的SQL都支持，比如我们无法创建table space)。下面是在创建好tables、运行应用后查询用户表的例子 -</p>
<p><a href="/assets/media/uploads/2014/08/run-sql.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1099" src="/assets/media/uploads/2014/08/run-sql.png" alt="run-sql" width="641" height="374" /></a>现在可以把Connections Blogs build成一个.war文件，通过cf push到Bluemix上，它可以正确的连接数据库，但界面上有很多错误，绝大部分是因为已有代码是在WebSphere Application Server下测试运行的，在Liberty环境下存在问题。另外也没有办法登录，因为我们还没有定义用户库。下篇文章我们将继续讨论应用的迁移。</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(2)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Phoenix</span><time class="comment-date">2014-12-30 17:03:48</time></div>
  <div class="comment-body"><p>请问dbname, scheme name, table name都是可以自定义的对吗？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2014-12-31 15:05:07</time></div>
  <div class="comment-body"><p>schema和table都可以自定义，dbname不可以。</p></div>
</li>
</ol>
</section>
{% endraw %}
