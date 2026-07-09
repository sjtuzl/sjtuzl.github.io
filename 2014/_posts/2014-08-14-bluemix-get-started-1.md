---
layout: post
title: "上手Bluemix (1)"
date: 2014-08-14 17:17:12 +0800
permalink: /20140814/bluemix-get-started-1.html
wp_id: 1065
wp_slug: "bluemix-get-started-1"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>之前写了个短文，说把IBM Connections Blogs移植到了Bluemix上。今天花点时间，写写具体的过程。对于不熟悉Bluemix的人，我一句话解释一下：Bluemix是IBM的PaaS平台，供开发者构建在云上跑的应用，而Bluemix本身是架在SoftLayer (IBM IaaS)之上的。</p>
<p>先来看看Bluemix长啥样。对于首次访问的用户，基本上唯一有用的界面就是Catalog了，里面列举了Bluemix提供的runtime、service和各种组件，大家的第一个应用就从这里开始。</p>
<p><a href="/assets/media/uploads/2014/08/catalog.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1067" src="/assets/media/uploads/2014/08/catalog.png" alt="catalog" width="800" height="370" /></a></p>
<p>IBM Connections是基于Java的Web应用，所以我们选择的Runtime是Liberty for Java（一个约20MB左右的Java Web容器）。输入基本参数，一个缺省的Webapp和一个WebSphere Liberty Profile的instance就产生了。这个webapp的首页是显示当前应用的一些运行时参数。</p>
<p><a href="/assets/media/uploads/2014/08/liberty.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1069" src="/assets/media/uploads/2014/08/liberty.png" alt="liberty" width="800" height="360" /></a>当创建好第一个应用后，Dashboard就成了常用的视图了，应用的启/停、监控、服务的创建和绑定都要在这个界面上完成。</p>
<p><a href="/assets/media/uploads/2014/08/quickstart.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1074" src="/assets/media/uploads/2014/08/quickstart.png" alt="quickstart" width="800" height="410" /></a></p>
<p>对于新手来说，'View Quick Start'按钮很有帮助，它指导开发者之后需要做的事情，包括安装cf工具来做应用上载，以及如何登陆和访问。我一开始就是按照这个步骤在写了Hello World之后把应用打包后用cf push到Bluemix上的。</p>
<p>有了第一个可以运行的demo webapp后，可以从Dashboard中把这个应用打包下载到本地，展开后用Eclipse在本地继续开发，完成后重新打包上传。多尝试几次后，就可以熟练的更新、上传应用了。需要注意的是，应用更新的最小粒度是.war（至少今天我都没有找到文件级别的更新），也就是说即使要改一个JSP文件也需要完整打包后上传。我试图找到类似SSH的方式允许远程文件上传，但最终没有找到。开发者能够在文件级别范围的访问仅限于在'Files and Logs'菜单下浏览文件目录并下载里面的文件，如log等。</p>
<p><a href="/assets/media/uploads/2014/08/filesystem.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1072" src="/assets/media/uploads/2014/08/filesystem.png" alt="filesystem" width="560" height="559" /></a></p>
<p>最后谈谈本地开发和测试。开发者可以使用Eclipse加上WebSphere Liberty Profile runtime集成到Eclipse中，具体下载地址 - <a href="https://developer.ibm.com/wasdev/downloads/liberty-profile-using-eclipse/">https://developer.ibm.com/wasdev/downloads/liberty-profile-using-eclipse/</a>。搞定后的开发环境大概是这样的（截图里面的Bluemix插件，下次再介绍）。</p>
<p><a href="/assets/media/uploads/2014/08/eclipse.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1082" src="/assets/media/uploads/2014/08/eclipse.png" alt="eclipse" width="630" height="266" /></a></p>
<p>好了，到此为止一个简单的Java webapp已经可以欢快的跑在Bluemix之上，我们也初步了解了开发者该如何更新和部署这个应用了。接下来，谈谈如何创建一个数据库服务并绑定应用，待续。</p>
</div>
{% endraw %}
<!--more-->
