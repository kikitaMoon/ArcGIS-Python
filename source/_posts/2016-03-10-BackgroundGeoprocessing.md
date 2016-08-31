title: 吧啦下 Background Geoprocessing
categories:
- 木工开物
date: 2014-06-25 09:32:12
tags: [Geoprocessing]
---


今天和大家说一下后台地理处理（GP），说到后台，自然会想到前台。

其实在 ArcGIS Desktop 9.X 以及更早的年代，ArcToolbox 中的工具运行的模式只有前台模式，也就是大家熟悉的情景：运行某个工具，然后工具运行窗口挡在 ArcMap的前面，窗口中的Log不停的滚动，直至工具运行完毕，ArcMap 才能使用。 并且，由于 ArcMap 和 ArcCatalog 是 32 的程序，单进程使用的系统资源是有限的。

为了解决这些问题，后台地理处理就产生了，从 ArcGIS 10.0 之后的版本，后台地理处理一直存在着。如果我们现在使用的操作系统是64bit的，那还可以安装后台地理处理64位程序包，在安装光盘中可以找到 ArcGIS for Desktop Background Geoprocessing （64bit）。


![](http://img.blog.csdn.net/20140624161610421?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


<br>

**为什么安装&nbsp;ArcGIS for Desktop Background Geoprocessing（64 位）？**

因为，后台执行一个工具时，在后台会启动一个新的进程，我们可以理解成开了一个新的 ArcMap，只是没有界面的ArcMap。安装 ArcGIS for Desktop—Background Geoprocessing（64 位）之后，就替代了原先的常规 32 位后台处理。在 RAM 容量较大的系统中，使用 64 位后台处理，有助于处理在 32 位环境中无法处理的大数据。由于所有执行工作都在原生 64 位空间中完成，因此可使用更多系统资源。

由于新开进程，所以，在打开 ArcMap 之后的第一次执行后台GP，会发现很慢有延迟，之后的几次会很快出现进度条和消息。实际上，后台处理会启动两个进程，两个 RuntimeLocalServer.exe 进程。在工具执行期间不要随便结束这两个进程，否则可能会导致结果异常。

![](http://img.blog.csdn.net/20140624173114906?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

<br>



**如何选择前台与后台GP处理？**

实际上，如果我们只是在做一些日常的小测试，做些小数据量的处理，可能除了结果之外，响应速度是我们关心的，那还是完全可以选择前台的，毕竟省去了新开进程的时间。但是如果仅仅因为在某些情况下的不稳定放弃后台运行，不是很明智，毕竟后台执行GP可以完全不耽误你手头的工作，还能更好的利用系统的资源。 后台运行从10.0版本开始产生，早期bug缠身，但是随着版本的更新，日趋稳定，10.2之后也开始支持并行运算，后台处理GP还是个不错的选择。

还是需要注意，什么情况下，后台GP不适用？

<br>


**后台64GP不支持的数据类型** 

* 个人地理数据库(.mdb)，Excel表（.xls、.xlsx） 	

<br>


**不在后台运行的工具包括：** 

* 元数据转换工具集（Metadata conversion&nbsp;）中的工具
* 地理数据库管理工具集（Geodatabase administration）中的工具
* 所有 Coverage 工具
* 用于创建包（Packages）的工具
* 绘图工具（Graphing tools）（仅针对 64 位地理处理；这些工具在传统的 32 位后台处理中运行）
* 作者禁用后台处理的自定义脚本、模型或功能工具