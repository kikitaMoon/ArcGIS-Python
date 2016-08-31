title: 了解 ArcScene 与 ArcGlobe 
categories:
  - 木工开物
date: 2012-11-17 12:13:13
tags: [3D]
---

ArcGIS 中，ArcScene 与 ArcGLobe 是两种3D数据可视化以及分析的组件或者说环境，它们二者有什么样的区别，如何根据自己的应用去选择呢？
以下是对这二者的对比信息总结：

# 1. 许可

都需要 3D Analyst License 才能启动。


# 2. 坐标系统

ArcScene - 使用第一个加入ArcScene的数据的坐标系统，当不同坐标系的数据加入时，进行动态投影，这点同ArcMap。通常使用平面坐标系（投影坐标系）。
ArcGlobe - WGS 1984 Cube Projection *，当不同坐标系的数据加入时，进行动态投影。
* 那神马是立方体投影（cube projection）？
也就是将地球投影到各面都是正方形的六面体上。如下图：

![](http://img.my.csdn.net/uploads/201209/20/1348111676_7466.gif)

需要说明，这种投影，经线和纬线都是直线；在纬度 +45° 和 -45° 之间，东南西北方向是准确的，比例尺是正确的；在极面上，由中心确定的方向是真实的。
但是这种投影不适合制图，仅适用于ArcGlobe。


# 3. 内存管理与缓存机制

ArcScene - 将所有数据加载到内存中，必要的时候使用虚拟内存。也因此，ArcScene通常用来展示小场景、小数据量。
ArcGlobe - 通常专用于超大型数据集，缓存过程中会建立索引并将所有数据组织为各个切片和细节层次。


# 4. 数据类型的支持

ArcGlobe支持terrain数据，但是ArcScene不支持。
ArcScene中不支持Annotation。

