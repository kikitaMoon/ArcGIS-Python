title: 聚焦等值面的创建
categories:
- 木工开物
date: 2013-07-12 12:28:36
tags: [Geoprocessing]
---
&nbsp; &nbsp; 日常我们会碰到有很多根据已知采样点生成等值面、等值线的需求，。由散点采样值估算相应区域，我们一般会想到插值，这样就获得了这个区域的连续表面。

&nbsp; &nbsp; 在ArcGIS中，插值的方法较多，主要有两个扩展模块的功能可以选用。一般情况下可以选择 Spatial Analyst 工具箱中，IDW，Kriging等方法进行插值。如果有更加复杂的参数设置和更加专业深入的插值分析，可以使用 Geostatistical Analyst，这里暂不赘述。


&nbsp; &nbsp;&nbsp;![](http://img.blog.csdn.net/20130708095149468?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;![](http://img.blog.csdn.net/20130708095542000?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


&nbsp; &nbsp; 这里以IDW插值为例，简述等值面、等值线的生成。


<br>

# 一、采样点插值





例如获取了如下一组点的臭氧浓度的采样值：

![](http://img.blog.csdn.net/20130708102201500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


使用 IDW 工具，设置输入数据，插值使用的字段，搜索半径等参数，获得栅格表面。

![](http://img.blog.csdn.net/20130708102238437?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


<br>

# 二、等值线的获取


Spatial Analyst 中提供了从栅格表面提取等值线的工具，Contour，设置等值线间隔，以及选择设置起算线。

&nbsp;&nbsp;![](http://img.blog.csdn.net/20130708103010265?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



得到结果：

&nbsp; &nbsp; &nbsp;&nbsp;![](http://img.blog.csdn.net/20130708103208734?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



<br>

# 三、等值面提取





在做等值面之前，我们需要思考下，等值面是指什么？等值面是否是两条等值线之间的闭合区域？等值面的划分依据是什么？

先说一种比较常用的场景，得到等值线后，为了美化制图，等值线之间的间隔也需要用渐变色予以填充，通常想到的方案是使用工具 Feature to Polygon。这样就得到了与等值线无缝贴合的等值面。如下图：

![](http://img.blog.csdn.net/20130712093921515)



从而获得等值面，这个类似于等间距分类或者等值面的方法。


<br>

<br>



**如果抛开等值线而言，比较准确的获取等值面的方法是什么呢？**

<br>

答案是对栅格表面进行重分类，用一定的数学算法将数据进行数值的重新划分与赋予。

下面来总结一下方案：





**（1）使用工具 Reclassify 进行栅格数据重分类：**

如下是一个由高程采样点获得的DEM，然后进行重分类，分类方法是等间距法：

PS：分类是有很多方法可以选择的，具体在分类面板中可以设置：

![](http://img.blog.csdn.net/20130712122641406)

![](http://img.blog.csdn.net/20130712100659281)


**（2）然后将栅格数据转为矢量面:**

使用转换工具， Raster to Polygon，得到矢量等值面：

![](http://img.blog.csdn.net/20130712101236468)


**（3）等值面，等值线的后期平滑处理**

由栅格数据得到的矢量数据，通常边界会出现很多方格子或者锯齿，后面要做的工作就是对面进行平滑和美化，当然这步是选做工作了。

前两步是数据的真实提取，这一步就是对地图画个妆，把最佳的效果展示出来。

为了防止直接平滑面出现边界不重合的问题，建议对面转线（Feature to line），平滑线后再转回面。做了个模型，把这个思路完整的展现出来，如下图：

![](http://img.blog.csdn.net/20130712120449250)




这样就会得到相对漂亮平滑的等值线和等值面。

细节对比图：

![](http://img.blog.csdn.net/20130712122149390)




<br>


以上就是制作等值面的方法。