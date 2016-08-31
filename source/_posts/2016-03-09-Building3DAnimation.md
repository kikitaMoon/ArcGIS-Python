title: ArcGIS 构建3D动画方法
categories:
  - 木工开物
date: 2014-09-16 15:43:44
tags: [3D]
---


## **Ⅰ 以动画表现视图（View）**

**1 捕获透视图（Capturing perspective views）**

使用“动画”工具条中的“捕获视图”工具 捕获视图 可以捕获照相机视图，这些视图作为关键帧，保存在某个照相机轨迹或地图视图轨迹中。

生成的轨迹将成为关键帧之间的连续插值，从而创建平滑的动画。



![](http://img.blog.csdn.net/20140915114952093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

<br>

**2 录制导航（Recording Navigation）**

简单录制功能是通过使用与动画控制对话框中的视频播放器类似的控件来实现的。单击录制按钮录制导航。

![](http://img.blog.csdn.net/20140915150738233)

录制导航时，可使用 ArcScene 或 ArcGlobe 中的飞行工具飞行 来创建照相机轨迹。

![](http://img.blog.csdn.net/20140915154715022)


<br>



**3 创建关键帧（Creat KeyFrames）**

这种方法与捕获透视图相似，可以为当前视图进行快照，作为一个关键帧，可以插入到已有的轨迹中。

![](http://img.blog.csdn.net/20140915163702334)

在创建动画关键帧对话框上，使用相同的属性（如相同的照相机位置）创建多个关键帧，然后在动画管理器的“关键帧”选项卡上修改关键帧属性，细化动画创建。

如下例子，中通过创建两个相同的关键帧，控制照相机在某处的停留时间。

![](http://img.blog.csdn.net/20140915165444265)




<br>

**4 使用书签创建动画（Using Bookmark）**

将已经创建的书签作为关键帧也是个很好的方法，如果地图或者场景中以前做过书签，并且想把他们利用起来连贯的展现出来，就可以使用这种方法。

![](http://img.blog.csdn.net/20140915171129415)


<br>


**5 沿路径移动照相机或视图（Moving the Camera or View along a Path）**



我们还可以根据路径创建照相机轨迹或地图视图轨迹。所选线要素或图形可以用来定义路径，这样就将照相机的移动轨迹就约束在这个路径上。

例如下图所示：

![](http://img.blog.csdn.net/20140915174342992)

![](http://img.blog.csdn.net/20140915174826062)

<span style="font-family: 'Microsoft YaHei';">照相机的方向可由观察点和目标点这两个 3D 点定义。使用“根据路径设置照相机飞行路线”对话框上的“路径目标”选项可修改照相机的移动方式。有三个选项可用于沿路径移动照相机：

（1）沿飞行路径同时移动观察点和目标。

（2）保持当前目标沿路径移动观察点。

（3）保持当前观察点沿路径移动目标。

<br>

<br>

## **Ⅱ 以动画形表现图层属性**



创建图层轨迹的几种方式：


（1）图层透明度动画

使某些图层变得透明，以便其他图层能够随着动画的发展而可见；

方法：在创建关键帧的时候，设置图层的透明度百分比。

![](http://img.blog.csdn.net/20140916104353906)

![](http://img.blog.csdn.net/20140916104654513)


（2）图层可见性动画

关闭图层使之不可见。例如在某个时间，指定图层不需要显示；操作类似上面的，只不过截取关键帧的时候，打开/关闭图层即可，不赘述。


（3）**ArcScene** 中沿路径移动某个图层（例如汽车）

![](http://img.blog.csdn.net/20140916112832171)


（4）图层组动画

使用现有图层组，按照顺序播放一系列的图层，这个动画效果也比较常用，如果一个组中是相关的主题的一系列数据，通过播放，可以看到图层之间的演进关系。

![](http://img.blog.csdn.net/20140916141808812)




<br>

<br>


## **Ⅲ 以动画表现场景属性（ArcScene）**

这种动画类型是仅用于 ArcScene 的场景属性配置的。最常用的就是一天从日出到日落不同太阳位置的场景效果的连续播放。

我们要做的仅仅是在每个太阳位置时间点创建关键帧。

![](http://img.blog.csdn.net/20140916150957404)




场景属性设置：

![](http://img.blog.csdn.net/20140916151259409?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


![](http://img.blog.csdn.net/20140916151845168?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



![](http://img.blog.csdn.net/20140916151652734?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)




<br>

<br>



## **Ⅳ 以动画表现时态数据**

如果数据是含有时间字段的，我们还可以进行按照时间序列的播放时态数据的动画。

首先在图层属性中时间选项卡 **激活时态**。 然后创建时间动画。

![](http://img.blog.csdn.net/20140916152749859)

关于最后一个时间动画不想说很多，ArcGIS 有个关于时态的扩展模块，Tracking Analyst，这个扩展对于时态数据有更多的控制。

配置出的时间图层有更好的展现力，因此，这里就不再多说时间动画了。