title: 镶嵌数据集工具小结（八）色彩平衡与接缝线 Ⅱ
categories:
  - 木工开物
date: 2014-11-20 17:26:05
tags: [Raster,Geodata]
---

# 镶嵌数据集的色彩平衡

![](http://img.blog.csdn.net/20141111154935774)



## 创建接缝线

在对镶嵌数据集进行镶嵌的时候，有时还会用到接缝线（Seamline）。在前面总结过镶嵌数据集的镶嵌方法，其中最后一种是 Seamline 镶嵌方法。**在创建接缝线之前，建议先进行色彩平衡**，因此就拿到这里一起说。

当我们把镶嵌方法选为了 Seamline 镶嵌方法时，Seamline 就会替代 Footprint 来作为每幅栅格数据的边线。这样会让接缝更自然，镶嵌数据集看起来会更像是无缝的一整张栅格数据。如果为镶嵌数据集创建了接缝线，还有个好处就是，我们可以根据需要去编辑接缝线，例如有的接缝线刚好穿过一个建筑物，我们就可以尽可能让边线绕过建筑物，让影像看起来拼接的自然美观一些。

工具**Build Seamlines**用来为镶嵌数据集创建接缝线的。Seamline 与 Footprints 类似：每个面表示一个图像。面的形状表示查看镶嵌数据集时将用于生成镶嵌图像的那部分图像。构建了 Seamline 之后，ArcMap 中显示镶嵌数据集时，会又多了一个图层 Seamline。根据镶嵌方法，等级值将存储在属性表的 SOrder 字段中。

下面就一起看看这个工具的使用方法：

**Computation Method**

构建接缝线，有五种计算方法可选：**GEOMETRY ,&nbsp;RADIOMETRY , COPY_FOOTPRINT ,&nbsp;COPY_TO_SIBLING ,&nbsp;EDGE_DETECTION&nbsp;**。

为了更直观的认识上面构建接缝线的方法，我还是用个简单的数据来说明问题：

数据是按照北西方法镶嵌，加上Footprint是这样的：

![](http://img.blog.csdn.net/20141118140650312?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


**Geometry / 几何**—— 根据当前的排序方法和Footprint来生成接缝线。通过这种方法生成的接缝线一眼就知道了栅格数据之间的压盖关系，并且接缝线（面）之间没有要素压盖。

![](http://img.blog.csdn.net/20141118141019296?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)![](http://img.blog.csdn.net/20141118170155647?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


**Radiometry/ 辐射度**—— 通过检查相交区域的值和样式来构建接缝线，接缝线是Footprint交点之间的折线。这种方法拼接的影像看起来更自然一些。

![](http://img.blog.csdn.net/20141118143818488?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)![](http://img.blog.csdn.net/20141118170036695?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



**Copy_footprint/复制轮廓**—— 这种方法的接缝线只是相应轮廓线的副本。

![](http://img.blog.csdn.net/20141118145314046?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



**Copy_to_sibling/复制到同类**—— 此方法将已有的接缝线复制到与其组名相同的同类要素中。这种方法常常用于全色波段与多光谱波段范围不同的卫星影像，从而确保它们共享相同的接缝线。&nbsp;这里没有合适的数据，不放图了。



**Edge_detection/边缘检测**—— 对相交区域应用边缘检测过滤器，以确定该区域中要素的边。然后，沿检测到的边创建接缝线。这种方法创建的接缝线也很漂亮和自然。

举个例子，看下面的影像边界是不是扎眼？

![](http://img.blog.csdn.net/20141118171347882?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

使用边界探测方法创建接缝线后，一条沿着马路的折线（面的边界）产生了。

![](http://img.blog.csdn.net/20141118173513203?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

使用 接缝线方法拼接后就更加自然了。

![](http://img.blog.csdn.net/20141118173655828?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

**Sort Method**

默认情况下，Seamline 排序是使用 “North-West” 镶嵌方法生成的。还可以选择使用 “CLOSEST_TO_VIEWPOINT&nbsp;” 或 “BY_ATTRIBUTE&nbsp;” 镶嵌方法来创建接缝线。这与前面说的镶嵌方法的理念是一样的，不再啰嗦了。

**Cell Size**

像元大小用于确定要生成接缝线时的栅格大小。

通常用在镶嵌数据集中存在多种数据分辨率并且只想为一个等级生成接缝线的情况。例如，如果将高分辨率数据源与低分辨率数据源进行混合，则可指定适合其中一个数据源范围的像元大小。如果存在多个 LOWPS（低像素大小）值，或者不确定要指定哪个像元大小，可将此参数留空。该工具将自动在适当的等级上创建接缝线。此参数的单位与镶嵌数据集的空间参照单位相同。

**沿接缝线混合（羽化）**

可以定义沿接缝线发生的混合的混合值（羽化）和类型，混合发生在接缝线上有重叠栅格的像素之间。

**Blend Width Units**

定义混合宽度的单位。默认是 PIXELS（像素）；还可选择 GROUND_UNITS，也就是也镶嵌数据集的单位相同。

**Blend Width**

混合宽度定义要混合的像素数目。

**Blend Type**

BOTH，INSIDE，OUTSIDE 三种混合类型。

例如：如果“混合宽度”值为 10，且使用 BOTH 作为混合类型，则将在接缝线的内部和外部分别混合 5 个像素。如果该值为 10，且混合类型为 INSIDE，则将在接缝线的内部混合 10 个像素。

**Request Size Type**

PIXELS — 将根据像素大小修改请求大小。根据栅格像素大小对最近图像进行重采样。

PIXELSIZE_FACTOR —将根据像素大小因子修改请求大小。通过将像元大小等级表（Level Table）中的 &nbsp;Cell Size 与 Pixel Size Factor 相乘对最近图像进行重采样。

**Request Size**

此参数决定对栅格进行重采样的大小，用于定义行列数。最大值为 5000。可以基于栅格数据的复杂程度增大或减小该值。