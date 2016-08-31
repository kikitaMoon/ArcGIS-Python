title: 镶嵌数据集工具小结（二）镶嵌数据轮廓线与边界
categories:
  - 木工开物
date: 2014-10-17 14:57:34
tags: [Raster,Geodata]
---
上一篇帖子说明了如何创建镶嵌数据集、添加栅格数据，以及相关的常用参数配置。

下面再接着说如何根据自己的各种需要来修改镶嵌数据集，这一贴的主题主要是如何创建、修改镶嵌数据集的轮廓线和边界。

**修改镶嵌数据轮廓线、边界类工具**

![](http://img.blog.csdn.net/20141017145207271)

当镶嵌数据集创建好之后，我们将其加入到 &nbsp;ArcMap 中后发现，镶嵌数据集是以类似图层组的形式加入的，包含了至少三个图层，分别为：**Boundary**、**Footprint** 和 **Image**。

![](http://img.blog.csdn.net/20141017145458637)

在使用开头列出的那些工具之前，我们需要对上图的几个图层有所了解，了解的过程中自然会发现这些工具的用武之地。

**Image（影像）**

影像图层用于控制镶嵌数据集的动态镶嵌影像的渲染。如果你在ArcMap中显示过单张影像，那会发现这个图层其实看起来和单张影像差别不大。也就是镶嵌数据集将散列在磁盘上的多张栅格数据，动态拼接成了一整张栅格。对影像图层属性做出的修改不会影响镶嵌数据集，仅影响镶嵌数据集在显示时的渲染方式。

**Footprint（轮廓线）**

轮廓线是按照镶嵌数据集的坐标系统创建的，有可能有原始栅格数据的坐标系不一致。还记得上一篇中提到过创建镶嵌数据集时指定的坐标系可以与原始栅格数据不同吗？轮廓线包含镶嵌数据集内每个栅格的轮廓，但是不一定是每个栅格数据集的范围，而应该是栅格数据集内有效栅格数据的范围。NoData 区域是轮廓线形状所排除内容的典型示例。

![](http://img.blog.csdn.net/20141016153532207?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

当然，我们也可以根据自己的需求，进一步定义和裁剪栅格数据。方法通常是三种：

- **1）自动计算方法：**
  
使用 **Build Footprint** 工具执行系统计算得到新的轮廓线。

重新定义轮廓线的方法有：

 - RADIOMETRY：根据像素值范围来重新定义轮廓线的形状，从而排除无效数据（*辐射法重新计算轮廓线这个小专题可以展开，以后有时间可以详细整理。）
 - GEOMETRY：将轮廓线的形状重新定义为其原始几何形状
 - COPY_FROM_SIBLING：在使用全色锐化的栅格类型时，轮廓线将被替换为多光谱项的轮廓线。

在这之前，还可以使用 **Define Mosaic Dataset NoData** 工具将栅格中不希望显示的值置为Nodata，这个工具允许同时将多个值置为Nodata。然后再执行 Build Footprint 可以一次性排除全部Nodata值。

**2）手工编辑方法：**

通过编辑工具条，手工编辑修改 Footprint 面要素得到新的轮廓线。这种方法和我们平时编辑矢量面没有什么区别。

**3）导入已有多边形的方法：**

可以使用工具**Import Mosaic Dataset Geometry **，将面要素导入，按照指定的关联字段替换轮廓线。另外，此工具也可用于替换边界或接缝线多边形。


**Boundary（边界）**

Boundary层，我们可以理解成镶嵌数据集所引用的所有栅格数据的外边界，实际它是一个储存在地理数据库（GDB）内部的面要素类。我们可以使用 **Build Boundary** 工具来创建这个层，也可以在一开始添加栅格工具中勾选&nbsp;Build Boundary 参数。

那这个Boundary 层是基于什么计算得到的呢？ 本质上，是将许许多多的 Footprint 层进行融合得到的。 也就是我们可以理解成，Footprint是每个栅格数据的边界，而Boundary是全部栅格的Footprint融合之后的总外边界。边界用于确定镶嵌数据集的空间范围。

如下图，说明 Footprint 与 Boundary：

![](http://img.blog.csdn.net/20141017112717132?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

创建边界可以指定简化方法，可以是实际数据边界，也就是不进行简化（None），可以是凸多边形（Convex Hull），还可以是外接矩形（Envelope）。

如下图一目了然：

![](http://img.blog.csdn.net/20141017135953912)


如果镶嵌数据集中所包含的栅格数据超出了边界，那超出的数据在镶嵌图像中就不可见了。因此，我们可以通过修改边界来限制镶嵌数据集的可见内容。


类似操作 Footprint，我们可以通过手工编辑，或者使用工具&nbsp;Import Mosaic Dataset Geometry 制作自定义边界。

![](http://img.blog.csdn.net/20141017135947171)

当然与&nbsp;Import Mosaic Dataset Geometry&nbsp;工具相应，我们还可以使用工具 **Export Mosaic Dataset Geometry**导出镶嵌数据集的轮廓线、边界等要素类。


有关轮廓线、边界、镶嵌数据集图层就到这里了，对于初学者来说，上面这些足够用了。

下一篇我会接着整理有关概视图创建等增强优化镶嵌数据集的工具。
