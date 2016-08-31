title: 羽化效果的HeatMap
categories:
  - 木工开物
date: 2015-06-09 11:07:58
tags: [Mapping,ArcGIS Pro]
---
用采样点制作热力图是个非常常见的需求。热力图可以给地图的阅读者直观的信息，下面就看看如何在 ArcGIS Pro 中做一个漂亮的HeatMap。

<br>

# 1.

准备好采样点数据，当然是量大更优。我这里用了全球地震点数据，大约有 21W+ 的数据量。像这一类的数据可以从一些提供公开数据的网站获取，例如 [USGS](http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php) 。


![](http://img.blog.csdn.net/20150608105255424)

<br>

<br>

# 2.

使用 ArcGIS 中的密度分析工具可以从点数据直接生成密度栅格，工具位于 ArcToolbox —— Spatial Analyst —— Density 工具集下。这里我采用了 Kernel Density 。

![](http://img.blog.csdn.net/20150608141704212)


<br>

<br>

# 3.

制作一个自己喜欢的热力色带，最边缘的颜色使用透明色，这样就有“羽化”的效果。

![](http://img.blog.csdn.net/20150608142932524)

应用色带之后：

![](http://img.blog.csdn.net/20150608143314185)


<br>

如有需要，可以进一步为图层设置透明：

![](http://img.blog.csdn.net/20150609110455795)


