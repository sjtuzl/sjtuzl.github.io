---
layout: post
title: "IBM Connections5.0新功能介绍(4) – 自动图片上传"
date: 2014-07-02 18:06:06 +0800
permalink: /20140702/ibm-connections5-4-autoimage.html
wp_id: 996
wp_slug: "ibm-connections5-4-autoimage"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Connections 5.0的自动图片上传功能极大简化了图片附件上载的过程 - 它允许用户用copy/paste的方式把图片拷贝到编辑器中，Connections会自动把图片解码并上传到后台服务生成附件，之后服务器返回一个图片的URL并插入到当前编辑器中，整个过程对用户是完全透明的。</p>
<p style="text-align: center;"><a href="/assets/media/uploads/2014/07/insertimage.png"><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-997" title="insertimage" src="/assets/media/uploads/2014/07/insertimage.png" alt="" width="718" height="507" /></a></p>
<p>现在的新浏览器很多都已经支持图片拷贝功能，但浏览器的处理方法是把图片用BASE64编码，并嵌入到正文中。这种方法有不少问题，比如图片无法单独缓存，第三方应用无法正确显示图片等。Connections采用的方法在用户体验、适用性和性能上达到了最好的平衡。</p>
</div>
{% endraw %}
<!--more-->
