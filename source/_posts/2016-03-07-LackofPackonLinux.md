title: 解决Linux系统中缺少Xvfb包的问题
categories:
  - 木工开物
date: 2015-05-08 21:19:05
tags: [Linux,Deployment]
---

上一篇文中写了在 Linux上安装 ArcGIS Server前的准备工作，最后一步是环境检测，只有所有项都通过才可以安装 ArcGIS Server。

不幸的是，第一次其实没有通过环境监测，提示系统中缺少了Xvfb包，具体的检测结果如下：

![](http://img.blog.csdn.net/20150508210646386)


检测报告中提示了解决方法，参考技术文章 [40860](http://support.esri.com/en/knowledgebase/techarticles/detail/40860)：

但是这篇文章只告诉我们缺包了，需要安装一个Xvfb包，没有说明包的获取与安装过程等，下面我就bala一下喽。


<br>
<br>

# 1 . 下载Xvfb包到主机 


用 **wget** 命令下载xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm包到主机。


>**wget http://vault.centos.org/6.2/os/x86_64/Packages/xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm**



![](http://img.blog.csdn.net/20150508210738597)


<br>
<br>

# 2 .  运行安装Xvfb包


>**yum localinstall xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm**


![](http://img.blog.csdn.net/20150508211626954)


<br>
<br>

# 3 . 执行环境检测

所有检测通过即可安装 ArcGIS Server 程序：

![](http://img.blog.csdn.net/20150508174345432)


