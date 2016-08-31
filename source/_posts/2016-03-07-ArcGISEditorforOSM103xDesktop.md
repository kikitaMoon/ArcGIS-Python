title: 'ArcGIS Editor for OSM, 10.3.x Desktop'
categories:
  - 木工开物
date: 2015-04-01 14:32:13
tags: [Geodata]
---
对于好多地图爱好者，由于保（众）密（所）严（周）格（知），获取高精度的数据不是个容易事，幸亏有了可爱的 [OpenStreetMap](http://www.openstreetmap.org/) 。


 ArcGIS Editor for OpenStreetMap 是一个免费开源的 ArcGIS Desktop 插件。上个月Esri官网提供可用于Desktop 10.3 的最新版本插件。


**下载页面：[ArcGIS Editor for OSM, 10.3.x Desktop](http://www.arcgis.com/home/item.html?id=75716d933f1c40a784243198e0dc11a1&_ga=1.40580837.631931551.1427269542)**

相关资源自取：[**点这里**](https://github.com/Esri/arcgis-osm-editor/wiki)

<br>
<br>

下载之后，有32位和64位两个安装包，如果你安装了Desktop的64位后台GP补丁，就把64位的插件程序也安装上。

ArcToolbox中多了好多工具……

![](http://img.blog.csdn.net/20150401115843672)

<br>
<br>

这里我就推荐两个最常用的工具。
<br>
<br>

**Download OSM Data**

下载的范围，可以通过手工填写坐标指定，也可以根据ArcMap现有的图层范围进行指定，这个方便又好用。

![](http://img.blog.csdn.net/20150401142437646)


![](http://img.blog.csdn.net/20150401140857073)

<br>
<br>

**Load OSM Data**

如果你已经从 OpenStreetMap 下载了 *.osm 数据文件，那就用这个工具导入 GDB 即可。简单到没什么可说的，请看图。

![](http://img.blog.csdn.net/20150401142938102)

<br>
<br>

有个关键问题，注意：

> **How much of the OSM data can I download?**
> 
> The ArcGIS Editor for OpenStreetMap uses the OpenStreetMap API, which limits downloads to **an area of 0.5 by 0.5 degrees or 50,000 nodes**, whichever is reached first. This is usually more than enough to fill an area for editing.


