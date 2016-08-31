title: 要素外接矩形的四个角点坐标、长度、宽度、面积如何计算到要素属性表中?
categories:
  - 木工开物
date: 2013-05-21 11:48:38
tags: [Geoprocessing,Python]
---


title: 要素外接矩形的四个角点坐标、长度、宽度、面积如何计算到要素属性表中？

使用工具 **Calculate Field**。

![](http://img.blog.csdn.net/20130521114737149)

9.3以上版本可按下图的方法分别求出envelope的x、y坐标的最大、最小值，由此可得出你要的那些值，需注意的的是求长度、面积等要在投影坐标系下进行。

**X的最大值：`!shape.extent.XMax!`**

**X的最小值：`!shape.extent.XMin!`**

**Y的最大值：`!shape.extent.YMax!`**

**Y的最大值：`!shape.extent.YMin!`**

**面积：`!shape.area!`**

**周长：`!shape.length!`**


![](http://img.blog.csdn.net/20130702154802796?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

