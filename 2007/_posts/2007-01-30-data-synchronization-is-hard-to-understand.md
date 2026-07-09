---
layout: post
title: "同步"
date: 2007-01-30 22:18:57 +0800
permalink: /20070130/data-synchronization-is-hard-to-understand.html
wp_id: 613
wp_slug: "data-synchronization-is-hard-to-understand"
has_comments: true
---
{% raw %}
<div class="e-content">
<p>数据同步，是很多计算机软件都有的功能，用来帮助以实现两份数据的一致性。可我对同步却一直很小心谨慎，甚至尽量回避，因为要理解每个软件自己对同步的定义，以及这些定义隐藏下的实现是很劳神的事儿。</p>
<p>刚用Notes的时候， 知道了要做“复制”，即服务器上的新邮件会下载到本地复本上；而本地复本上自上次复制后被删除的邮件，在新的复制过程中会从服务器端同时删除。这样“复制”下来，服务器和本地的拷贝完全一样。我有一次不小心，在本地批量删除了上百个邮件，于是不敢继续“复制”，生怕一损俱损。为了把服务器上保存着的那几百封邮件重新拷贝到本地，我选择了为远程邮件创建一个新复本。在新复本复制完成后，改文件名成当前本地邮件复本，同事删除老复本（绝对的笨办法，但我整个过程，自己可以完全理解并明确知道每一步的后果）。</p>
<p>iPod的“同步”，是要求iTunes上的资料库与iPod播放器里一致，通俗一点就是绑定：iTunes instance和iPod设备的绑定。如果要用自己机器上的iTunes上拷贝音乐到别人的iPod上，意味着要首先删除这个iPod上的内容，然后“同步”。我不知道可不可以支持从iPod到iTunes的同步，即iPod上的歌曲覆盖iTunes的资料库（考虑到著作权问题）。如此一来，iPod的同步成了单向复制，不仅是内容只进不出，而且更换iTunes，会导致iPod上数据强制删除。</p>
<p>Windows Mobile的同步，我完全不用。每次通过USB接上PDA后，总是要问我要不要同步，我不知道它是让我把PDA里的新东西传递到PC上，还是PC上的东西传到PDA上，还是双方有了内容修改，彼此更换内容并达成一致。</p>
<p>Lotus EasySnyc我尝试用过一次，也没有太明白“同步”到底是从哪儿到哪儿：同步后如果PDA上更改，信息能否回到PC；PC上信息更改，是否能回到PDA上；双方同时更改，谁来覆盖谁？</p>
<p>所以在真正的同步操作发生前，用户几乎没有机会能了解到“同步”后究竟会导致哪些事情发生，哪里的数据最新、最可靠？整个过程可逆否？如果两边的数据都可以被独立修改的话，如此一来，数据同步和源代码版本控制便很类似了。代码控制提供的词汇比“同步”这两个词好，普通用户很容易理解它的含义：update（这个有点晦涩）, check-in, check-out, add to control, commit，方向性都十分明确而且可以被理解。</p>
<p>如果还有新的软件需要“同步”功能，希望能在对话框上有类似下面这样明确的选项（不妨考虑用"下载"、"上传"这样更明确的词汇以避免混淆）：</p>
<p><img loading="lazy" decoding="async" src="/assets/media/uploads/2007/01/sync-dialog.jpg" /></p>
<p>对于潜在的、需要作出取舍的选择，多透露一点实现细节，让操作结果变得可预测，有助于简化使用、树立用户对产品的信心。
</p>
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(4)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2007-01-30 23:29:00</time></div>
  <div class="comment-body"><p>我的Siemens SX1手机和Microsoft Outlook同步通信录的时侯，Siemens的同步软件就有你希望的这许多选项，呵呵，可见德国人做事还是比较严谨的。唉，只可惜西门子手机花落明基就此消失了。P.S. 偶很喜欢严谨的德国人的德国货——偶的冰箱也是西门子的，连剃须刀都是博朗的，呵呵。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-01-31 08:39:03</time></div>
  <div class="comment-body"><p>腐败，呵呵</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">vogel</span><time class="comment-date">2007-02-01 16:46:54</time></div>
  <div class="comment-body"><p>你的“同步”的理解很独到。不过我想，同步可能用在这方面上感觉你的理解偏向于数据的备份和恢复。这样理解的话，感觉似乎对他有些大材小用了。在控制理论中对同步的需求是不言而喻的，在其他领域里比如移动通信（如蓝牙）里面，“数据”同步意味着终端能否获得唯一的标识，这个意义就比较大了吧。</p>
<p>PS：德国货嘛，呵呵，我比较清楚。剃须刀其实在德国最好的还是飞利浦的吧，感觉上，奇怪吧。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/blog" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2007-02-02 08:39:08</time></div>
  <div class="comment-body"><p>剃须刀还是手工的好，很想要个Gillette Fusion，国内还没有卖的。</p></div>
</li>
</ol>
</section>
{% endraw %}
