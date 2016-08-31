title: ArcGIS 系统要求知多少
categories:
  - 木工开物
date: 2014-09-24 10:23:18
tags: [Deployment]
---
安装 ArcGIS 软件之前，一定要注意自己的操作系统，硬件（包括型号和驱动），甚至一些软件的版本是否能满足系统要求。只有出现在各个版本的列表中的操作系统和其他软硬件版本才算是真正的支持。否则可能会出现诸如不稳定，崩溃等等各种异常现象。

时常会被问到：“ArcGIS 9.3还能安装在 Windows XP SP1 中吗？ArcGIS 10.0能安装在 windows 8 中吗？”答案都是不能。但是前者安装时系统会主动报错，不支持安装，后者貌似没有任何提示，也安装上了。用户就会问，你不是说安装不上米？

“能不能安装”在官方和“民间”，是两个完全不同层面的问题。为什么这么说呢？我们一起脑补下。从个人学习角度，只要安装成功，没有收到致命报错，似乎就是支持安装；但是，从官方角度，我们可以理解成，这个操作系统的发布和ArcGIS某个版本软件开发测试不是同期的，例如10.0早在2010年就发布了，而win8在2013年才发布，没有经过严格测试证明可以全面支持的，不能称为支持。因此如果强行安装了，出于个人研究探索并无大碍，但只能后果自负了。

下面是各个版本的系统要求列表：

**ArcGIS 10.0**

[http://help.arcgis.com/en/systemrequirements/index.html](http://help.arcgis.com/en/systemrequirements/index.html)

**ArcGIS 10.1**

[http://resources.arcgis.com/en/help/system-requirements/10.1/index.html](http://resources.arcgis.com/en/help/system-requirements/10.1/index.html)

**ArcGIS 10.2.x**

[http://resources.arcgis.com/en/help/system-requirements/10.2/index.html](http://resources.arcgis.com/en/help/system-requirements/10.2/index.html)

***过气版本 ArcGIS 9.3***

Desktop：http://downloads.esri.com/support/systemrequirements/ArcGIS_Desktop_93_SystemRequirements.pdf

Server：http://downloads.esri.com/support/systemrequirements/arcgis_server.pdf


<br>

<br>


ArcGIS 9.2 甚至更早的版本就不说了，太久远了，现在的操作系统没有几个能支持的了，如果还在使用这8年前的版本，算了，丢了吧，反正你不爱ArcGIS。


以前整理过各个版本的补丁下载链接，[**点击**](http://blog.csdn.net/kikitamoon/article/details/8989539) 跳转另一篇博客。


另外，从10.2版本之后，不再提供像上面链接中一样的单独的补丁下载，而是做成完整的安装包，例如，截至到这篇博客的时间，最新的版本 10.2.1，10.2.2 这些版本既是如此。这样就可以在空白机器上直接安装最新版本，而不需要像以前一样，先安装旧版本再打补丁，避免重复劳动多次；对于已经安装10.1，10.2的机器，可以直接覆盖安装 10.2.1等新版本，也节省了卸载的时间。

产品的生命周期最可以说明问题，有图有真相：

![](http://img.blog.csdn.net/20140924102033625?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)