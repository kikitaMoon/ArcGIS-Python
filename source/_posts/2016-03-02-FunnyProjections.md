title: 你所不知的有趣投影方法

date: 2016-02-04 13:00:00

tags: [Coordinate System,Mapping]

categories: 木工开物


---



[高斯克吕格/Gauss Kruger](http://baike.baidu.com/view/311590.htm)、[兰伯特/Lambert](http://baike.baidu.com/view/1351534.htm)、[墨卡托/Mercator](http://baike.baidu.com/view/301981.htm)……这些是业内人士耳熟能详的 [投影方法](http://desktop.arcgis.com/en/arcmap/latest/map/projections/what-are-map-projections.htm)，它们各有适用场景以确保投影后某类或某几类变形最小，其最终要义就是最大程度地精确表示位置。然而，这一篇中不是对这些投影方法进行阐述，而是传递一些新奇特的投影玩法。

ArcGIS中提供了众多的坐标系统定义信息，有些 [投影坐标系](http://desktop.arcgis.com/en/arcmap/latest/map/projections/list-of-supported-map-projections.htm)一直静静存在，只是没有被关注，今天我们一起翻几个牌子。

<br>

准备示例数据，世界大洲及格网数据，当前是地理坐标系 WGS1984，首次拖拽到 ArcMap看起来是我们最熟悉的这个样子：

![](http://img.blog.csdn.net/20160203115028046)

下面我们变换不同的投影方法，看看世界发生了什么变化。

<br>
<br>

# 埃托夫投影/Aitoff projection

将世界投影到**长短轴为2：1的椭圆**上，有关这个投影方法的说明，戳 [**这里**](http://desktop.arcgis.com/zh-cn/desktop/latest/guide-books/map-projections/aitoff.htm)。

![](http://img.blog.csdn.net/20160204100735323)

<br>

# 等距方位投影/Azimuthal equidistant projection

这是一种**平面投影**，由纬度和经度确定的一个点作为平面与椭球的切点，详情戳 [这里](http://desktop.arcgis.com/zh-cn/desktop/latest/guide-books/map-projections/azimuthal-equidistant.htm)。

**当切点是本初子午线和赤道交点时**，我们看到的世界是这样，大陆好像散开的拼图：

![](http://img.blog.csdn.net/20160204102008292)

**当以北极为切点时**，我们看到的世界是这样：

![](http://img.blog.csdn.net/20160204102435150)

为什么有种莫名的熟悉感？联合国的Logo是这样吧，灵感来自这里：

![](http://img.blog.csdn.net/20160204102544166)


<br>

# 柏哥斯星状投影/Berghaus Star Projection

这种投影方法很有趣，让人一见倾心。此方法通常中心在北极，是对中央半球使用等距方位投影，而地球的另一半被分割为五个三角形，从而形成了一个围绕圆心的星形。详情戳 [这里](http://desktop.arcgis.com/zh-cn/desktop/latest/guide-books/map-projections/berghaus-star.htm)。

![](http://img.blog.csdn.net/20160204103811171)

这种投影方法被 [美国地理学家协会(AGG)](http://www.aag.org/) 采用作为 Logo。

![](http://img.blog.csdn.net/20160204104028616)

<br>

# 彭纳投影/Bonne Projection

这个投影方法，博主同样喜欢。伪圆锥投影，所有的纬线为同心圆弧，并且投影变换后是个大大的心形。

喜欢研究算法的同学，戳[这里](https://en.wikipedia.org/wiki/Bonne_projection)看公式。

![](http://img.blog.csdn.net/20160204104631674)


<br>

# 温克尔三重投影/Winkel tripel projection

这可能是我们最常见的世界地图挂图的一种投影方法，详情戳[这里](http://desktop.arcgis.com/zh-cn/desktop/latest/guide-books/map-projections/winkel-tripel.htm)。

![](http://img.blog.csdn.net/20160204105327787)


![](http://img.blog.csdn.net/20160204105538334)


<br>

# 古蒂等面积投影/Goode homolosine projection

这种投影方法最小化整个地球的变形，是一种不连续的伪圆柱等积投影，详情戳[这里](http://desktop.arcgis.com/zh-cn/desktop/latest/guide-books/map-projections/goodes-homolosine.htm)，还有[这里](https://en.wikipedia.org/wiki/Goode_homolosine_projection)。

这种投影方法有两个版本，大陆和海洋。

Land:
![](http://img.blog.csdn.net/20160204110539288)


Ocean:
![](http://img.blog.csdn.net/20160204110548713)


<br>

# “上帝视角”/The World From Space

最后说一种 ArcGIS 自带的命名为 “The_World_From_Space” 的平面坐标系（WKID: 102038），使用了正射投影（Orthographic Projection）方法。投影变换后，像是在太空遥看这个蓝色星球。

![](http://img.blog.csdn.net/20160204111434263)

这个坐标系的默认参数是 Longitude_Of_Center: -72.5333333334；Latitude_Of_Center: 42.5333333333，因此北美大陆位居中央。

![](http://img.blog.csdn.net/20160204111650287)

修改下参数，调整下切点位置，把我们心中美丽的中国转过来~

![](http://img.blog.csdn.net/20160204114444479)


<br>

投影变换是不是也挺有意思的？ 让我们真正发现了“数学之美”。春节临近，祝大家新春愉快喽！