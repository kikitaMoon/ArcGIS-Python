title: 栅格数据中的 Zone 与 Region
categories:
- 木工开物
date: 2014-09-01 17:22:00
tags: [Raster]
---

Zone 与 Region 在字面上都是区域的意思，但是在做分析与统计的时候二者却是有区别的。


**什么是Zone？**


简而言之，具有相同值的像元就属于一个Zone。也就是，Zone由栅格中所有具有相同值的像元组成，分区可以由相邻像元和/或不相连像元组成。如下图一目了然：

![](http://img.blog.csdn.net/20140901161928822)



**什么是Region？**

一个Zone内的每组相连像元都可视为一个Region</span>。ArcGIS 中提供了从 Zone 获得 Region 的工具 Group Region。

![](http://img.blog.csdn.net/20140901162814668)

![](http://img.blog.csdn.net/20140901165652590)&nbsp;&nbsp;![](http://img.blog.csdn.net/20140901165743384)



**工具的工作顺序：** 扫描的第一个区域接收值 1，第二个区域接收值 2，依此类推，直到所有区域都已赋值。扫描将按从左至右、从上至下的顺序进行。赋给输出区域的值，取决于系统在扫描过程中是在什么时候遇到它们的。

**与原始Zone的关系：** 默认，生成的数据的属性表中会有 LINK 字段，记录Region从Zone的来源：

![](http://img.blog.csdn.net/20140901163437009)