title: Maplex中，设置面要素标注锚点位置

categories:
  - 木工开物

date: 2012-02-07 13:54:00
tags: [Mapping]

---


开启Maplex标注引擎后，面要素的标注选项中有一项叫做Anchor Point，用来设置带有背景牵引线的标注的放置位置。

![](http://hi.csdn.net/attachment/201202/7/0_13285941539YrH.gif)

一共提供了四种放置位置，一起来了解下区别在哪里。

![](http://hi.csdn.net/attachment/201202/7/0_13285941574un6.gif)

1. 几何中心(然后轮廓线上最近点)   Geometric center (then closest point on outline)

这里的几何中心是指面的重心。注意：重心并不一定都处于图形的内部。所以尝试先放置要素几何中心，如果几何中心在外部无法放置，则放置到最近的轮廓线上一点。
  
2. 侵蚀中心   Eroded center (always within polygon)

向内“缩小”面，收紧到最后，得到中心点，类似剥洋葱，这个点一定位于面内部。

3.  多边形轮廓线上的最近点 Closest point on the polygon outline

锚点将放置在多边形轮廓线上距离标注最接近的点。

4.  未裁剪多边形的几何中心(然后侵蚀中心)   Geometric center of unclipped polygon (then eroded center)

先尝试忽略中间“洞”的多边形的几何中心，不行再放到侵蚀中心。
    
下图作为这几个中心的比较：

![](http://hi.csdn.net/attachment/201202/7/0_132859416386Z5.gif)

其实，如果嫌麻烦，把Placement选项设置好也可以满足大部分需求。

