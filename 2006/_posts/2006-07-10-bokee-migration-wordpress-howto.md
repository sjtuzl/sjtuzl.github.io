---
layout: post
title: "博客网(bokee/blogchina)至WordPress搬家攻略"
date: 2006-07-10 23:48:35 +0800
permalink: /20060710/bokee-migration-wordpress-howto.html
wp_id: 450
wp_slug: "bokee-migration-wordpress-howto"
has_comments: true
---
{% raw %}
<div class="e-content">
<p><strong>摘要 </strong></p>
<p>Web内容集成曾经是最困难的工作之一，感谢XML/Web services，在Web 2.0的时代终于可以比较容易的实现了。目前绝大部分blog系统都支持两种方式的内容输入：标准的基于Web的方式，即用户登录、发贴；另外就是通过API利用客户端软件发贴。这两种方式可以简单的想象成WebMail和基于SMTP邮件客户端。本文实现了基于半结构化内容抽取和异构XML目标数据的集成。</p>
<p><strong>实现方法 </strong></p>
<p>现在常用的<a href="http://codex.wordpress.org/XML-RPC_Support">Blog API</a>有Blogger API, MetaWeblog API, Movable Type API等，这些API都采用了XML-RPC进行数据包装和传输。 blogchina.com目前仅支持早期的Blogger API 1.0（而且是部分支持），而WP同时支持这三种API。</p>
<p>为了把http://zhangling.blogchina.com 里过去两年的文章完整的搬到新系统中，我首先尝试了用Blogger API去读取blogchina里的文章，但碰到了问题。</p>
<p>用Java开发，我用了<a href="http://ws.apache.org/xmlrpc/">Apache的XML-RPC</a>包。经尝试，发现blogchina仅支持<em>blogger.getUserInfo</em>、<em>blogger.getTemplate</em>和<em>blogger.getUsersBlogs</em>等几个有限的方法，对于关键的抽取文章内容的函数则完全不支持。这意味着所有的内容无法通过编程的方法获得，工作量一下上升了很多。</p>
<p>于是我在浏览器分别打开04-06年的文章列表，用下载工具将页面里所有博客文章进行批量下载（还好这个过程的工作量不是很大），然后在本地磁盘上根据年份和文章分类建立多层子目录，把对应的文章放在不同目录下面。现在的问题变成如何从HTML页面中把文章标题、内容、发贴日期和评论分别抽取出来作为XML-RPC参数发送给WP系统自动建立新文章。仔细研究了这些HTML文件，发现它们都具有相同的结构和布局，仅仅是内容上的变化，其他如布局和风格几乎完全一样。接下来就需要分析HTML代码找到文章标题、内容、日期、评论部分的特征标签以进行内容抽取。比如就标题来讲，所有的标题前都有”diaryTitle"标签；所有发贴日期都符合正则表达式"年\\S*月\\S*日.*星期\\S\\s\\d\\d:\\d\\d"，等等这些信息都对内容的正确提取提供了保证。</p>
<p>根据分析得到的特征标签，写了4个Java class（TitleExtractor, ContentExtractor, DateExtractor和CommentExtractor) 。对300多篇文章进行测试，抽取成功率100%（当然还写了一些字符串处理函数解决一些有变数的字串）。于是，数据源的问题得到的解决。</p>
<p>花费最多时间的倒是对WP的数据写入部分。我用了MetaWeblogAPI，使用XML-RPC中的XmlRpcClient类，构建好参数列表，测试发现中文出现问题。Java程序送出的XML数据包在WP系统上显示为乱码。经调试确认XML-RPC使用的是UTF-8编码，而WP也是配置成UTF-8。在调试多次失败后，我用<a href="http://www.ethereal.com/">Ethereal</a>（已经改名成<a href="http://www.wireshark.org/">WireShark</a>）捕获了发出去的HTTP数据包，发现Apache的XML-RPC实现把中文字符进行HTML转义，导致WP无法识别。为了验证，我装了<a href="http://www.zoundry.com/">Zoundry</a>并尝试发贴，在捕获的HTTP请求包中，Zoundry把“中文标题”四个汉字编码成“\344\270\255\346\226\207\346\240\207\351\242\230”，而且WP正确的接受并成功显示！接下来，我下载了<a href="http://jakarta.apache.org/commons/codec/">Apache commons codec</a>包，尝试了里面多个编码器，始终没能成功，不得不考虑使用其他Java实现。</p>
<p>最终我找到了合适的包<a href="http://sourceforge.net/projects/xmlrpc">Redstone XML-RPC</a>，它顺利的把我GB2312编码的文章上传到WP上（需要把WP缺省编码改成GB2312），于是剩下的事情就是一个for循环对目录里的所有文件做一次内容提取、参数组装和网络调用。为了简单，我把评论部分附加在正文末尾（因此可以在新博客老帖子的正文部分里看到很多老系统的影子，如黑色的头像:)</p>
<p><strong>结论</strong></p>
<p>虽然一些商业系统开始提供博客搬家服务（如<a href="http://banjia.blogbus.com/index.jsp">blogbus</a>、<a href="http://home.hexun.com/helpv2/help-11.06.aspx">和讯</a>），由于可用性的限制要实现完整的系统搬家难度还是非常大（我在blogbus尝试10篇文章的搬家未获得成功）。因此，如果懂软件开发的话，自己写点搬家程序会更容易、更便捷。</p>
<p><strong>参考文献</strong></p>
<p>1. Apache XML-RPC: <a href="http://ws.apache.org/xmlrpc/">http://ws.apache.org/xmlrpc/</a><br />
2. WordPress API: <a href="http://codex.wordpress.org/XML-RPC_Support">http://codex.wordpress.org/XML-RPC_Support</a><br />
3. Ethereal Bug 894: <a href="http://bugs.ethereal.com/bugzilla/show_bug.cgi?id=894">http://bugs.ethereal.com/bugzilla/show_bug.cgi?id=894</a><br />
4. PHP和JAVA的XML-RPC中文问题解决办法: <a href="http://bugs.ethereal.com/bugzilla/show_bug.cgi?id=894">http://fanqiang.chinaunix.net/program/php/2005-09-06/3586.shtml</a></p>
<p><strong>附录（部分代码）</strong></p>
<p>XmlRpcClient client = null;<br />
try {<br />
client = new XmlRpcClient(new URL("http://www.zhangling.org/blog/xmlrpc.php"), true);<br />
} catch (MalformedURLException e) {<br />
// TODO Auto-generated catch block<br />
e.printStackTrace();<br />
}</p>
<p>for (int i = 0; i < files.length; i++) {<br />
try {<br />
filename = folder.getAbsoluteFile() + "\\" + files[i];<br />
FileInputStream fileInput = new FileInputStream(filename);<br />
InputStreamReader reader = new InputStreamReader(fileInput,"GB2312");<br />
BufferedReader bufferReader = new BufferedReader(reader);<br />
while (bufferReader.ready()) {<br />
content = content + bufferReader.readLine() + "\n";<br />
}<br />
} catch (Exception e) {<br />
System.err.println(e);<br />
}</p>
<p>title = titleExtractor.getTitle(content);<br />
description = contentExtractor.getContent(content)<br />
+ commentExtractor.getComment(content);<br />
datestring = dateExtractor.getDate(content);<br />
content = "";</p>
<p>Vector v = new Vector();<br />
v.add("1");<br />
v.add("AAAA");<br />
v.add("********");<br />
Hashtable hashtable = new Hashtable();<br />
hashtable.put("title", title);<br />
hashtable.put("description", description);<br />
Date date = new Date(datestring);<br />
hashtable.put("dateCreated", date);<br />
String category[] = new String[1];<br />
category[0] = "技术";<br />
hashtable.put("categories", category);<br />
v.add(hashtable);<br />
v.add("true");<br />
try {<br />
Object result = client.invoke("metaWeblog.newPost", v);<br />
System.out.println("received: " + result);<br />
} catch (Exception e) {<br />
Logger.writeLog(filename + ":" + e);<br />
System.out.println(e);<br />
}</p>
<p>}</p>
<p>}
</p>
</div>
{% endraw %}
<!--more-->
{% raw %}
<section class="archived-comments" id="comments">
<h2 class="comments-title">评论 <span class="comment-count">(6)</span></h2>
<p class="comments-note">以下评论迁移自原博客，仅作存档，不可回复。</p>
<ol class="comment-list">
<li class="comment">
  <div class="comment-meta"><span class="comment-author">maoxs</span><time class="comment-date">2006-07-11 05:20:54</time></div>
  <div class="comment-body"><p>he he... 恭喜，费了这么些力气，看着很酷 :)</p>
<p>什么时候电信免费让大家都有个域名和网站吧... 到那个时候，估计个人门户就由他们提供了 -- 一股脑儿把什么 Blog, Wiki, RSS, eMail, 电子支付/Shopping, searching 等等全都是基于“服务”的方式给 mashup 起来，就不用你这么辛苦了。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-07-11 19:43:22</time></div>
  <div class="comment-body"><p>Apache的XML-RPC实现的这个问题算Bug吧？应该向他们提啊</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-07-11 20:56:54</time></div>
  <div class="comment-body"><p>可能是by design的，只是它的protocol用在WP里不支持。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.fengdingcn.org/blog" rel="nofollow noopener">Ding Feng</a></span><time class="comment-date">2006-07-11 21:53:45</time></div>
  <div class="comment-body"><p>建议赶紧去feedburner烧一个feed，国内的feedsky也行。</p>
<p>省的以后换 feed URL 还烦心通知大家。</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author">Ian Zhou</span><time class="comment-date">2006-11-01 16:39:24</time></div>
  <div class="comment-body"><p>我想从MSN Space上面提取日志，但是getRecentPosts只能返回20篇日志的ID。没有全部ID的列表，如何才能把Space上面的内容提取出来呢？163提供这样的迁移功能，说明应该是有办法的吧？</p></div>
</li>
<li class="comment">
  <div class="comment-meta"><span class="comment-author"><a href="http://www.zhangling.org/" rel="nofollow noopener">Zhang Ling</a></span><time class="comment-date">2006-11-01 18:42:14</time></div>
  <div class="comment-body"><p>建议看一下MSDN的文章： MetaWeblogAPI and MSN Spaces。里面对getRecentPosts方法的描述是支持post数量的，public struct[] metaWeblog.getRecentPosts(string blogid,<br>
string username,<br>
string password,<br>
int numberOfPosts);</p>
<p>我没验证过，你可以试试。</p></div>
</li>
</ol>
</section>
{% endraw %}
