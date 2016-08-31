title: ASCII 栅格的显示
categories:
  - 木工开物
date: 2015-04-21 18:25:39
tags: [Raster,Geodata]
---
今天刚好有人问到一个有关 ASCII 栅格数据的问题，这里梳理下，用最简单的方式极速理解。

<br>

>**什么是ASCII栅格？**      就是用ASCII文本记录的栅格数据……
>
>**怎么得到ASCII栅格？**   比如使用工具 Raster to ASCII……

<br>

<br>






一般在 ASCII 栅格的文件头中我们会看到这几行：

![](http://img.blog.csdn.net/20150421172716734)

**ncols**  和 **nrows**   表示这份数据的行列数，这份数据是10×10。

**xllcorner** 和 **yllcorner** 表示的就是栅格的左下角（low left）角点的坐标。

**cellsize** 也就是像元大小，表示每个正方形单元的尺寸。

通过这几个值不就确定了栅格数据的范围了吗？嗯，确定了。

<br>

看图说话：

![](http://img.blog.csdn.net/20150421175341113)


<br>

文本文件下面的值就对应到每个格子里的像元值：

![](http://img.blog.csdn.net/20150421182308665)




<br>
<br>
我想你不会再有any疑问了……

