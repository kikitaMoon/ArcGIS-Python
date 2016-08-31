title: 我们可能会遇到的距离量算方法
categories:
  - 木工开物
date: 2014-12-25 15:57:46
tags: [Geoprocessing,Spatial Statistics]
---


在看空间统计相关的文档资料的时候，看到了几个有关距离丈量方法的术语词汇，诸如：欧式距离、曼哈顿距离、切比雪夫距离…… 老外习惯于使用名字来命名算法，可是对于门外汉们，是一种困惑，今天就整理下，一起温故知新。 

<br>

# **1. 欧式距离（Euclidean Distance）** 

欧式距离是我们在直角坐标系中最常用的距离量算方法，例如小时候学的“两点之间的最短距离是连接两点的直线距离。”这就是典型的欧式距离量算方法。 

通常这这个距离的获取是基于我们熟悉的“勾股定理”，解算三角形斜边得到的。 

![](http://7xospm.com1.z0.glb.clouddn.com/903d44fd-0d16-4834-9165-2dbfa5068af1_20141224105628950.png) 

![](http://7xospm.com1.z0.glb.clouddn.com/507d3266-3fb1-45a8-9b01-31ed04a03c5f_20141224111231097.png) 

_看看维基百科：[http://en.wikipedia.org/wiki/Euclidean_distance](http://en.wikipedia.org/wiki/Euclidean_distance)_ 


<br>

# **2. 曼哈顿距离（Manhattan Distance）** 

曼哈顿距离是与欧式距离不同的一种丈量方法，两点之间的距离不再是直线距离，而是投影到坐标轴的长度之和。 

        ![](http://7xospm.com1.z0.glb.clouddn.com/1e2f0997-552d-4f94-9fb6-7b075615a9b2_20141225151215828.png) 

还是看图吧，图比文字更显见。 

        ![](http://7xospm.com1.z0.glb.clouddn.com/1d6a5b0d-e8e1-4916-8cb3-20817b85e24f_20141224135416343.png) 

图中绿色的线为欧式距离的丈量长度，红色的线即为曼哈顿距离长度，蓝色和黄色的线是这两点间曼哈顿距离的等价长度。 

想想我们下象棋的时候，车炮兵之类的，是不是要走曼哈顿距离？ 

如果不会下象棋，没关系，看下面的例子： 

![](http://7xospm.com1.z0.glb.clouddn.com/5a932b6c-0b91-4e0d-b7b2-3901a42f7fb4_20141224140558562.png)

   在美国道路会像这样是很多的规则的网格状，从A到B通常无法去沿直线行走，而是会避开建筑物，走几个街区到达。    

图中蓝色的线即为曼哈顿距离的典型应用场景。 

_看看维基百科：[http://en.wikipedia.org/wiki/Taxicab_geometry](http://en.wikipedia.org/wiki/Taxicab_geometry)_ 

<br>

# **3. 切比雪夫距离（Chebyshev distance）** 

数学上，切比雪夫距离是将2个点之间的距离定义为其各坐标数值差的最大值。 

       ![](http://7xospm.com1.z0.glb.clouddn.com/5b836ab3-8f5d-4028-8f9b-7a05f6f60ea0_20141225150924640.png) 

网上搜索，好多有关这个距离的解释，大多都是采用国际象棋中的王的走步来作为例子，王可以前后左右走，还可以斜前斜后走，一共8个方向可以认为距离均等。 

也就是在下面3&amp;times;3邻域内，中心网格的中心点到8个邻域网格中心点的距离相等。 

      ![](http://7xospm.com1.z0.glb.clouddn.com/dc5d6004-2e66-40ca-838d-abe5136637a7_20141225150721218.png) 

_看看维基百科：[http://en.wikipedia.org/wiki/Chebyshev_distance](http://en.wikipedia.org/wiki/Chebyshev_distance)_    