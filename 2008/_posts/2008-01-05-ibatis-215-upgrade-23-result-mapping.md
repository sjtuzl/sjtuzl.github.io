---
layout: post
title: "iBatis 2.1.5升级至2.3问题一则"
date: 2008-01-05 20:36:02 +0800
permalink: /20080105/ibatis-215-upgrade-23-result-mapping.html
wp_id: 699
wp_slug: "ibatis-215-upgrade-23-result-mapping"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Lotus Connections 2.0后台的O/R mapping将从iBatis 2.1.5升级到2.3，今天在测试的时候发现部署iBatis 2.3后导致Blogs出现大量exception，大部分功能失效。然而根据文档，2.3的API是向下兼容的，理应不该出现此类问题。</p>
<p>做了一番调查，发现原因如下：当iBatis拿到结果集后调用Java pojo的setter方法来保存对象集合，而如果一个pojo存在两个同名但参数类型不同的setter时，2.3版本iBatis会调用到错误的方法。以Blogs为例，其中一个pojo有两个同名的setter方法，一个参数类型是java.util.Set，另外一个是java.util.List。iBatis会错误的调用"<em>setXXX(Set mydata)</em>"而不是"<em>setXXX(List mydata)</em>"方法，因为iBatis的O/R映射集合类型是不支持java.util.Set的，所以出现argument type mismatch的错误。</p>
<p>通过修改pojo，消除同名setter方法可以解决升级到2.3后的这个问题。
</p>
<p>
</div>
{% endraw %}
<!--more-->
