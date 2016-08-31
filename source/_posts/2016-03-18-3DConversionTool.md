title: 3D分析之常用转换工具
categories:
  - 木工开物
date: 2012-11-21 11:49:04
tags: [3D,Geoprocessing]
---
![](http://img.my.csdn.net/uploads/201211/20/1353395828_6620.png)

三维分析工具箱中，Conversion工具集为我们提供了很多用于格式转换的工具，其中有几个能为我们解决很多常见问题，这里整理下：


# **1. 各种数据格式的3D模型导入到ArcGIS中展示**

使用 Import 3D file 工具，ArcGIS 主要支持以下 3D模型的导入：

 - 3D Studio Max (*.3ds)
 - SketchUp (*.skp)
 - VRML and GeoVRML (*.wrl)
 - OpenFlight (*.flt)
 - COLLADA (*.dae).

将数据导入为ArcGIS的 Multipatch（多面体）要素类，可以选择 shapefile 和 Geodatabase 来存储。

这里需要注意：shapefile multipatch 是不能存储纹理的，如果需要保存纹理，要选择 GDB multipatch feature class。

<br>

# **2. 需要得到 Multipatch 的 2D 轮廓线**

使用 Multipatch Footprint 工具

![](http://img.my.csdn.net/uploads/201211/20/1353403645_1891.gif)

<br>

# **3. 获得栅格数据三维边界线/面**

使用 Raster Domain 工具

![](http://img.my.csdn.net/uploads/201211/20/1353403802_9824.gif)

<br>

# **4. 使用点数据和现有模型制作场景**

常常有这样的应用场景：手头有采集的兴趣点数据，并且有现成的3DS、Skp等等诸多模型，需要将这些模型放置在正确地理位置，并将它们统一存入GDB中进行维护。我们可以这样来做：

（1） 在ArcScene或者ArcGlobe中添加点图层.

（2）双击图层符号，弹出【符号选择器】窗口，点击【编辑符号】。

![](http://img.my.csdn.net/uploads/201211/21/1353459602_7940.png)

（3）在弹出的【符号属性编辑器】中，类型下拉列表中选择【3D Marker Symbol】，并在之后的窗口中选择模型的路径。

![](http://img.my.csdn.net/uploads/201211/21/1353460413_1919.png)

（4）上步中，根据需要分门别类的给每类点配以不同的模型，最后得到丰富的3D模型组成的场景。

![](http://img.my.csdn.net/uploads/201211/21/1353467736_5976.png)

（5） 使用工具：**&nbsp;Layer 3D to Feature Class，**将模型统一转入GDB，集中存储和维护。原来的模型细节及纹理得到很好的保留。

![](http://img.my.csdn.net/uploads/201211/21/1353470343_8027.png)


