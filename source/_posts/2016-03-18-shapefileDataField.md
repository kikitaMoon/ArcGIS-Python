title: 有关shapefile存储时间字段的问题
categories:
  - 木工开物
date: 2013-03-04 09:20:05
tags: [Geodata]
---

很多ArcGIS的用户会很疑惑，为什么excel或者其他数据库中的时间数据数据，例如15:40:30等这样的数据，转成shapefile数据后，这个日期字段中的值会变成12:00:00 ？

我们知道shapefile是基于dbase来存储的，通过dbf文件来存储属性字段，dbf支持的日期时间字段，实际上不是真正意义上的DateTime型，而是只能存储8位的日期型字段，也就是：YYYYMMDD。

所以，强烈建议用户，如果需要使用日期时间型字段时，请选用GDB数据类型。如果出于特定原因一定需要使用shapefile的。可以考虑新加字段，单独来存储时间，两种常用的方案：

- （1）将时间换算成秒，由某个数值型字段来存储。
- （2）分别使用三个字段来存储，时分秒数值。
 
 <br>

顺便提一嘴。GDB存储时间日期的格式为：yyyy-mm-dd hh:mm:ss AM or PM。至于ArcMap中日期的显示的样式，是由windows系统来控制的。例如：M/d/yy, MM/dd/yy, yy/MM/dd等样式。

关于shape文件的详细描述，请查看如下两个连接中的任何一个：

http://www.digitalpreservation.gov/formats/fdd/fdd000280.shtml

http://www.gdal.org/ogr/drv_shapefile.html

从中都会获得有用的数据描述。


在资源库中也上传了esri有关shapefile的描述文档。


