title: 凹凸有致的地图——浮雕风
categories:
  - 木工开物
date: 2015-08-07 14:13:37
tags: [Mapping]
---
想要下面这样一副地图，怎么做？

![](http://img.blog.csdn.net/20150807135152365)


<br>

<br>


# 1.
准备包含一个数值属性字段的面数据，比如包含人口信息的欧洲大陆数据，使用分级色带渲染。

![](http://img.blog.csdn.net/20150807135833315)



<br>

<br>


# 2.

使用 Choropleth Hillshade 工具制造“浮雕”栅格。感谢作者jwasil的分享，这个工具可以在Github上自取：[**点这里**](https://github.com/jwasil/choropleth-hillshade)。


![](http://img.blog.csdn.net/20150807140326067)


<br>

<br>


# 3.

给矢量面图层设置30%的透明，完成。

![](http://img.blog.csdn.net/20150807140846239)

<br>
<br>


[Maps we love](http://www.esri.com/products/maps-we-love/usa-population-change) 中也有一个web map，就是使用这个工具做的，[来看看](http://nation.maps.arcgis.com/apps/SimpleViewer/index.html?appid=a6cb3e1caa7549418b1a5945bcb36717)。

