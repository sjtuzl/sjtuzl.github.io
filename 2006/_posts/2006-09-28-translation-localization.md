---
layout: post
title: "本地化一例"
date: 2006-09-28 23:42:55 +0800
permalink: /20060928/translation-localization.html
wp_id: 509
wp_slug: "translation-localization"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>听说Google Calendar出了本地化版本，出于对ajax localization实现手段的好奇，我读了一下它的JavaScritp代码，发现了蛮有趣的几个本地化语言翻译例子。</p>
<p>获取Google Calendar的JavaScript的方法很简单，"View Source"后定位到.js文件并下载即可（不能用download manager之类下载软件，因为calendar的JS文件与cookie绑定，只有认证后才可获得）。Calendar现在的JS文件从文件名上看像是动态生成的，比如叫“<span style="font-style: italic">20060927154334doozercompiled__zh_cn.js</span>”(在日历“设置”里切换语言，分别得到多份本地化JavaScript代码)。 这个JavaScript文件不小，所有的本地化消息都保存在里面，用类似Java语言里“\uxxxx”方式对非拉丁字符进行编码，无法直接查看。可以使用JDK自带的native2ascii.exe工具，执行"<em style="font-weight: bold">native2ascii -reverse source.js target.js</em>"把文件中的字符编码转换成可显示的字符串。</p>
<p>下面是在文件里找到的几处翻译：</p>
<p>1. 英文：“<span style="font-weight: bold">e.g., Dinner with Michael 7pm tomorrow</span>”</p>
<p>繁中：“<span style="font-weight: bold">例如：明晚 7 時與小李晚餐</span>”</p>
<p>简中：“<span style="font-weight: bold">例如，明天晚上 7 点同王平一起吃饭</span>”</p>
<p>2. 英文：“<span style="font-weight: bold">e.g., Breakfast at Tiffany's</span>”</p>
<p>繁中：“<span style="font-weight: bold">例如，永和豆漿早餐</span>”</p>
<p>简中：“<span style="font-weight: bold">例如，在蒂凡尼早餐</span>”</p>
<p>3. 英文：“<span style="font-weight: bold">e.g., 7pm Dinner at Pancho's</span>”</p>
<p>繁中：“<span style="font-weight: bold">例如，晚上 7 時在福華飯店晚宴</span>”</p>
<p>简中：“<span style="font-weight: bold">例如，晚上 7 点在必胜客晚餐</span>”</p>
<p>大致可以看出Google基本采用传统方式翻译语言包，即首先产生英文包，然后分发到各译员手中分别翻译，各语言的翻译员单独工作，所以就有了对餐厅翻译的繁、简中文差异问题。繁体中文的翻译比较一致，无论早餐、晚餐，地点都换成了台湾民众熟悉的品牌（“福华饭店”我猜是台北比较著名的一个餐厅）；简体中文翻译比较有趣，早餐没换地方，估计翻译的人认为蒂凡尼早餐应该是common sense（其实并不是这样），而Pancho对国人太陌生，就换成了“<span style="font-weight: bold">必胜客</span>”，呵呵。为什么不用“<span style="font-weight: bold">全聚德烤鸭</span>”呢，本地化却本地化出了一个洋玩意，合理的解释大概是全球化的强劲已经削弱了本地化的特征，过度的本地化(<span style="font-weight: bold">over localization</span>)反而不入时、不与时俱进。反映出的另外一个问题是国内没有知名的早餐连锁店。上海有“新亚大包”，估计北京人不了解；北京本地的早点品牌上海人不清楚，依我看，还不如也用“<span style="font-weight: bold">永和豆浆</span>”，容易达成共识。</p>
<p>至于“<span style="font-weight: bold">小李</span>”和“<span style="font-weight: bold">王平</span>”的差异应该说是翻译彼此没有直接沟通造成的（虽然是在同一个大文化背景下），比较正常。不过下面这段有关数量级的本地化，繁中和简中却完全一致：</p>
<p>“var tn={"<span style="font-weight: bold">零":0,"〇":0,"零":0,"壹":1,"一":1,"弌":1,"貳":2,"贰":2,"二":2,"弍":2,"兩":2,"两":2,"叄":3,"叁":3,"三":3,"弎":3,"參":3,"参":3,"肆":4,"四":4,"伍":5,"五":5,"陸":6,"六":6,"柒":7,"七":7,"捌":8,"八":8,"玖":9,"九":9,"拾":10,"十":10,"什":10,"念":20,"貳拾":20,"廿":20,"卄":20,"二十":20,"叄拾":30,"卅":30,"三十":30,"肆拾"</span><br style="font-weight: bold" /><span style="font-weight: bold">:40,"卌":40,"四十":40,"佰":100,"百":100,"仟":1000,"千":1000,"萬":10000,"万":10000,"百萬":1000000,"億":100000000,"京":1000000000,"吉":1000000000,"垓":1000000000000,"太":1000000000000,"兆":1000000000000,"拍":1000000000000000,"艾":1000000000000000000,"泽":1.0E21,"皆":1.0E21,"尧":1.0E24,"佑":1.0E24,"分":0.1,"厘":0.01,"釐":0.01,"毫":0.0010,"毛":0.0010,"微":1.0E-6,"塵":1.0E-9,"奈"</span><br style="font-weight: bold" /><span style="font-weight: bold">:1.0E-9,"纳":1.0E-9,"漠":1.0E-12,"皮":1.0E-12</span>”</p>
<p>说实话，上面的变量定义的确厉害，极有可能是通过辞海查出来的。这又是一个over localization的例子，有多少中国人知道"拍"、"皆"、"尧"呢。从翻译流程上看，这些变量的翻译是简、繁双方通过气以后达成共识双方共用的。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(1)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.littlerain.net" rel="nofollow noopener">Liu Yan</a></span><time class="comment-date">2006-09-30 09:01:17</time></div>
  <div class="comment-body"><p>看来做一个产品还是需要很多人力的，以前以为机器，程序解决一切，现在才觉得是根本不可能的（至少目前是这样的）。</p></div>
</li>
</ol>
</section>
{% endraw %}
