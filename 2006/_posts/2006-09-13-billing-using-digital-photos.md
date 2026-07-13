---
layout: post
title: "抄表"
date: 2006-09-13 23:59:39 +0800
permalink: /20060913/billing-using-digital-photos.html
wp_id: 500
wp_slug: "billing-using-digital-photos"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>今天在地铁里取了免费《时代报》的读者一定看到了这样一条新闻：为了便于工作繁忙的白领们及时交付水电煤费，上海准备推出用手机、数码相机对计量表进行拍照，然后通过电子邮件、彩信发给水电煤气公司，实现抄表作业的服务。</p>
<p>不知道其他城市是怎样抄表的，我所在的小区水、电表是在户外的，抄表员在业主不在家的时候也可以抄表，但燃气表是在室内，需要自己每两个月抄一次，贴在门上。如果碰巧忘记，上门的抄表员就会估计一个数字，打入帐单中。</p>
<p>对于自动抄表，我以前听说有用RFID技术的，是不是Honeywell搞的，记不清了。上海的新做法，是用数字的方法实现模拟的抄表：最后一步需人工看数码照片，记录读数。</p>
<p>不考虑该办法的实际成本，假如要设计这样一套系统，把需要考虑的问题和备选方案，稍微列一下：</p>
<p>1. 如果发email的话，单一收件地址肯定不行，要爆掉；或者每个区每个街道一个专用email地址；还得要求邮件标题符合一定规范，帮助自动过滤分类；要考虑客户email客户端的编码，GB2312/UTF-8都得能处理；不少免费邮件会自带广告，不小心会被收件服务器当垃圾邮件过滤掉；一定有很多人不注意，拍好的照片不压缩、不resize，一个几兆的文件丢过去，还有人只发了信忘记带上附件；如果出现错误邮件，收件方是否需要一一回复确认，还是听之任之；</p>
<p>2. 如果使用Web提交方式，上面一些如邮件编码等问题可以避免，可控性明显加强，做的好一点就可以像Wiki page的attachment。另外需要用户注册，每个用户必须有唯一ID与家庭住址门牌号对应，每户每月（或双月）只能上传一次照片，照片在燃气公司处理前可以修改，处理后只读，方式同网上购物的订单管理；</p>
<p>3. Flicker + <a href="http://www.smmail.cn/smmail/sy/index.html">市民信箱</a>；</p>
<p>4. 短信绑定用户、验证身份；发送附加照片的彩信到指定号码；每条彩信收费2元。</p>
<p>能想出这个办法的人还是很佩服的，一直认为“笨拙的使用高科技”是可爱、可敬的，况且提出这个方案需要头脑和勇气，要赞的。
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">Comments <span class="comment-count">(11)</span></h2>
<p class="comments-note">These comments were migrated from the original blog and are archived read-only.</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">peter</span><time class="comment-date">2006-09-14 23:21:25</time></div>
  <div class="comment-body"><p>其实第二种方式比较好,提交照片的时候立刻就把图片中的数字识别出来,并且请用户更正(如果有错的话,其实现在的识别率肯定可以保证不用出错了),最后确认后再提交.这个时候提交的就只是文本信息,而不是图像信息了.</p>
<p>看到这个,我想起了两件事情.<br>
1)同济大学本科生的成绩查询系统,除了显示数字化的成绩外,还附有该科目试卷得分处的图片.这种透明化的方式,方便了学生核实,避免发生统计错误.----但是我一直认为这样的话,工作量,存储量会很大.这个系统我没有使用过,是我上模式识别课程的时候,负责开发这个系统的老师讲的.这个似乎跟图像识别无关,只是一种互相认证的方式.<br>
2)前几天去梅龙镇广场看(推荐), 才发现有个识别手机电影票的售票机.我估计其工作原理就是在客户通过手机订票,在到达影院后,把显示着订票确认后由SP发来座位信息的短信内容的手机放进仪器内进行图像识别.机器确认后打印出一张相应的电影票出来.----这种方式倒是不错,发个短信就可以得到电影票了.不知道已经投入使用了多久了.呵呵.估计其它领域,例如车票,机票也有了这样的服务了.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">peter</span><time class="comment-date">2006-09-14 23:21:54</time></div>
  <div class="comment-body"><p>其实第二种方式比较好,提交照片的时候立刻就把图片中的数字识别出来,并且请用户更正(如果有错的话,其实现在的识别率肯定可以保证不用出错了),最后确认后再提交.这个时候提交的就只是文本信息,而不是图像信息了.</p>
<p>看到这个,我想起了两件事情.<br>
1)同济大学本科生的成绩查询系统,除了显示数字化的成绩外,还附有该科目试卷得分处的图片.这种透明化的方式,方便了学生核实,避免发生统计错误.----但是我一直认为这样的话,工作量,存储量会很大.这个系统我没有使用过,是我上模式识别课程的时候,负责开发这个系统的老师讲的.这个似乎跟图像识别无关,只是一种互相认证的方式.<br>
2)前几天去梅龙镇广场看(推荐), 才发现有个识别手机电影票的售票机.我估计其工作原理就是在客户通过手机订票,在到达影院后,把显示着订票确认后由SP发来座位信息的短信内容的手机放进仪器内进行图像识别.机器确认后打印出一张相应的电影票出来.----这种方式倒是不错,发个短信就可以得到电影票了.不知道已经投入使用了多久了.呵呵.估计其它领域,例如车票,机票也有了这样的服务了.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">peter</span><time class="comment-date">2006-09-14 23:28:47</time></div>
  <div class="comment-body"><p>hehe, 发现了输入系统的一个bug,上面我是说到 梅龙镇广场看 &amp;lt; 东京审判 &amp;gt;结果,这个东京审判就没有显示出来.</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">peter</span><time class="comment-date">2006-09-14 23:33:00</time></div>
  <div class="comment-body"><p>上面的 大于号和小于号能显示出来,是因为我用了转义符号 "&amp;lt; 东京审判 &amp;gt;"</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-09-14 23:55:39</time></div>
  <div class="comment-body"><p>同济的方法不错，学生查分的时候肯定是要看的，人还是信物理的东西；<br>
梅陇镇的这个也很酷，不过很怀疑识别成功率。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">magic</span><time class="comment-date">2006-09-15 13:18:28</time></div>
  <div class="comment-body"><p>梅陇镇的东西是二位码，相信一年内会大批量用了，在日本已经用的狠普遍的说</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-09-15 23:36:49</time></div>
  <div class="comment-body"><p>什么叫二位码</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-09-16 00:17:34</time></div>
  <div class="comment-body"><p>应该是指二维码。</p>
<p>参见：http://www.gmedia.cn/index.htm</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">magic</span><time class="comment-date">2006-09-16 21:56:16</time></div>
  <div class="comment-body"><p>Nod，就是楼上的。 ：）</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Peter</span><time class="comment-date">2006-09-17 08:43:00</time></div>
  <div class="comment-body"><p>原来是环艺电影院线今年7月底才开始用的,</p>
<p>http://www.chinacsw.com/zlzx/compnews.asp?id=60658&amp;amp;city=%D6%D8%C7%EC%CA%D0&amp;amp;classen=puyang</p>
<p>二维码挺好的,拥有条形码一般的识别率.</p>
<p>会不会以后用RFID来买票的?呵呵.如果手机(手持移动设备)能够动态地发射出不同的射频,然后通过RFID reader来识别......</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://hi0898.com" rel="nofollow noopener">wzy</a></span><time class="comment-date">2006-10-01 17:45:12</time></div>
  <div class="comment-body"><p>原来停车是咪表管理，现在很多地方都把咪表撤了，换手机管理了，成本低的笨方法有时也不错。</p></div>
</li>
</ol>
</section>
{% endraw %}
