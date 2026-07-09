---
layout: post
title: "Eclipse Refactoring API"
date: 2005-12-17 14:31:00 +0800
permalink: /20051217/eclipse-refactoring-api.html
wp_id: 296
wp_slug: "eclipse-refactoring-api"
has_comments: false
---
{% raw %}
<div class="e-content">
<p>这个星期花了四天时间用Refactoring API写重构插件。Eclipse Refactoring API从2.0的internal class过渡到3.0开放class，结合JDT AST语法树，可以实现强大的代码操纵功能。基于JFace的RefactoringWizard可以方便的生成重构向导和代码比较预览。</p>
<p>如果文档和资料足够齐全的话，最多2天就能写完了，可以省掉2天连蒙带猜额外了解API和调用方式的时间。</p>
<p>下面是迄今我能在网上找到的几篇Eclipse JDT AST和Refactoring具参考价值的文章，都是IBM developerWorks上的：</p>
<p>1. <a href="http://www-128.ibm.com/developerworks/opensource/library/os-ecjdt/">Extend Eclipse's Java Development Tools</a></p>
<p>2. <a href="http://www-128.ibm.com/developerworks/opensource/library/os-ast/?ca=dgr-lnxw97ASTParser">Exploring Eclipse's ASTParser</a></p>
<p>3. <a href="http://www-128.ibm.com/developerworks/cn/java/j-refactor/">在Eclipse中创建新的重构功能</a></p>
<p>第三篇是CSDL北京同事写的，很不错的文章。现在市面上Eclipse的书这么多，真正能帮助解决问题，尤其是中、高级问题的，太少了。</p>
</div>
{% endraw %}
<!--more-->
