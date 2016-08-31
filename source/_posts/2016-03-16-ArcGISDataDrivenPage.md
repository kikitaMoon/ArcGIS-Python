title: ArcGIS Data Driven Page
categories:
- 木工开物
date: 2013-06-26 10:08:20
tags: [Mapping]
---

通过 “Data Driven Page” 可以基于单个地图文档，快速创建一系列布局页面。按照图层中的各个索引要素，将地图分割为多个部分，分别生成相应的地图。


![](http://img.blog.csdn.net/20130621160054515?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


可见，索引要素是决定地图出图的重要部分，常见的索引方式，例如：网格索引，带状索引等等。

![](http://img.blog.csdn.net/20130621160204953?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![](http://img.blog.csdn.net/20130621160217000?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


Data Driven Page 工具条上的设置，主要也是来配置索引图层，那索引图层如何制作？


![](http://img.blog.csdn.net/20130621161409515?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


![](http://img.blog.csdn.net/20130621161556203?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)&nbsp;


ArcGIS 提供了一系列制作和准备 Data Driven Page 的 GP工具。

![](http://img.blog.csdn.net/20130621163458796?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

此工具可以创建可用作索引的矩形格网面，如下图所示，其中格网的标注表示了PageName：

![](http://img.blog.csdn.net/20130624143335796?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


索引网格面的属性表：

![](http://img.blog.csdn.net/20130624143556187?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

格网索引在于给有数据的位置创建期望网格大小的矩形要素，不仅适用于面要素，点，线也同样的，如下：

&nbsp;&nbsp;![](http://img.blog.csdn.net/20130624144405546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

&nbsp;&nbsp;![](http://img.blog.csdn.net/20130624144417343?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


# 2. Strip Map Index Feature

该工具可根据单个线状要素或一组线状要素，创建一系列矩形面索引要素。用于根据线状要素定义一幅带状地图或一组地图中的页面。

![](http://img.blog.csdn.net/20130624151936156?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


对应生成的索引数据中，属性表中很好的记录了各幅地图的对应关系，Angle 记录了数据框需要旋转的角度，如下图：

![](http://img.blog.csdn.net/20130624152042125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


# 3. Calculate Adjacent Fields

此工具最常用于填充地图册中相邻页面的标注字段。此工具将向输入要素类追加八个新字段（每个字段表示八个罗盘点中的一个：北、东北、东、东南、南、西南、西和西北）。

例如 Field Name 选择为“PageName”，创建的新字段名：

“PageName_N”、“PageName_NE”、“PageName_E”、“PageName_SE”、“PageName_S”、“PageName_SW”、“PageName_W”和“PageName_NW”。

![](http://img.blog.csdn.net/20130624154314546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)


<br>

# 4. Calculate Central Meridian and Parallel

此工具基于要素范围的中心点计算中央经线和标准纬线。这个工具又几个注意事项：

（1）直接对没有投影的要素类运行此工具将会产生错误。要素类必须进行**投影**。

（2）**坐标系字段**必须是文本字段，并且字段长度应大于或等于 600 个字符。

在新字段中添加了文本坐标信息，格式类似如下：

```
<span style="background-color:rgb(204,204,204)">PROJCS[&quot;World_Mercator&quot;,GEOGCS[&quot;GCS_WGS_1984&quot;,DATUM[&quot;D_WGS_1984&quot;,SPHEROID[&quot;WGS_1984&quot;,6378137.0,298.257223563]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433]],PROJECTION[&quot;Mercator&quot;],PARAMETER[&quot;False_Easting&quot;,0.0],PARAMETER[&quot;False_Northing&quot;,0.0],PARAMETER[&quot;Central_Meridian&quot;,-118.525225741025],PARAMETER[&quot;Standard_Parallel_1&quot;,46.76032322895251],UNIT[&quot;Meter&quot;,1.0],AUTHORITY[&quot;ESRI&quot;,54004]]

```

<br>

# 5. Calculate&nbsp;Grid Convergence Angle

此工具根据要素类中各要素的中心点计算偏离正北方向的旋转角度（网格收敛角），并将所得值填充到指定字段中。这样就方便了，将地图旋转到正北方向。

此工具替代了&nbsp;Calculate Geodesic Angle（计算大地线角度）。输入数据需要指定有效的投影坐标系。

计算角度的算法提供了三种：

- GEOGRAPHIC — 以正北方向作为起点，顺时针旋转的角度。这是默认设置。
- ARITHMETIC — 以正东方向作为起点，逆时针旋转的角度。
- GRAPHIC — 以正北方向作为起点，逆时针旋转的角度。

了解网格收敛角，放图一张：

![](http://img.blog.csdn.net/20130626095349828?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

<br>

# 6. Calculate UTM Zone

根据中心点计算每个要素的 UTM 带，并在指定字段中存储该空间参考字符串。



（1）需要一个足够长（&gt; 600 个字符）的新的文本字段。

（2）为了得到最佳结果，输入要素的基准面应与数据框使用的基准面相同。

（3）该工具不执行任何地理变换。

在新字段中的复制内容，类似如下：

```
<span style="background-color:rgb(204,204,204)">PROJCS[&quot;GCS Beijing 1954 UTM Zone 51R (Calculated)&quot;,GEOGCS[&quot;GCS_Beijing_1954&quot;,DATUM[&quot;D_Beijing_1954&quot;,SPHEROID[&quot;Krasovsky_1940&quot;,6378245.0,298.3]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433]],PROJECTION[&quot;Transverse_Mercator&quot;],PARAMETER[&quot;False_Easting&quot;,500000.0],PARAMETER[&quot;False_Northing&quot;,0.0],PARAMETER[&quot;Central_Meridian&quot;,123.0],PARAMETER[&quot;Scale_Factor&quot;,0.9996],PARAMETER[&quot;Latitude_Of_Origin&quot;,0.0],UNIT[&quot;Meter&quot;,1.0]]
```


关于数据驱动制图就说这么多了，主要是整理了帮助中的关键点，配以了实例截图做说明，帮助理解。