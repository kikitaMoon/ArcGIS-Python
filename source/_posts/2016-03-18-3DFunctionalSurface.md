title: 3D分析之Functional Surface工具箱
categories:
- 木工开物
date: 2012-11-18 21:51:59
tags: [3D,Geoprocessing]
---

![](http://img.my.csdn.net/uploads/201211/18/1353207928_5109.png)


# **1. Add Surface Information（添加表面信息）**

向点、线或面要素的属性表添加表面高程信息。

||要素几何||表面属性||
||Point||从表面上点的 XY 坐标插入的点高程。||
||MultiPoint||针对多点记录中所有点得到的点的最小、最大和平均高程。||
||Polyline||沿着表面的线的 3D 距离。从表面上线的路径获得的最小、最大和平均高程和坡度。||
||Polygon||面定义的表面部分的 3D 面积。来自表面的最小、最大和平均高程和坡度。||


# **2. Interpolate shape（插值 Shape）**

根据从栅格、不规则三角网 (TIN)、或 terrain 数据集获取的高程值为要素类插入 z 值。

![](http://img.my.csdn.net/uploads/201211/18/1353208672_8553.gif)


# **3.&nbsp;Intersect 3D Line With Surface（&nbsp;3D线与表面相交）**

计算 3D 线要素与一个或多个表面的几何交集，并以分割线要素和点的形式返回交集。

![](http://img.my.csdn.net/uploads/201211/18/1353208838_7228.png)


# **4.&nbsp;Stack Profile（堆栈剖面）**

创建表格和可选图表，用于说明一个或多个多面体、栅格、TIN 或 terrain 表面上的线要素的剖面。

这个工具可以来制作剖面图。

![](http://img.my.csdn.net/uploads/201211/18/1353208936_2561.png)


表中各个字段的含义：

- FIRST_DIST - 到剖面段中第一个折点的距离。
- FIRST_Z - 剖面段中第一个折点的高度。
- SEC_DIST - 剖面段中第二个折点的距离。
- SEC_Z - 剖面段中第二个折点的高度。
- LINE_ID - 用于定义剖面的线要素的唯一 ID。
- SRC_TYPE - 剖面源的数据类型，是表面或多面体。
- SRC_ID - 要描绘剖面的多面体要素的唯一 ID。不适用于表面输入。
- SRC_NAME - 剖面源的名称和路径。


# **5.&nbsp;Surface Volume（表面体积）**

可计算指定参考平面以上或以下的栅格、不规则三角网 (TIN) 或 terrain 数据集表面的面积和体积。

![](http://img.my.csdn.net/uploads/201211/18/1353209255_4876.gif)