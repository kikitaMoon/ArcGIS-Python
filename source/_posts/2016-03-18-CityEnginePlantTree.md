title: 【CityEngine】如何在街道两侧放置路灯、行树等
categories:
  - 木工开物
date: 2013-04-17 10:23:08
tags: [CityEngine,3D]
---
使用CGA代码将对象（路灯、树木等）放置到路边。这里用到的主要方法就是Split 函数去做分割。

思路是，现将shape按照较短的轴向进行最初的分割剥离，得到路的两边sidewalk，然后将这些分割出来的形状进行再次分割，也就是沿着长的轴的方向分割成多个重复的小的形状，最后，用实际的模型（如路灯或树等）替换这些小块。

<br>

下面是示例代码，参考下：

```
[plain] view plain copy
Sidewalk -->  
    SidewalkGeometry.  
    SidewalkObjects     # 复制shape!  
  
# 思路：沿着道路的方向纵向切割道路，得到两边的人行道。  
# 在剩下的shape“dot”中，插入树木、路灯等静态模型对象。  
      
attr placementWidth = 0.05  
  
attr streetDist = 0.2  
attr objectDist = 5  
  
attr objectSize = 0.1  
attr objectHeigt = 2  
  
SidewalkObjects -->  
    # 沿道路纵向分割两边的人行道。  
    split(v,unitSpace,0) { streetDist : NIL | placementWidth : PlacementStrip | ~1 : NIL  }  
      
      
PlacementStrip -->  
    # 沿着人行道分割横向切割，切成小段。  
    split(u,unitSpace,0) {objectDist: NIL | placementWidth : PlacementPoint }*  
  
PlacementPoint -->  
    alignScopeToGeometry(yUp, 0) # align the shape to the current point shape, thus the street direction!  
    # r(0,90,0) # 旋转90度，视情况使用，例如路灯模型。  
    s(objectSize*2, objectHeigt, objectSize)  
    i("builtin:cube")  
    center(xz)  
```


效果示例：

![](http://img.my.csdn.net/uploads/201304/17/1366169977_1647.jpg)

