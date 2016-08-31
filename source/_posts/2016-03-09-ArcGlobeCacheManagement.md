title: ArcGlobe 缓存管理
categories:
- 木工开物
date: 2014-08-05 11:26:08
tags: [3D]
---

<span style="font-family:Microsoft YaHei; font-size:14px">ArcGlobe拥有缓存机制，因此可以应对大量3D数据的可视化，下面就总结下有关缓存的知识点。</span>

<span style="font-family:Microsoft YaHei; font-size:14px">

</span>

<span style="font-family:Microsoft YaHei; font-size:14px">首先，需要了解，ArcGlobe具有两种缓存机制：内存缓存，硬盘缓存。</span>

<span style="font-family:Microsoft YaHei; font-size:14px">

</span>

<span style="font-family:'Microsoft YaHei'">**<span style="font-size:24px; color:#cc0000">内存缓存&nbsp;</span>**<span style="font-size:14px">指的是分配可供 ArcGlobe 使用的物理内存 (RAM) 大小。要获得最佳性能，可设置对每个所使用的数据类型所分配的内存大小。ArcGlobe 通过设置内存缓存来改善 3D 视图的交互性能，可针对每个 ArcGlobe 文档（.3dd 文件）配置特定的内存值。</span></span>

<span style="font-family:'Microsoft YaHei'"><span style="font-size:14px">![](http://img.blog.csdn.net/20140805102306496?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

</span></span>

<span style="font-family:'Microsoft YaHei'"><span style="font-size:14px">![](http://img.blog.csdn.net/20140805110536867?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

</span></span>

<span style="font-family:'Microsoft YaHei'"><span style="font-size:14px">

</span></span>

<span style="font-family:'Microsoft YaHei'"><span style="font-size:14px">

</span></span>

<span style="font-family:Microsoft YaHei">**<span style="font-size:24px; color:#cc0000">磁盘缓存&nbsp;</span>**<span style="font-size:14px">会为 ArcGlobe 中的每个图层创建临时文件或缓存，从而有助于高效地显示和导航数据。</span></span><span style="font-size:14px; font-family:'Microsoft YaHei'">每个图层，而不是数据源，对应一“套”缓存文件，以文件夹的形式保存。文件夹通常以图层名+GUID命名。例如下图：</span>

<span style="font-family:Microsoft YaHei; font-size:14px">![](http://img.blog.csdn.net/20140805101124635?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

</span>

<span style="font-family:Microsoft YaHei; font-size:14px">![]()

</span>

<span style="font-size:14px"><span style="font-family:Microsoft YaHei">保存 ArcGlobe 文档（*.3dd）或创建图层文件（*.lyr）</span><span style="font-family:Microsoft YaHei">可确保不会无意中删除磁盘缓存，以及保留缓存的链接以供以后使用。如果图层的显示发生更改，则会自动删除它的磁盘缓存并重新进行计算。</span></span>

<span style="font-size:14px"><span style="font-family:Microsoft YaHei">

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">默认缓存是按需进行创建，也可以进行手动创建图层的</span><span style="font-family:'Microsoft YaHei'">部分缓存、</span><span style="font-family:'Microsoft YaHei'">全部缓存。</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">![](http://img.blog.csdn.net/20140805110228156?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">![](http://img.blog.csdn.net/20140805110245671?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">磁盘缓存的格式可以根据需要选择，ArcGlobe 支持两种磁盘缓存格式：JPEG 和 DXT。一般来说，JPEG 磁盘缓存格式占用的磁盘空间较少，而 DXT 缓存可提高渲染速度。</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-family:'Microsoft YaHei'; font-size:14px">下面的问题引自帮助，稍加整理，放在这里辅助这两种格式的选择：</span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-size:18px; color:#ff6666"><span style="font-family:'Microsoft YaHei'; background-color:rgb(204,255,255)">**JPEG 和 DXT 格式的区别是什么？**</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">在显卡较新的计算机上，DXT 缓存不必在渲染前解压缩。但 JPEG 缓存却需要在渲染前解压缩，因此存在性能开销。</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">具有 16 位色彩格式的 JPEG 缓存数据要求每像素占 2 个字节内存，而 DXT 缓存数据则要求每像素仅占 1 个字节内存。这意味着，DXT 数据所占用的图形内存只占 JPEG 16 位色彩数据所占用图形内存的一半。但 DXT 缓存所占用的磁盘空间通常比 JPEG 缓存大 8 到 12 倍。</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-size:18px; color:#ff6666"><span style="font-family:'Microsoft YaHei'; background-color:rgb(204,255,255)">**JPEG 与 DXT 分别应于何时使用？**</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">**1）显卡硬件的版本**</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">如果计算机的显卡版本较低，有可能不支持 DXT 格式。在此类情况下，ArcGlobe 将使用仿真软件代替硬件，使计算机支持 DXT 缓存，但这样的话，使用 DXT 磁盘缓存选项并不会提高性能。</span></span><span style="font-family:'Microsoft YaHei'; font-size:14px">版本较新的计算机则可以实现 DXT 格式的硬件支持，因此适合使用 DXT 缓存选项。如果注重应用程序的性能，则建议使用该格式。</span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">**2）数据范围**</span></span>

<span style="font-family:'Microsoft YaHei'; font-size:14px">决定 JPEG 和 DXT 缓存性能差异的一个关键性因素是数据范围。对于本地区域范围内的图像数据，DXT 缓存的渲染速度比 JPEG 缓存最多可快 40%（以每秒的帧数衡量）。但是，如果数据是全球范围的，则两种格式之间几乎没有差异。</span><span style="font-family:'Microsoft YaHei'; font-size:14px">但是，无论数据范围如何，DXT 磁盘缓存格式与 JPEG 磁盘缓存格式的缓存</span><span style="font-family:'Microsoft YaHei'; font-size:14px">生成时间相同</span><span style="font-family:'Microsoft YaHei'; font-size:14px">。</span>

<span style="font-family:'Microsoft YaHei'; font-size:14px">**3）物理内存的大小**</span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">决定选择哪种格式的另一个关键性因素是计算机的物理内存大小。使用 DXT 缓存而非 JPEG 缓存时，ArcGlobe 将节省 10% 到 30% 的整体内存，从而在渲染大型数据集而计算机内存（RAM 和图形卡纹理内存）却有限的情况下可以提高性能。</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">**4）磁盘空间**</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">最后一个值得考虑的因素是磁盘空间。尽管 DXT 缓存的交互性能通常比 JPEG 缓存要好，但是它所占据的磁盘存储空间却会多出很多。根据数据的不同，DXT 缓存所占用的磁盘空间比 JPEG 缓存大 8 到 12 倍。</span></span><span style="font-family:'Microsoft YaHei'; font-size:14px">因此，应考虑是需要更好的性能还是更大的磁盘空间。</span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>

<span style="font-size:18px; color:#ff6666"><span style="font-family:'Microsoft YaHei'; background-color:rgb(204,255,255)">**使用 DXT 缓存时有哪些特殊注意事项？**</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">能否使用 DXT 取决于 OpenGL 图形卡驱动程序和图形卡硬件。有时，一些 OpenGL 工具可能无法支持或无法正常支持 DXT 压缩。这可能导致 DXT 缓存中产生失真。要解决此类问题，可以更新显卡驱动程序版本或使用其他显卡。

</span></span>

<span style="font-size:14px"><span style="font-family:'Microsoft YaHei'">

</span></span>