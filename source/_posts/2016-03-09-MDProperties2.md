title: 镶嵌数据集工具小结（五）镶嵌数据集的属性 Ⅱ
categories:
  - 木工开物
date: 2014-11-10 15:40:11
tags: [Raster,Geodata]
---
**设置镶嵌数据集属性工具 Ⅱ**

![](http://img.blog.csdn.net/20141027161618093 /)

这一篇接着说这个参数无比巨多的工具 Set Mosaic Dataset Properties ，镶嵌属性这一组参数会控制多幅影像的拼接方式和顺序等。

![](http://img.blog.csdn.net/20141030174319646)

如果我们的多幅影像的数据源之间没有重叠，那么拼接顺序就没有什么值得设置的。但是我们一般拿到的航片、卫片等都是有重叠的，不同的镶嵌规则会让数据在拼接出现差异，我们设置这一组参数来控制影像的拼接方式和顺序等。

![](http://img.blog.csdn.net/20141110103650420)

<br>

# **Mosaic Methods（镶嵌方法）**

**![](http://img.blog.csdn.net/20141030174429250)



在“允许的镶嵌方法”中我们可以选择影像的镶嵌方法，从而控制用户访问镶嵌数据集时可以使用哪些方法。同时，可以设置一种方法作为默认方法。


- None 根据镶嵌数据集属性表中的顺序 (ObjectID) 对栅格进行排序。
- Center - 根据栅格中心与视图中心的距离对栅格进行排序，与视图中心距离越小，栅格的默认次序越靠前。
- NorthWest - 中心越靠近西北的栅格显示的位置越靠上。
- LockRaster - 允许用户根据 ObjectID 锁定单个或多个栅格数据的显示。
- ByAttribute - 根据已定义的元数据属性及其与基值的差对栅格进行排序。
- Nadir - 根据像底点位置和视图中心的距离对栅格进行排序。此方法与“Center”方法类似，但使用的是栅格的像底点，像底点可以不是中心点，尤其是在倾斜的影像中。
- Viewpoint - 使用“视点”工具根据用户定义的位置与栅格的像底点位置对栅格进行排序。
- Seamline - 使用预定义的接缝线形状分割栅格（可以选择是否沿接缝线使用羽化功能）并根据属性表中的 SOrder 字段对影像进行排序。

假设我现在有这样9幅影像数据源的镶嵌数据集，可以把他们理解成9张卡片。看图比看例子更容易理解，下面通过一个例子来了解各种镶嵌方法，前提是我们都是用升序排序和使用默认的 First 镶嵌运算符。

★ 选在**None**方法，默认使用了数据的存储顺序作为镶嵌顺序，也就是 ObjectID 的顺序。图中的数字即使各幅影像的 ObjectID，数字越靠前，镶嵌的也就越靠前。

![](http://img.blog.csdn.net/20141102180840281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 选择 **Center** 方法，中心的影像最优先：

![](http://img.blog.csdn.net/20141107165933121?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 选择 **NorthWest** 方法，我们看到位于西北角的 7 获得了最优先的镶嵌顺序，反之，东南角的9排在最后：

![](http://img.blog.csdn.net/20141102181036266?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 选择 **Lock Raster **方法，允许客户端可以指定某些栅格数据，这样仅对被锁定的栅格进行显示：

![](http://img.blog.csdn.net/20141107171537671?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![](http://img.blog.csdn.net/20141107171707761?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 选择 **ByAttribute** 方法，需要指定 **_Order Field_** ，例如按照自定义字段 MyOrder 排序：
 
![](http://img.blog.csdn.net/20141107165826578?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![](http://img.blog.csdn.net/20141107165750364?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如果您的字段是数值或日期字段，则可以设置排序基础参数（**_Order_Base_**）。可以根据此值与 Order_Field 中的其他值之间的差异对影像进行排序。

还可以指定排序是升序还是降序。

![](http://img.blog.csdn.net/20141107172724461?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

★ 选择 **Nadir** 方法，类似于 Center 方法，只是像底点距离整个视图中心的距离成为镶嵌的标准：

如下图，点A即为像底点（nadir），在垂直摄影测量中，影像中心点和像底点可能是重合的：

![](http://img.blog.csdn.net/20141110104653486?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

此方法与“Center”方法类似，但使用的是栅格的像底点，像底点可以不是中心点，尤其是在倾斜的影像中。

![](http://img.blog.csdn.net/20141110104707604?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

★ 选择 **Viewport **方法，可以使用“ViewPoint”工具根据自定义的位置与栅格的像底点位置对栅格进行排序。

ViewPoint 是个隐藏工具，我们可以在自定义菜单中找到并添加出来：

![](http://img.blog.csdn.net/20141110141450593?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

打开 Viewpoint 窗口之后，我们就可以自定义视点，视点的位置将会影响栅格数据的镶嵌顺序，如下图。

![](http://img.blog.csdn.net/20141110141806340?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在设置镶嵌数据集属性的时候，参数 View Point Spacing X 与 View Point Spacing Y 会影响 ViewPoint 对话框中的箭头按钮的偏移量，偏移量的长度单位是当前空间参考决定的。

![](http://img.blog.csdn.net/20141110142326640)

★ 选择 **Seamline** 方法，使用预定义的接缝线形状分割栅格，并且可以选择是否沿接边使用羽化功能。在生成接缝线的过程中对排序进行预定义。使用此镶嵌方法时，镶嵌运算符 LAST 无效。

镶嵌数据集的接缝线可以通过 **Build Seamlines** 工具来创建，这个工具后面会单独的总结一下。这里就不罗嗦了。

<br>

# **Mosaic Operator（镶嵌运算符）**

镶嵌运算符用于确定如何解析重叠像元。

![](http://img.blog.csdn.net/20141110153104890?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- First 重叠区域中所列出的第一个栅格数据集中的像元。
- Last 重叠区域中所列出的最后一个栅格数据集中的像元。
- Min 重叠区域中包含所有重叠像元中的最小像元值。
- Max 重叠区域中包含所有重叠像元中的最大像元值。
- Mean 重叠区域中包含所有重叠像元的平均像元值。
- Blend 重叠区域是镶嵌影像中沿各栅格数据集边缘重叠的像元值的混合。默认情况下，各栅格的边由轮廓线或接缝线定义。
- Sum 重叠区域中包含所有重叠像元的像元值总和。

**Blend Width（混合宽度）**

当在上述方法中，定义混合（Blend）镶嵌运算符所使用的像素距离。

跨越边界时此值将分成两半；因此，如果该值为 40，则将在轮廓线内部混合 20 像素，在轮廓线外部混合 20 像素。

如果存在接缝线，可以在接缝线表中定义每个接缝线的混合宽度和类型，从而覆盖此值。

除了镶嵌方法以及有关的这些参数，镶嵌属性的设置参数中还包含了其他一些与镶嵌有关的参数，放在下面以便参考：

![](http://img.blog.csdn.net/20141110153037702?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**Max Number Per Mosaic（每个镶嵌图的最大栅格数）**

这个参数是为了镶嵌数据集镶嵌过多栅格数据，默认值为 20。

例如，在没有创建概视图时，不希望让机器耗费资源过多的去镶嵌栅格数据。但是这种情况下，很可能20幅图像不足够观看，如果你的机器硬件过硬，这个数字也可以适量调大。这个参数相当于性能与体验的博弈，在没有概视图的时候可以自己尝试设置。

**Cell Size Tolerance Factor （像元大小容差系数）**

用于控制具有不同像素大小的镶嵌数据集项目在某些操作（例如镶嵌或接缝线生成）中的分组方式。

系数 0.1 表示所有比最低像素大小高百分之十的 LowPS 值都被视为相同的值。此值必须大于或等于 0.0。可在等级表中查看结果。

**Output Cell Size（输出像元大小）**

镶嵌数据集的像元大小一般是自动计算的，我们也可以进行自定义。这个参数用于自定义指定镶嵌数据集的像元大小，可选择图层作为像元大小模板，也可指定实际像元大小。如果指定像元大小，可以将单个值用于方形像元大小，或者将 X 值和 Y 值用于矩形像元大小。