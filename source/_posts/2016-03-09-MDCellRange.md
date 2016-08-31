title: 镶嵌数据集工具小结（九）计算像元大小范围
categories:
  - 木工开物
date: 2014-11-28 15:41:03
tags: [Raster,Geodata]
---
**计算像元大小范围**

![](http://img.blog.csdn.net/20141127151918341)

像元大小范围指的是，镶嵌数据集中的影像参加动态镶嵌的像元大小范围，也就是，动态镶嵌的过程中从栅格数据集中读取的像元大小的范围。


在镶嵌数据集的属性表中，字段 **LowPS** 列和 **HighPS** 列定义镶嵌数据集从源栅格数据集中读取的像元大小的 **实际范围**。当我们向镶嵌数据集中添加栅格时，工具会根据源栅格数据分辨率、金字塔等级、金字塔选项中的设置 来计算属性表中 LowPS 与 HighPS 字段值。
例如，下图中的 LowPS = 0.1 表示基础像素值，High = 0.4 表示正在使用的顶级金字塔像素值。对于不包含金字塔的栅格数据集，低像素大小和高像素大小可能为相同的值，例如第一行。

![](http://img.blog.csdn.net/20141125171612875?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

例如，在使用所有金字塔等级的情况下，如果栅格数据集包含 1 米的像元，且包含像元大小为 2、4、8 和 16 米的金字塔，则 LowPS 是 1，HighPS 是 16。如果在栅格金字塔选项中将最大像元大小设置为 8，则 HighPS 将为 8 而不是 16。

![](http://img.blog.csdn.net/20141127155304879?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


属性表中还有两列：**MinPS** 列和 **MaxPS** 列，用来定义在什么像元大小范围内请求什么栅格数据。当我们向镶嵌数据集中添加栅格数据时，选中添加栅格至镶嵌数据集对话框上的 **Update Cell Size Ranges (optional)** 选项，或使用工具 **Calculate Cell Size Ranges** 时，就会填充两列字段值；也可以手动编辑表中的值。
MinPS 和 MaxPS 是根据栅格数据和叠加在上面的概视图来计算的。

用下面一幅图，可以看出默认情况下，MinPS，MaxPS 与 LowPS，HighPS 的关系：

![](http://img.blog.csdn.net/20141127164421578?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


当加入镶嵌数据集的栅格数据源有多种分辨率时，就可以利用像元大小范围来控制不同比例尺下显示不同的栅格数据。

例如，在国家级别查看影像，可以使用 [Landsat](http://baike.baidu.com/view/4221567.htm?fromtitle=Landsat&fromid=7195765&type=syn) 影像，约 30 米的像元大小；当放大到更高的比例，镶嵌数据集可以提供 SPOT 图像，像元大小约 5 米；进一步放大时，最终将看到航空正射影像，像元大小更小，分辨率更高。


比例尺和像元大小有很大的关系，如果我们希望求取计算的话，可以参考如下公式：
	**Scale = CellSize * 96 / 0.0254**
	其中，ArcGIS 中 DPI 的默认值为 96，1 英寸（Inch） = 0.0254米，CellSize是以“米”为单位的。
	公式反之，可以通过比例推算像元大小：
	**CellSize = Scale * 0.0254 / 96**


如果我们访问镶嵌数据集时，不断的放大地图，最终请求的影像的 Cell Size 小于了全部的 MinPS，那么就会请求失败，不再会返回影像；反之，如果我们不断的缩小地图，最终请求的Cell Size 大于了全部的的 MaxPS，那么也会请求失败，返回黑色和白色的棋盘状图案。也就是说，镶嵌数据集的像元大小范围会直接影响我们在缩放地图时影像数据的可见性。

That's all ...