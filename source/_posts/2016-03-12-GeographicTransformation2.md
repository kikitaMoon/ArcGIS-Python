title: ArcGIS中的地理坐标系转换方法参数（二）
categories:
- 木工开物
date: 2014-01-19 10:37:38
tags: [Coordinate System]
---
<span style="font-size:12px">&nbsp; &nbsp; 上篇博客说的是 Project 工具中 Geographic Transformation 参数什么情况下是必填的。</span>

<span style="font-size:12px">&nbsp; &nbsp; &nbsp;另外，Project 是矢量数据的坐标系变换工具，如果数据源是栅格数据，需要使用 Project Rater 工具。</span>

<span style="font-size:12px">&nbsp; &nbsp; &nbsp;这篇博客主要写一下，有关自定义地理变换方法。</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">&nbsp; &nbsp; &nbsp;ArcGIS 中提供地理变换方法主要有这几种：Geocentric_Translation、Molodensky、Molodensky_Abridged、Position_Vector、Coordinate_Frame、Molodensky_Badekas、NADCON、HARN、NTV2、Longitude_Rotation、Unit_Change 和 Geographic_2D_Offset。可使用“创建自定义地理变换（Creat Custom Geographic Transformation）”工具来创建转换方法。地理坐标系包含了基于椭圆体的基准面，因此地理变换会更改基础椭圆体。在基准面间进行变换的方法很多，这些方法具有不同的精度和范围。</span>

<span style="font-size:12px">&nbsp; &nbsp; &nbsp;地理变换是针对地理坐标系的，也就是经纬度坐标进行转换，如果输入数据的坐标系中还包含了平面坐标系（投影），在使用 Project 工具的过程中会自动做相应的投影变换，转到地理坐标系，地理变换后，如果需要再转为相应的投影坐标系。</span>

![](http://img.blog.csdn.net/20140119093112281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

<span style="font-size:12px">

</span>

<span style="font-size:12px; color:#cc0000">**PS：**</span><span style="font-size:12px">**<span style="color:#cc0000">&nbsp;</span>** &nbsp; 所有的自定义地理变换文件都将存储为扩展名为 .gtf 的文件，并存储在用户 Application Data 文件夹下的 ESRI\&lt;ArcGIS product&gt;\ArcToolbox\CustomTransformations 文件夹中。自定义变换文件不能进行编辑。它们为二进制文件，用来储存版本和字符串长度信息，如果在ArcGIS之外进行自行编辑，可能会被损坏。</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">下面我们来看看常用的转换方法吧，帮助中有介绍，我下面来个精简整理版的：</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">**_<span style="color:#3333ff">1）<span style="font-size:12px">Geocentric_Translation</span></span>_**</span>

<span style="font-size:12px"><span style="font-size:12px">地心变换，也就是我们常说的**三参数变换**，是最简单的基准面变换方法。地心变换在 XYZ 或 3D 直角坐标系中对两个基准面间的差异情况进行建模。定义一个基准面使其中心为 0,0,0。相距一定距离定义另一个基准面（dx,dy,dz 或 ΔX,ΔY,ΔZ，单位为米）。</span></span>

<span style="font-size:12px"><span style="font-size:12px">&nbsp; **<span style="color:#009900">图示</span>**</span></span><span style="font-size:12px"><span style="color:#009900">：</span></span><span style="font-size:12px">&nbsp; &nbsp;</span>![](http://img.blog.csdn.net/20140119095634937)<span style="font-size:12px">&nbsp;&nbsp;</span><span style="font-size:12px"><span style="color:#009900"> 方程：</span></span><span style="font-size:12px">&nbsp;</span>![](http://img.blog.csdn.net/20140119095643953)

<span style="font-size:12px">

</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">_<span style="color:#3333ff">**2）Coordinate Frame，Position&nbsp;Vector**</span>_</span>

<span style="font-size:12px">这两种方法是我们常说的七参数变换，或者布尔沙模型。通过对三参数变换再增加四个参数可实现更复杂和精确的基准面变换。七个参数是指三个线性平移量 (dx,dy,dz)、绕各轴的三个角度旋转值 (rx,ry,rz) 和一个比例尺因子。旋转值以十进制秒为单位给定，而比例尺因子采用百万分率 (ppm)。</span>

<span style="font-size:12px"><span style="font-size:12px"><span style="font-size:12px">&nbsp;**<span style="color:#009900">图示</span>**</span><span style="font-size:12px"><span style="color:#009900">：</span></span><span style="font-size:12px">&nbsp;</span>![](http://img.blog.csdn.net/20140119100747546)&nbsp; &nbsp; &nbsp;<span style="font-size:12px"><span style="color:#009900">**&nbsp;方程：![](http://img.blog.csdn.net/20140119100835046)**</span></span>

</span></span>

<span style="font-size:12px">为什么七参数有上面两种方法？其实可以认为是一种模型，只是不同的国家对旋转量的正负号定义标准不同而已。</span>

<span style="font-size:12px"></span>

*   坐标框架旋转变换（coordinate frame），美国和澳大利亚的定义，逆时针旋转为正；
*   位置矢量变换（position vector），欧洲的定义，逆时针旋转为负。

<span style="font-size:12px">另外，**<span style="color:#3333ff">_莫洛金斯基–巴德卡斯（Molodensky_Badekas）_</span>**方法是七参数方法的变型。它具有三个附加参数，用于定义旋转点的 XYZ 原点。</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px"><span style="color:#3333ff">**_3）Molodensky，Molodensky_Abridged_**</span></span>

<span style="font-size:12px"><span style="font-size:12px">莫洛金斯基方法直接在两种地理坐标系之间转换，实际上无需转换到 XYZ 系统。莫洛金斯基方法需要三个平移量 (dx,dy,dz) 以及两个旋转椭球体的长半轴 (Δa) 和扁率 (Δf) 的差。

</span></span>

<span style="font-size:12px"><span style="font-size:12px">这种方法，相对用的少，方程我就不粘了，详见帮助：</span></span>

<span style="font-size:12px"><span style="font-size:12px">[http://resources.arcgis.com/en/help/main/10.2/index.html#/na/003r00000012000000/](http://resources.arcgis.com/en/help/main/10.2/index.html#/na/003r00000012000000/)

</span></span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">OK，今天就到这里了~</span>