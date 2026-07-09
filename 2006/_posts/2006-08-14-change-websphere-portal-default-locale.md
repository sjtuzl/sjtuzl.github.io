---
layout: post
title: "更改WebSphere Portal 5.1缺省locale"
date: 2006-08-14 21:30:17 +0800
permalink: /20060814/change-websphere-portal-default-locale.html
wp_id: 480
wp_slug: "change-websphere-portal-default-locale"
has_comments: false
---
{% raw %}
<div class="e-content">
<p><strong>症状：</strong></p>
<p>访问WebSphere Portal在浏览器生成弹出式calendar，其月份显示为中文。由于应用程序对日期的校验是针对英文格式设计的，所以客户端无法正确提交被格式化后的日期参数。经研究，此calendar的日期信息是根据server locale格式化的，因此需要把portal的缺省locale设置成en_US，从而在不修改应用代码的前提下跑通此程序。</p>
<p><strong>实验：</strong></p>
<p>1. 因为操作系统为中文Windows 2000 Server，想到的第一个办法是在控制面板中更改区域设置，把OS的locale设为“英语(美国)”。重启机器，启动portal后，问题依旧;</p>
<p>2. 修改startServer.bat里调用的setupCmdLine.bat，添加“set LANG=en”；无效；</p>
<p>3. 修改startServer.bat的Java 启动参数，加上“-Duser.language=en”，重启Portal；无效；</p>
<p>4. 最终解决方案：修改portal的安装配置文件：”<PortalInstallDir>/shared/app/config/services/LocalizerService.properties“ ，设置参数”<strong>locale.default.language=en</strong>“。</p>
<p><strong>分析：</strong></p>
<p>WebSphere Portal在安装时，检测当前操作系统locale，并写入配置文件。此后每次portal server启动，读取此参数并调用Locale.setDefault()覆盖JVM的缺省值。
</p>
<p>
</div>
{% endraw %}
<!--more-->
