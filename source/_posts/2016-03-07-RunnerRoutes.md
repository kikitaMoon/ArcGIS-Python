title: 为Runner做一张有质感的图
categories:
  - 木工开物
date: 2015-06-05 10:52:33
tags: [Mapping,ArcGIS Pro]
---
如今，通过 GPS 我们可以轻松采集到自己的足迹，Runner们用各种手机App记录跑步路线也再平常不过。如果我们有大量的足迹信息，也可以试试 ArcGIS Pro 的渲染能力，来看看自己的 Favourite 线路如何分布。

<br>

我在 ArcGIS Online 上 down 到了某位 Runner 的足迹信息，当然大家也可以用自己的，gpx，txt，kml 等常见的 GPS Tracklog 文件都是可以直接导入成为 ArcGIS 支持的格式。根据文件格式的不同，你可能会需要 GPX to Feature ， Add XY Event layer， KML to Layer ，Points to Line 等这些工具的辅助，得到路线数据，表示路线的线数据当然越多越好。

<br>




ArcGIS Pro 的符号化中增加了符号的透明效果，这一点完胜 ArcMap 的渲染效果。你想问ArcMap什么效果？如下，好像有点惨不忍睹：

![](http://img.blog.csdn.net/20150605104227988)



<br>



由于ArcGIS Pro 中的新增的符号透明不是图层的整体透明，而是每个Feature的符号透明，就会产生色彩叠加的效果。直观上说，就是符号叠加越密集的位置，色彩会越深，给人以渐变色彩的热力图的感受。




<br>

#**怎么做？**

<br>

##**1.**
加入数据，GPS路线数据和深灰色主题的底图服务。

![](http://img.blog.csdn.net/20150605095942898)


<br>

##**2.** 

选个喜欢的颜色，并进入 more。

![](http://img.blog.csdn.net/20150605100740196)


<br>



##**3.** 

设置个透明百分比。

![](http://img.blog.csdn.net/20150605094759196)

<br>


##**4.** 

Done !

![](http://img.blog.csdn.net/20150605093131933)


<br>
无需任何高级的分析，所见即所得。相比周围，明显这条路是这位 Runner 最经常挥洒汗水的一条……

![](http://img.blog.csdn.net/20150605105103092)


<br>



