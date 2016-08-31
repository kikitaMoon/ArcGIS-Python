title: 镶嵌数据集工具小结（四）镶嵌数据集的属性
categories:
  - 木工开物
date: 2014-10-29 15:00:24
tags: [Raster,Geodata]
---
**设置镶嵌数据集属性工具**

![](http://img.blog.csdn.net/20141027161618093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我们可在镶嵌数据集属性窗口看到 General，Default，Key MetaData 三个选项卡。

- General 中包含了类似单个栅格数据集的属性信息，例如像元大小、像元类型、位深、范围等等信息，详情可以戳 [**这里**](http://resources.arcgis.com/zh-cn/help/main/10.2/index.html#//009t00000018000000)，不再赘述；

- Default 选项卡中包含了一些镶嵌数据集所特有的属性，这些属性将会影响客户端查看镶嵌数据集的显示方式和交互方式；

- 如果为镶嵌数据集定义了产品定义，则 Key Metadata 将来自产品定义，Key Metadata 包含了用于渲染和一些处理过程的波段和波长信息。

![](http://img.blog.csdn.net/20141027153224478?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 需要注意的是，如果我们在图层列表中去修改镶嵌数据集的默认属性，这种修改不会存储到镶嵌数据集内部，因此当移除图层，这些设置就失效了。图层上的修改，一般用于临时查看修改效果，或者多个用户访问镶嵌数据集，并且希望自己的修改不影响到其他人。

而我们在Catalog中，镶嵌数据集的属性中设置的属性是存储在镶嵌数据集中。 需要了解Default 选显卡中各个属性项的作用和对镶嵌数据集的影响，非常详细的说明就戳** [这里](http://resources.arcgis.com/zh-cn/help/main/10.2/#/na/009t00000038000000/)**，注意其中部分参数仅适用于镶嵌数据集作为 Image Service 发布和访问的情形。

在工具箱中提供了一个可以设置这些属性的工具  Set Mosaic Dataset Properties 关于这个工具，我就结合镶嵌数据集属性来说明各个参数的作用和适用情况。由于这是一个很多很多参数的工具，这一篇先说说影像属性部分的参数吧。

![](http://img.blog.csdn.net/20141029145413027?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



**影像属性**


**_Maximum Size Of Requests_**：

![](http://img.blog.csdn.net/20141028141823777?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

控制每次生成镶嵌影像时的最大行数和列数。仅当将镶嵌数据集作为影像服务而发布和访问时，此属性才适用。

**_Allowed Compression Methods_**：

![](http://img.blog.csdn.net/20141028141917878?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

定义将镶嵌影像从服务器传输到客户端时所使用的压缩方法。如果通过 LAN 访问影像服务，即使数据量很大也不会引发问题。但通过速度较慢的 Internet 连接访问时，最好在传输前对影像进行压缩。压缩会减小传输影像的大小，但服务器需要先对数据进行压缩，因而增添了额外负荷。如下是几种压缩方法的整理：

- **None** —— 不压缩影像，这可以提供最高质量的影像，但是在网络中需要传输的数据量最大。
- **LZ77** —— 一种高效的无损压缩方法，推荐用于具有相似像素值（离散数据）的影像，例如扫描的地图或分类后的影像。
- **JPEG** —— 一种高效的压缩方法，它通常可将影像压缩三至八倍，但在影像质量上有轻微损失。如果选择 JPEG 方法，也可通过输入 0 至 100 之间的任意值来编辑质量。值 80 提供大约 8 倍的压缩，通常能够保证影像质量。
- **LERC** —— 一种高效的有损压缩方法，推荐用于具有较大像素深度的数据（如浮点型、32 位、16 位或 12 位数据）。选择此方法时，需要指定代表每个像素所适用的最大错误值的质量值。该值以镶嵌数据集的单位指定。例如，如果误差为 10 厘米而镶嵌数据集的单位为米，则输入 0.1。对于浮点型数据，LERC 比 LZ77 的压缩效果好 5 到 10 倍，压缩速度快 5 到 10 倍；对于整型数据，LERC 的压缩效果和压缩速度更优于 LZ77。使用整型数据并且指定的错误限制为 0.99 或更低时，LERC 相当于无损压缩。

**_Default Resampling Method：_**

![](http://img.blog.csdn.net/20141028143111501?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- **NEAREST** —— 使用最邻近采样法可获得较精确的辐射度值。这种方法通常速度较快，但会导致要素的边呈锯齿状。
- **BILINEAR** —— 双线性插值法可提供较平滑的影像，但会导致某些影像被滤除掉。对于连续栅格数据，建议使用双线性插值法。
- **CUBIC**—— 与双线性插值相比，三次卷积插值法生成的几何更加精确，但速度较之稍慢。
- **MAJORITY** —— 众数法最适用于离散数据。

**_Clip to Footprint：_**

许多情况下，栅格和轮廓线是相同的，但当它们不同时，您可以指定是否裁剪栅格。


**_Footprints May Contain NoData：_**

指定镶嵌数据集的轮廓线是否包含 NoData 的像素。如果选择包含，可以确保footprint中不包含洞。


_**Clip To Boundary**：_

指定是否要裁剪镶嵌数据集的影像到边界，或显示整个镶嵌影像。


**_Color Correction：_**

设置是否启用为镶嵌数据集设置的色彩校正


**_Allowed Mensuration Capabilities：_**

![](http://img.blog.csdn.net/20141028163714082?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- **None**  — 不使用任何测量功能；
- **Basic** — 允许计算距离、点、质心和面积；
- **Base-Top Height** — 允许测量底部至顶层高度。要执行底部至顶层高度测量，需要有理多项式系数 (RPC) 信息.
- **Base-Top Shadow Height** — 允许测量底部至顶层阴影高度。要执行底部至顶层阴影高度测量，需要太阳方位角和太阳高程信息。
- **Top-Top Shadow Height** — 允许测量顶部至顶部阴影高度。要执行此测量，需要太阳方位角、太阳高程和有理多项式系数 (RPC) 信息。
- **3D** — DEM 可用时，可进行 3D 测量。

具体对应的测量工具，我们可以在 Image Analysis 窗口中使用。

![](http://img.blog.csdn.net/20141029111447680?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

有关影像测量这一块将来如果有时间会单独整理一下，这里不再插入了，不然篇幅过长了。_

**Data Source Type：**

![](http://img.blog.csdn.net/20141029113540082?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- Generic - 通用类型，镶嵌数据集没有指定的数据类型。
- Thematic - 镶嵌数据集为专题型，专题数据具有离散值。
- Processed -镶嵌数据集已得到处理。镶嵌数据集的颜色已经过调整。
- Evelation -镶嵌数据集包含高程数据。

琳琅满目的影像属性参数就说到这里，下一篇接着说设置镶嵌数据集属性中的镶嵌属性参数。