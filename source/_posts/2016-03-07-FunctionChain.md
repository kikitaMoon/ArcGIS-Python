title: 镶嵌数据集工具小结（十）函数链
categories:
  - 木工开物
date: 2014-12-04 16:22:10
tags: [Raster,Geodata]
---


**镶嵌数据集中的函数**

在下文中会提到的工具有这几个，先摆在这里，有个初步的记忆：

![](http://img.blog.csdn.net/20141203110222940)

<br>

这个主题中，一起来看一下镶嵌数据集的函数。

**★** 不过首先需要额外了解，在 ArcGIS 中，其实除了镶嵌数据集，普通的栅格数据集也可以使用函数，这并不仅仅是镶嵌数据集的特性。在 Image Analyst 窗口中，我们可以点击 fx 按钮给现有数据配置函数。

例如，下面给DEM增加个临时的山影效果，而不需要在硬盘上去存储这个结果：

![](http://img.blog.csdn.net/20141202115634265?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


![](http://img.blog.csdn.net/20141202155321880?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


在栅格数据上使用函数后，我们就可以直接查看函数作用后的结果栅格图层。在镶嵌数据集中创建的函数可以存储在数据库中，并且可以根据自己的需求，给栅格数据指定多个依次进行的函数，下一步的函数会使用上一步的函数的结果作为输入，称之为 **函数链**（Function Chain），一环扣一环，很形象。

给镶嵌数据集整体进行函数运算好处就是整体连续，如果我们每幅进行各自函数运算然后镶嵌，就会发现数据是不连续的片状。

![](http://img.blog.csdn.net/20141202155940461?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

我们在镶嵌数据集的属性窗口中可以看到 Function 选项卡，这就是配置函数链的主要的位置。

![](http://img.blog.csdn.net/20141202160306484)

如果我们在建库的时候选择某种 产品定义（Product Defination），在镶嵌数据集内部镶嵌数据集项目的也会存在函数链。

![](http://img.blog.csdn.net/20141203101020033?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

ArcGIS 提供了很多可以用于栅格处理的函数，在 Web Help 文档中有每个函数的详细描述，这里我就不一一整理了。Web Help当工具书用，还是十分便利的，大家自可按需查询，点[**这里**](http://resources.arcgis.com/zh-cn/help/main/10.2/index.html#//009t00000044000000)。

<br>


镶嵌数据集工具箱中有这样几个工具，涉及到了函数，就联合上面的内容一起说说，从整体的总结来看，正文才刚刚开始……

<br>

前面说过了，我们可以直接在镶嵌数据集上右键，Function 选项卡中增加、删除、修改函数链，我们也可以使用工具 **Edit Raster Function** 。

如果没有特别的要使用 Model Builder或者脚本等调用这个工具，个人建议可以直接到属性中去修改，操作起来更方便直观。这个工具提供了 **Insert、Replace、Remove**三种修改选项，可以将 **栅格函数模板文件(.rft.xml)** 通过操作应用给镶嵌数据集，这种文件可以在** Function Template Editor **中保存获得。

举个最简单的例子，前面用了山影函数，现在我需要换成地貌晕染函数，执行下这个工具，导入现有的函数模板替换掉即可。

![](http://img.blog.csdn.net/20141203172639032)

接着第二个相关的工具&nbsp;**Build Mosaic Dataset Item Cache**，这个工具是把 “Cached Raster Function” 函数插入到每个栅格数据函数链的顶部，这样该函数就成为链中最后实现的函数。一般是涉及到运算量较大的处理过程时，这样做可以提高性能。

在这个工具中，我们可以定义、生成缓存、指定缓存的存储位置。默认情况下，会在镶嵌数据集所处位置旁的文件夹中生成和存储缓存。此文件夹的名称与地理数据库的名称相同，但扩展名为 .cache。但是，如果镶嵌数据集创建于 ArcSDE 地理数据库，则将在该地理数据库中创建缓存。

如果我们想得到函数链处理之后镶嵌数据集中的各个栅格数据，就可以使用工具 **Export Mosaic Dataset Items**。