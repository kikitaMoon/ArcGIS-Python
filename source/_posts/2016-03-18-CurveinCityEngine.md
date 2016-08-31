title: 在CityEngine中的圆柱体建模
categories:
  - 木工开物
date: 2013-03-12 17:54:48
tags: [CityEngine,3D]
---
CityEngine中不支持弧段的存储，各种面都是折线面，也就是ArcGIS中的Polygon。

当遇到圆柱体的建筑物或实体时，如何为其建模呢？

![](http://img.my.csdn.net/uploads/201303/12/1363067872_5967.jpg)

![](http://img.my.csdn.net/uploads/201303/12/1363067887_9719.jpg)

考虑到ArcGIS与CityEngine的数据是可以互操作的，那就在ArcGIS中来构建圆形或者弧段，然后将之处理成近似弧段的多边形，然后导入CityEngine来作为模型的底面基础。按照这个思路，来动手做一下。

<br>

# 1. 准备带弧的数据

在ArcGIS Desktop 中准备数据，创建 File GDB，用于存储弧段。可以从空白开始，也可以在现有数据中编辑。

创建圆、椭圆、贝塞尔曲线、圆弧构成的面等等：

![](http://img.my.csdn.net/uploads/201303/12/1363073123_8744.png)

![](http://img.my.csdn.net/uploads/201303/12/1363073161_6984.png)

![](http://img.my.csdn.net/uploads/201303/12/1363073172_9625.png)

![](http://img.my.csdn.net/uploads/201303/12/1363073260_1858.png)

以上图形都处于节点编辑状态，从节点数目我们可以发现，都是以复杂对象存储的。然而这些是CE不能读取的，那么下一步就是转折线了。

<br>

# 2. 弧转折线

使用 ArcToolbox中的工具 Densify 工具来对弧段加密，从而将高级的函数要素对象转为简单的点线面几何。

![](http://img.my.csdn.net/uploads/201303/12/1363073946_2997.png)
	
根据需要设置间距或者偏移等参数，从而控制加密点的生成位置，这里的需要主要是指将来模型的详细程度。

如果需要比较逼真，距离可以相对小一些，这样的节点会更密集些，但是在CE中建模时可能会更耗时，更加占用资源；

如果相对可以粗略些，距离可以设置大些，这样的节点会稀疏些，建立模型会更加快速，但是边界相对不会很平滑。

![](http://img.my.csdn.net/uploads/201303/12/1363074633_1525.png)

![](http://img.my.csdn.net/uploads/201303/12/1363074641_4067.png)

![](http://img.my.csdn.net/uploads/201303/12/1363074621_4013.png)

![](http://img.my.csdn.net/uploads/201303/12/1363074649_7023.png)

<br>

# 3.导入CE，进一步加工

经过简单的拉拔，可以做出简单的类似弧段建筑物。

![](http://img.my.csdn.net/uploads/201303/12/1363079683_1760.png)

到这里，这些类弧段的楼房骨架就有了。

