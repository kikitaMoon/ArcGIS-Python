title: ArcPad 10 使用与同步 ArcGIS Server 的数据全攻略（一）

categories:
  - 木工开物

date: 2012-04-09 14:13:00
tags: [ArcPad]

---


在移动设备上，使用ArcPad可以创建、显示、查询、编辑数据。根据工作流模式的不同，我们可以采取不同的数据组织形式。

首先，先了解下ArcPad 支持哪些数据格式：

> 1. ShapeFile；
> 2. ArcPad AXF 文件： 这个文件使用了SQL Server 精简版数据引擎，所以在上一篇中说部署时，需要安装SQL Server Compact for Windows Mobile；
> 3. ArcPad Graphics layer：用XML写的文件，可以储存 annotation, points, lines, and polygons；
> 4. ArcPad Photo layer：用XML写的文件，用于存储引用的照片信息，需要和照片文件放置在同个文件夹中；
> 5. ArcPad StreetMap 文件
> 6. Raster layers，具体支持以下格式:	
>   - JPEG (*.jpg)
>   - JPEG 2000 (*.jp2)
>   - MrSID Generation Two, or MG2 (*.sid)
>   - MrSID Generation Three, or MG3 (*.sid)
>   - Portable Network Graphics, or PNG (*.png)
>   - Tagged Image File Format, or TIFF, including GeoTIFF (*.tif)
>   - Windows Bitmap (*.bmp)
>   - CADRG raster maps


<br>
	

- 如果想要进行“从0开始”的外业作业方式，可以在ArcPad 中创建快速工程（包含了点、线、面三个shapefile层）。
- 如果已有 shapefile 数据，只需将这些数据拷贝到移动设备中，在ArcPad添加数据时引用即可。这与ArcGIS Desktop是一致的。
- 如果已有本地Geodatabase数据，这时，也可以使用ArcPad数据管理工具条Check out数据，然后通过check in提交数据。
- 如果是企业级的应用，可以与ArcGIS Server 、ArcGIS Desktop 联合使用，使用ArcPad加载已发布的服务，并且进行版本编辑，同步服务器数据。


以上提到的四种应用的场景，前三种比较好理解，也易于操作。所以最后一种，作为本文的主要总结对象，网上ArcPad的资料相对较少，遂决定梳理一下这种情况下授权、管理、编辑数据的全过程，一共我会分两次与大家分享。

	
	
# 一、激活ArcPad Data Manager扩展


必须先了解的是ArcPad Data Manger工具条。这个工具条是在PC上安装ArcPad时，自动安装的一个ArcGIS Desktop的扩展。

既然是扩展，当然首选需要激活，在ArcMap的菜单栏中，Custom -- Extensions -- 勾选 “ArcPad Data Manager”，如下图：

![](http://my.csdn.net/uploads/201203/29/1332984466_3620.png)
	
这一扩展包含了ArcPad Data Manager 与 ArcPad Tools两部分，分别位于工具条与ArcToolbox工具箱中。

![](http://my.csdn.net/uploads/201203/29/1332987320_6723.png)
![](http://my.csdn.net/uploads/201203/29/1332987399_7606.png)

	
# 二、为 ArcGIS Server 授权数据


用于授权给ArcGIS Server的数据是有要求的，必须满足以下条件：

（1）SDE GDB；（2）含有Global ID；（3）注册为版本。


点击 ![](http://my.csdn.net/uploads/201203/29/1333003545_9071.png) Author Project for ArcGIS Server”，进行数据授权。

![](http://my.csdn.net/uploads/201203/29/1333005687_5773.png)

选择需要签出的数据， 

![](http://my.csdn.net/uploads/201203/29/1333005691_5691.png)

设置空间参考范围，以及生成ArcPad地图文档的名称， 

![](http://my.csdn.net/uploads/201203/29/1333005694_5511.png)

设置完成后，会提示正确信息： 

![](http://my.csdn.net/uploads/201203/29/1333013109_2267.png)

至此，ArcPad 数据的准备就完成了。 下一篇文章，会进入 ArcGIS Server with ArcPad Capability 的发布，ArcPad如何加载和使用ArcGIS Server 服务的主题。


