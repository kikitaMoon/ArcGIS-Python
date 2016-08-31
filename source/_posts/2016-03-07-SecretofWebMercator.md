title: Web Mercator 公开的小秘密
categories:
  - 木工开物
date: 2015-05-29 09:44:56
tags: [Coordinate System]
---
网上已经有好多作者都不吝笔墨，写了好多有关 Web Mercator这个坐标系的前世今生。多搜罗多摄入，我们会得到很多有用的信息。今天讨论到 3758，3857，102100，900913…… 这些ID又一石激起千层浪，看来整理总结下还是有点必要。


<br>

# Web Mercator 如何定义？



<br>

 我们知道，地理数据的坐标系一般有两大类，一是地理坐标系(GCS)，是经纬度单位的椭球坐标系；二是投影坐标系(PCS)，是平面直角坐标系。

投影坐标系（PCS）的定义一般会包含两方面的定义信息：
（1）基准面/Datum — 与GCS相应
（2）投影方法/Projection Method

<br>

## 1

**Web Mercator 是一个投影坐标系统，其基准面是 WGS 1984 。**


<br>


那么，第一个问题，*WGS 1984 是什么？*

“ 世界大地坐标系是美国国防部制图局（Defence Mapping Agency， DMA）为统一世界大地坐标系统，实现全球测量标准的一致性，定义用于制图、大地、导航的坐标基准。它包括标准地球坐标框架、用于处理原始观测数据的标准椭球参考面（即基准和参考椭球）和定义标准海平面的重力等势面（大地水准面）。……”（摘自《大地坐标系统及其应用》）

在上面一段中可以知道，定义一个坐标系绝对是一个复杂浩大的数学工程。 我们经常听说的 WGS 1984 （或 WGS 84）就是其中一个世界大地坐标系统。我们经常使用的 GPS 的坐标参考系统也是它。

WGS 1984 的具体定义参数：

> GCS_WGS_1984
> WKID: 4326 Authority: EPSG
> 
> Angular Unit: Degree (0.0174532925199433)
> Prime Meridian: Greenwich (0.0)
> Datum: D_WGS_1984
>   Spheroid: WGS_1984
>     Semimajor Axis: 6378137.0
>     Semiminor Axis: 6356752.314245179
>     Inverse Flattening: 298.257223563

通过参数描述，我们知道 WGS 1984 是一个长半轴(a)为6378137，短半轴（b）为6356752.314245179 的椭球体，扁率(f)为298.257223563，f=(a-b)/a 。


![这里写图片描述](http://img.blog.csdn.net/20150528211737974)



<br>



## 2



**Web Mercator 坐标系使用的投影方法不是严格意义的墨卡托投影，而是一个被 EPSG（European Petroleum Survey Group）称为**伪墨卡托**的投影方法，这个伪墨卡托投影方法的大名是 Popular Visualization Pseudo Mercator，PVPM。** 看起来就觉得这个投影方法不是很严谨的样子，大众化的？受欢迎的？可视化伪墨卡托投影……


因为这个坐标系统是 Google Map 最先使用的，或者更确切地说，是Google 最先发明的。在投影过程中，将表示地球的参考椭球体近似的作为正球体处理（正球体半径 R = 椭球体半长轴 a）。这也是为什么在 ArcGIS 中我们经常看到这个坐标系叫 **WGS 1984 Web Mercator (Auxiliary Sphere)**。Auxiliary Sphere 就是在告知你，这个坐标在投影过程中，将椭球体近似为正球体做投影变换，虽然基准面是WGS 1984 椭球面。

![这里写图片描述](http://img.blog.csdn.net/20150528211907842)


后来，Web Mercator 在 Web 地图领域被广泛使用，这个坐标系就名声大噪。尽管这个坐标系由于精度问题一度不被GIS专业人士接受，但最终 EPSG 还是给了 WKID:3857。

下面放一张在 EPSG 官网上找到的3857坐标的具体参数介绍，供参考：

![这里写图片描述](http://img.blog.csdn.net/20150528180842720)


<br>

<br>


#  Web Mercator 的阴暗面


<br>

Web Mercator 无论是来自Google程序员的谬误，还是为了简化换算的有意为之，现在它都已经名正言顺的成为了 Web 底图的最受欢迎平面坐标系。

问题又来了，**为什么这么受欢迎的坐标系还会受到GIS大咖的诟病？**

拒绝给这个坐标系分配 坐标系ID 的原话是这样的：

**“** The projected coordinate reference system originally lacked an official spatial reference identifier (SRID), and the Geodesy subcommittee of the OGP's Geomatics committee (also known as EPSG) refused to provide it with one, declaring "We have reviewed the coordinate reference system used by Microsoft, Google, etc. and believe that it is technically flawed. We will not devalue the EPSG dataset by including such inappropriate geodesy and cartography."  **”**

这不是EPSG 冷酷无情无理取闹，从技术角度看是有原因的。简而言之，主要原因在于基准面被篡改后，本来是等角投影的Mercator坐标变换算法，不再等角了，而是近似等角，也就是出现角度变形。这种变形势必影响了坐标的精度，如下是某位GIS专家给出的概要说明（闪亮的最后一条）：

![这里写图片描述](http://img.blog.csdn.net/20150528231421817)


如果你想进一步关心细节，想知道这位专家对 Web Mercator 的 dark side 的深入见解，点[这里](http://hydrometronics.com/downloads/Web%20Mercator%20-%20Non-Conformal,%20Non-Mercator%20%28notes%29.pdf)看看。


<br>


<br>

# 不再混乱的 ID


<br>

也是由于GIS专业人士的质疑，这个坐标系的ID经历了曲折的过程，好多做Web开发的朋友都感到困惑。简单地顺一下：

**OpenLayers:900913**     由于得不到官方的认证ID，Google为Web Mercator 任性地制定了这个ID，自娱自乐，也祝大家玩的开心……下面可不是我编的。

>i think 900913 is great.
9-g
0-o
0-o
9-g
1-l
3-e
get it? 900913 is equal to google. THAT’S AMAZING ! =-)

**EPSG:3785**  这是 EPSG 在 2008 年给 Web Mercator 设立的WKID，但是这个坐标系的基准面是正圆球，不是WGS 1984。 存在了一段时间后被弃用。

**EPSG:3857**  EPSG为 Web Wercator 最终设立的WKID，也就是现在我们常用的Web 地图的坐标系，并且给定官方命名 "**WGS 84 / Pseudo-Mercator**"。

**ESRI:102113**   Esri内部使用ID，与 EPSG:3785 相应。已被弃用。

**ESRI:102100**   Esri内部使用ID，与 EPSG:3857 相应。

因此，细心地话，会发现在 ArcGIS Server 的REST 服务页面中，Web Mercator 的空间参考会记做： **102100(3857)**

![这里写图片描述](http://img.blog.csdn.net/20150528234841686)

<br>

<br>

<br>

这些东西其实一直都是公开的，博主没有生产这些小秘密，只是小秘密的搬运工。

<br>

我把自己看过的资源放在下面，共享之，文中提到的已经做链接了地，下面就不重复列举：

http://en.wikipedia.org/wiki/Web_Mercator

http://blogs.esri.com/esri/arcgis/2014/09/25/what-does-the-nga-web-mercator-advisory-mean-for-esri-defense-and-intelligence-users/

http://blogs.esri.com/esri/arcgis/2012/03/05/mercators-500th-birthday/

http://www.sharpgis.net/post/2008/05/15/SphericalWeb-Mercator-EPSG-code-3785

http://crschmidt.net/blog/archives/243/google-projection-900913/

http://forums.esri.com/Thread.asp?c=93&f=984&t=288607

