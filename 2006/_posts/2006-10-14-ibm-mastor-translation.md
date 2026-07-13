---
layout: post
title: "跨语言交流的Mastor"
date: 2006-10-14 21:58:41 +0800
permalink: /20061014/ibm-mastor-translation.html
wp_id: 519
wp_slug: "ibm-mastor-translation"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>据<a href="http://news.yahoo.com/s/pcworld/20061012/tc_pcworld/127481">报道</a>，美国政府将在伊拉克部署IBM的自动翻译系统Mastor，用来帮助驻伊美军与使用阿拉伯语的当地警察进行交流。</p>
<p>Mastor安装在一台移动计算机上，包括了语音识别、机器翻译、语音合成技术。使用双方分别对着电脑用自己的母语说话，然后计算机在对语音信号进行分析后、翻译、合成后播放出来。</p>
<p>Mastor的主要使用场合包括医疗信息等特殊环境下的辅助翻译（可以想象在这个领域用外语交流的难度） ，借助Mastor，说不同语音的医生和病人可以更好的交流。</p>
<p>我曾经在Yorktown举行的一次技术展示里看到IBM开发的从阿拉伯文到英文的自动翻译和摘要系统。不难想象911对于这个研究工作的带来的影响和推动作用。</p>
<p><a href="http://domino.research.ibm.com/comm/research_projects.nsf/pages/mastor.index.html">IBM Mastor 主页</a><br />
<a href="http://www.research.ibm.com/jam/speech_to_speech.mpg">IBM Mastor演示</a>
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(6)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Jet</span><time class="comment-date">2006-10-16 12:47:46</time></div>
  <div class="comment-body"><p>感觉只是一些简单的对话，而且语速不能太快。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vogel</span><time class="comment-date">2006-11-15 23:40:56</time></div>
  <div class="comment-body"><p>请问这个Mastor与IBM Translation Server有何关系？<br>
我正在做一个项目中用到IBM的WTS。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-11-16 08:34:22</time></div>
  <div class="comment-body"><p>没有直接的关系，Mastor应该用到了机器翻译引擎，这个和WTS里的应该很相似。Mastor里另外一个核心组件是语音识别，这是WTS里没有的（包含在WebSphere Voice Server里）。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vogel</span><time class="comment-date">2006-11-16 16:51:58</time></div>
  <div class="comment-body"><p>我的意思是，这个Mastor是不是集成了WTS以及你所说的WebSphere Voice Server来进行跨语言交流的？感觉WTS使用RMI与其他组件应该都可以通信吧。不过这三个核心技术每一个都是难中之难啊。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-11-16 21:10:55</time></div>
  <div class="comment-body"><p>Mastor应该不会直接集成WTS，会用其中的组件，WVS也一样。WTS的RMI就是一个接口，开放给应用调，Mastor不是一个分布式系统，就一个黑盒子，两边各做一人，一个说，翻译好了后另外一个说。</p>
<p>我曾把WTS的Machine translation单独抽出来，几个大词库和Java API及dll，可以自己写程序实现机器翻译。WebSphere和RMI，是它身上包的一层可拆卸的壳。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vogel</span><time class="comment-date">2006-11-16 22:18:22</time></div>
  <div class="comment-body"><p>也是<br>
刚才看了下mastor主页里的，原来mastor都可以用PDA来实现。既然用不着分布式实现，那自然用不着RMI。只是不知道该怎么剥离。毕竟，暂时我只看到了WTS API，还没有看到里面的东东。真有些雾里看花的感觉。</p></div>
</li>
</ol>
</section>
{% endraw %}
