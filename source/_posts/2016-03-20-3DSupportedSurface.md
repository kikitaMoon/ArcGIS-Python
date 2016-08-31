title: 3D分析之ArcGIS 支持的表面类型
categories:
  - 木工开物
date: 2012-11-17 12:14:13
tags: [3D,Geoprocessing]
---

为了表示连续的表面，ArcGIS 提供了多种表示、存储函数表面的数据格式，主要是以下四类，其中包括10.1带来的新类型：LAS Dataset。

我们可以借助于ArcGIS的3D分析扩展，对这些函数表面数据进行三维的显示、分析等。但是需要注意的是，这些数据并不是真正意义上的真三维，这是我们常说的2.5D。因为这些数据在某个XY坐标对对应的位置上，只能存储一个Z值，而真正的三维实体是在某个位置上有一系列的Z值。这种三维实体，ArcGIS中是以Multipatch存储和表示的。


**1.Raster**

![](http://img.my.csdn.net/uploads/201210/15/1350267554_7479.png)

这是最常见的一种栅格表面数据格式，通常是浮点型的连续栅格。

**2.TIN**

![](http://img.my.csdn.net/uploads/201210/15/1350267567_4448.gif)

**3.LAS Dataset**

![](http://img.my.csdn.net/uploads/201210/15/1350267580_7017.png)

**4.Terrain Dataset**

![](http://img.my.csdn.net/uploads/201210/15/1350267593_1476.gif)


**四种格式，在各种GDB中的支持情况：**

![](http://img.my.csdn.net/uploads/201210/15/1350267492_6753.png)


