title: 查看端口号占用情况
categories:
- 木工开物
date: 2013-06-03 17:35:07
tags: [License]
---

# **1.查看端口占用情况**



使用命令 <span style="color:#cc0000">**netstat -ano** ，检查所有在使用的端口。

![](http://img.blog.csdn.net/20130603164449984)



如果查询指定端口，使用：<span style="color:#cc0000">**netstat -aon|findstr &quot;Port No.&quot;**，如下：

例如，查看49506端口号对应的进程，进程号976：

![](http://img.blog.csdn.net/20130603164957218)




# **2. 查看PID 对应的程序**



查看具体哪个程序在占用某个端口，使用命令：

`netstat -aon|findstr "Port No."`


接着上面的例子，976对应的程序。

![](http://img.blog.csdn.net/20130603170740843)


好了，找到他了，可以换端口号，可以杀掉当前进程，随你……


<br>


**PS：**

在输命令时，可能会遇到报错：“nestat -ano不是内部或外部命令……blabla……”

需要查看下&nbsp;C:\Windows\System32 下是否有 **netstat.exe**。

如果有，再检查下环境变量中**Path**项中有没有这项：**C:\Windows\System32** ,没有的话就添加上。

![](http://img.blog.csdn.net/20130603173425515)

