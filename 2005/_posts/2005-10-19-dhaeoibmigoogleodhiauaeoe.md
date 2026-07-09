---
layout: post
title: "小测试：IBM和Google中文机器翻译"
date: 2005-10-19 13:41:00 +0800
permalink: /20051019/dhaeoibmigoogleodhiauaeoe.html
wp_id: 278
wp_slug: "dhaeoibmigoogleodhiauaeoe"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>Google的自动机器翻译很不错，而IBM也有自己的机器翻译引擎，现在集成在<a href="http://www-306.ibm.com/software/pervasive/products/voice/translation_server.shtml">WebSphere Translation Server</a>中。周五我用了半天的时间，利用WTS机器翻译API写了一个基于SWT的小程序，可以把Windows Explorer里的英文文本文件拖放到SWT窗口上，点一下按钮进行翻译然后自动保存翻译后的文件。这个小工具是打算翻译从BT上下载的电影上带的.srt格式的字幕文件而写的（.idx和.sub采用的是位图字幕，不能直接利用机器翻译处理）。</p>
<p>下面是我用这个小工具(WTS引擎)和<a href="http://www.google.com/language_tools?hl=en">Google Translate</a>这两个翻译引擎的一个比较。注：小规模采样，不能作为引擎的基准测试标准，仅供参考。</p>
<p><strong>英文来源：新华社“神六”新闻稿。</strong></p>
<p>“The launch and return of Shenzhou 6 has cost China 1 billion Yuan, b<!--ADV_CONTENT-->ut the turnover, according to experts, should be 5 to 6 times that figure. The development of space industry's development has historically been a strong impetus for a nation's growth and China is continuing this trend. China's space mission has boosted related industries and created domestic value of approximately 100 billion Yuan. "</p>
<p><strong>Google自动翻译结果：</strong></p>
<p>“发射和回归Shenzhou 6 花费中国1 十亿元, 但转交,&nbsp; 根 据专家, 应该是出现的5 到6 次。空间industry's 发展发展历 史上是坚强推动为nation's 成长并且中国正在继续这个趋向。 China's 航天任务促进相关产业和创造大约100&nbsp; 十亿元的国内 价值。”</p>
<p><strong>IBM自动翻译结果：</strong></p>
<p>“Shenzhou 6的发射和回报已经使中国付出十亿元,但是周转根据专家将去乘那个数字是5比6.航天工业发展的发展已经为一个国家的成长在历史上是一强烈动力和中国正继续这倾向.中国的空间任务已经增强相关工业和建立大约一千亿元的国内价值.”</p>
</p>
</div>
{% endraw %}
<!--more-->
