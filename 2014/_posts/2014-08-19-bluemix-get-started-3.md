---
layout: post
title: "上手Bluemix (3)"
date: 2014-08-19 17:46:52 +0800
permalink: /20140819/bluemix-get-started-3.html
wp_id: 1109
wp_slug: "bluemix-get-started-3"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>截止<a href="http://www.zhangling.org/blog/20140815/bluemix-get-started-2.html">上篇文章</a>，我们已经在Bluemix上构建了一个可以连接Bluemix数据库服务、基于WebSphere Liberty Server的Java Web应用了。我们提到Connections Blogs的老版本（相比新版本对WebSphere Application Server (WAS)已经是最小的了）跑起来还是会有很多错误，大致总结一下：</p>
<p>1) WAS专用API. 如做Basic Authentication用的是WAS Programmatic Login的API;</p>
<p>2) 和WAS环境相关的配置文件。代码中需要到WAS环境下特定的目录找某些配置文件；</p>
<p>3) 不同Web container的实现差异。在移植过程中发现对于URL的最后一个斜杠/，在WAS和Liberty中处理是不同的；</p>
<p>4) 文件系统。Blogs会把上传附件保存在文件系统，目前我也不清楚Bluemix上给我的空间大小(应该是1G)和位置。通过测试说明至少服务器端代码是可以在Liberty安装目录下创建目录和文件的；</p>
<p>5) Directory service。这是Connections自己的code，根据用户配置调用WAS VMM API从Federated Repository，或者Connections Profiles里查找用户详细信息。这两个数据源在Bluemix上都没有，所以需要更新一些代码跳过用户同步过程。</p>
<p>在disable了Basic Authentication、Connections navbar、Directory service和Lucene index后，Blogs最终可以跑在Bluemix上。</p>
<p>最后的问题是用户登录，我没打算搞个LDAP，只要创建些简单的测试用户就可以了。在Liberty里很容易做到，通过在server.xml中添加用户定义和角色定义，如下：</p>
<p><strong>定义用户：</strong></p>
<p><em>&lt;basicRegistry id="basic" realm="WebRealm"&gt;</em><br />
<em>      &lt;user name="ajones1" password="jones1"/&gt;</em><br />
<em>      &lt;user name="ajones2" password="jones2"/&gt;</em><br />
<em>      &lt;user name="ajones3" password="jones3"/&gt;</em><br />
<em>      &lt;user name="ajones4" password="jones4"/&gt;</em><br />
<em>      &lt;user name="ajones5" password="jones5"/&gt;</em><br />
<em>      &lt;user name="ajones6" password="jones6"/&gt;</em><br />
<em>&lt;/basicRegistry&gt;</em></p>
<p><strong>定义用户在应用中的role：</strong></p>
<p><em>&lt;application type="war" id="blogs" name="blogs" location="blogs.war"&gt;</em><br />
<em>    &lt;application-bnd&gt;</em><br />
<em>        </em><br />
<em>        &lt;security-role name="<strong>person</strong>"&gt;</em><br />
<em>            &lt;special-subject type="<strong>ALL_AUTHENTICATED_USERS</strong>" /&gt;</em><br />
<em>        &lt;/security-role&gt;</em><br />
<em>        &lt;security-role name="<strong>admin</strong>"&gt;</em><br />
<em>            &lt;user name="ajones1"/&gt;</em><br />
<em>        &lt;/security-role&gt;</em><br />
<em>        </em><br />
<em>    &lt;/application-bnd&gt;</em><br />
<em>&lt;/application&gt;</em></p>
<p>"ALL_AUTHENTICATED_USERS"是个特殊的保留角色，对应于WAS的相同角色，用来指定所有已登录用户。测试中我发现security-role的映射有bug，不是每次调用<em>request.isUserInRole(role)</em>都会返回正确的结果。</p>
<p>接下来的事情很关键 - 如何把一份自定义的server.xml文件上传到server端？答案：你做不到。目前找到的解决方案是按照Bluemix的buildpack去部署应用，即同时上传Liberty的Runtime和应用程序。利用Eclipse的Bluemix插件很容易实现:</p>
<p>1) 下载Eclipse Bluemix插件。在Eclipse Marketplace搜索‘bluemix’，找到后安装：</p>
<p><a href="/assets/media/uploads/2014/08/bluemix-plugin-install.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1113" src="/assets/media/uploads/2014/08/bluemix-plugin-install.png" alt="bluemix-plugin-install" width="567" height="545" /></a></p>
<p>2) 安装后右键在Server Tab里点New Server，选择IBM Bluemix，开始配置：</p>
<p><a href="/assets/media/uploads/2014/08/config-bluemix-plugin.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1114" src="/assets/media/uploads/2014/08/config-bluemix-plugin.png" alt="config-bluemix-plugin" width="722" height="604" /></a></p>
<p><a href="/assets/media/uploads/2014/08/domain.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1116" src="/assets/media/uploads/2014/08/domain.png" alt="domain" width="628" height="433" /></a></p>
<p><a href="/assets/media/uploads/2014/08/bind-db.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1117" src="/assets/media/uploads/2014/08/bind-db.png" alt="bind-db" width="627" height="433" /></a></p>
<p>3) 配置完成后，可以直接用Publish选项发布整个Runtime和application。</p>
<p><a href="/assets/media/uploads/2014/08/upload.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1119" src="/assets/media/uploads/2014/08/upload.png" alt="upload" width="543" height="525" /></a></p>
<p>&lt;终&gt;</p>
</div>
{% endraw %}
<!--more-->
