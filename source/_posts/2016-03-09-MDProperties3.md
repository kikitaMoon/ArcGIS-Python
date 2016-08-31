title: 镶嵌数据集工具小结（六）镶嵌数据集的属性 Ⅲ
categories:
  - 木工开物
date: 2014-11-11 14:31:11
tags: [Raster,Geodata]
---

**设置镶嵌数据集属性工具 Ⅲ**

![](http://img.blog.csdn.net/20141027161618093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这一篇接着，再接着，说这个参数无比巨多的工具 Set Mosaic Dataset Properties， 看看其中的 Catalog Item Properties 对应的各个参数的作用 。

![](http://img.blog.csdn.net/20141110173348453)

<br>

**元数据级别**

Metadata Level 参数用于定义从服务器到客户端的元数据传输量。如果要传输大量元数据，此属性将会影响传输时间，因此可选择对其进行限制。

通过下面三个选项，选择发布镶嵌数据集时从服务器提供给客户端的元数据级别：

- FULL —所有元数据将被传输，包含基本栅格数据集信息及函数链的详细信息。这是默认设置。
- BASIC —将传输栅格数据集级别信息，比如列和行、像元大小和空间参考信息。
- NONE —不提供任何元数据给客户端。

**允许传输的字段**

Allowed Transmission Field 参数列表，定义将镶嵌数据集作为服务提供时属性表中对客户端可见的字段。

默认情况下，此列表包括字段：Name, MinPS, MaxPS, LowPS, HighPS, Tag, GroupName, ProductName, CenterX, CenterY, ZOrder, Shape_Length, Shape_Area。如果镶嵌数据集中包含自定义字段，这个列表中除了上面的字段，还会出现自定字段。

**许是否启用时间**

![](http://img.blog.csdn.net/20141111115257175?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如果镶嵌数据集包含定义时间的属性字段，可创建自动具有时间感知性的镶嵌数据集。

如果激活了时间，则需要指定与时间有关的其他参数——起始和结束字段，以及时间格式。建议将时间值存储在日期字段中，但也支持字符串和数值字段。

**地理变换方法**

如果镶嵌数据集的坐标系统不同于源栅格数据坐标系统，则可能需要指定特定的地理变换方法。通过 Geographic Transformation 参数列表选择地理变换。

**可下载的最大项目数**

Max Number of Download Items 参数用来限制客户端可从影像服务中下载的栅格数量。该值会影响系统负荷。

如果不希望客户端从镶嵌数据集内下载任何栅格，可将其设置为 0。另外注意，Grid格式数据源的镶嵌数据集不能下载。

**返回的最大记录数**

以影像服务的形式查看镶嵌数据集时，Max Number of Records Returned 参数用来限制，针对客户端每个请求，服务器返回的记录数。

**最小像素作用**

只看中文名字让人有点晕，实际上 Minimum Pixel Contribution 参数用于指定镶嵌数据集中的项目需要至少具有多少像素才能在镶嵌数据集中使用。默认值为1个像素。

我们可以设置合理的值，这样镶嵌数据集会跳过所有像素量不够大的栅格项目。跳过这些镶嵌数据集项目将有助于提高镶嵌数据集的计算或显示性能。这在大量叠置栅格只具有少量像素时尤其有用。

但是，同时需要知道，较大的值可能减少重叠项目成为感兴趣区组成部分的可能性；这会导致您的镶嵌数据集的某些区域空白。

特别需要注意的是，镶嵌数据集的属性中有其他两项属性与这个选项可能存在矛盾关系，因此，此属性仅在 **_始终将栅格裁剪至其轮廓_** 设置为“**是**”，并且 **_轮廓线可能含有 NoData_** 设置为 **否** 时有效。否则可能会无视这个选项。

![](http://img.blog.csdn.net/20141111142954812?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)