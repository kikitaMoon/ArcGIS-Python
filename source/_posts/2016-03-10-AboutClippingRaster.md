title: 使用矢量面裁剪栅格数据的对齐问题
categories:
- 木工开物
date: 2014-07-29 11:19:31
tags: [Raster]
---

最近凑巧有几个比较多的栅格裁剪问题，整理如下：


我们只有由于栅格与矢量数据的存储模型不相同，这就导致栅格数据的像元无法与矢量数据的点等同，从而导致裁切后的对齐问题，放大数据我们就能发现，如下图可以说明：（其中黑白色为栅格数据，每个正方形代表一个像元，红色区域为矢量面数据。）

![](http://img.blog.csdn.net/20140729100755390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)




我们按照默认设置运行 Raster工具箱中的 Clip 工具，看看结果，蓝色的栅格部分：


![](http://img.blog.csdn.net/20140729101943691?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)






发现，栅格数据裁剪完，并不是需要的矢量数据范围，而是矢量数据压盖的最小栅格数据范围。



如果我们需要得到的栅格，是矢量数据的范围，该如何做呢？



**【旧版本】如果正在使用的是10.1以及更早期的版本：**


1. 首先将作为裁剪范围的矢量面（Feature）转为图形（Graphic），在ArcMap中，在面图层上右键，使用 Convert &nbsp;Features to Graphics... 菜单，如下图：

（Graphic 被选中状态下，周围是有几个小方块的，与 Feature 被选中的亮蓝色不同哦...）

![](http://img.blog.csdn.net/20140729103840234?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


2.在 ArcMap 中，使用图层的右键菜单中的Export功能，导出选中Graphic 范围内的数据：


![](http://img.blog.csdn.net/20140729105009187?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


看看结果，为了清楚，我将Graphic的填充色去掉，栅格数据左边与上边界是与矢量数据一致的，这样就尽最大范围保持了结果栅格与矢量数据范围的最大一致性：

**PS：有人会问，为什么下边和右边边界没有完全贴合？ 需要知晓，栅格数据的行列数是矢量数据长度整除像元大小（导出的像元大小默认与源数据相同，也可以根据需要修改）得出的，而通常有余数的存在，因此没有那么严丝合缝，归根结底还是两种数据的存储模型不同导致的。**

![](http://img.blog.csdn.net/20140729105334939?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



**【新版本】如果正在使用的是10.2以及更新期的版本：**



新版本中 Clip 工具提供了额外的参数，可以简单的勾选就完成了上面的需求：

![](http://img.blog.csdn.net/20140729110657623?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


**PS：一定要注意右边的帮助哇，为了尽可能满足矢量数据边界范围，行列数是通过计算调整，也就是像元大小相比原始数据会变化，像元值会进行重采样获取。**

看看结果吧，影线区域是矢量，玫红色区域是生成的栅格：





![](http://img.blog.csdn.net/20140729111546105?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)











最后来张全家福，对比下，哪种结果是你想要的，决定对应的选择哪种方法 ，（左侧图层顺序，即为右侧图层显示顺序）。





![](http://img.blog.csdn.net/20140729111953116?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)





