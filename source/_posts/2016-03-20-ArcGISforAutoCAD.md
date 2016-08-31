title: ArcGIS for AutoCAD 小结

categories:
  - 木工开物

date: 2012-02-07 14:42:00
tags: [CAD,Geodata]

---


**一、 简介**
 ArcGIS for AutoCAD是Esri提供的一个针对AutoCAD免费插件。此插件可以使AutoCAD作为ArcGIS Server的客户端加载服务；并且可以作为GIS结构编辑器来组织CAD数据，从而作为直接可用的GIS 要素类；给CAD数据定义坐标系，可以被ArcGIS产品识别。

<br>

**二、 系统要求**

这里基于ArcGIS for AutoCAD 250版本。 


| 版本 | AutoCAD 2010/2011, 32-bit or 64-bit |
| AutoCAD Map 3D 2010/2011, 32-bit or 64-bit |
| AutoCAD Civil 3D 2010/2011, 32-bit or 64-bit|
| 操作系统| Windows 7 Enterprise, Ultimate, Professional, or Home  Premium|
|   Windows Vista Enterprise, Business, Ultimate, or Home  Premium (SP1 or later) |
|   Windows XP Professional or Home edition (SP3)|
|   Microsoft .NET Framework | 

Microsoft .NET Framework Version 3.5 (SP1 or later) |
|   Internet 方式连接ArcGIS Server |   ArcGIS Server 9.3 或更高版本发布服务 |

<br>

**三、 安装与加载**

下面以AutoCAD 2010（x64），ArcGIS for AutoCAD 250（x64）为例，介绍一下此插件的安装使用过程。

**1. 获取并安装插件**

插件的下载地址：[http://support.esrichina-bj.cn/2011/0224/963.html](http://support.esrichina-bj.cn/2011/0224/963.html)
 注意此插件区分32bit与64bit，选择合适版本下载，我这里使用ArcGISforAutoCADDownloadx64.exe。
 在已经安装AutoCAD的前提下，双击运行此exe即可。

**2. 插件的加载**

以管理员身份运行AutoCAD，在AutoCAD的命令提示行中输入：NETLOAD。出现资源管理器窗口，浏览至插件的安装目录，选择 ArcGISForAutoCAD.dll打开。

![](http://hi.csdn.net/attachment/201202/7/0_13285965249kvZ.gif)

之后出现插件加载画面。

![](http://hi.csdn.net/attachment/201202/7/0_13285965280rkE.gif)

加载ArcGIS for AutoCAD插件成功。

加载后，会多出ArcGIS for AutoCAD插件栏，如下图：
![](http://hi.csdn.net/attachment/201202/7/0_1328596532oOIs.gif)

**注意事项：**

添加ArcGIS Online服务时，可能会遇到错误：“找不到资源：‘**basemapui\basemapcenter.xaml’**”。

解决方法：这是个已知问题，下载补丁既可以解决此问题，地址：[http://resources.arcgis.com/zh-cn/content/patches-and-service-packs?fa=listPatches&PID=129](http://resources.arcgis.com/zh-cn/content/patches-and-service-packs?fa=listPatches&PID=129)

至此，ArcGIS for AutoCAD 插件即可以开始使用啦。



**四、 功能与使用**

**1. Map Service**

有了这个插件，首先可以使AutoCAD直接加载Map Service：

(1) ArcGIS Online

使用Esri Map Gallery中的地图作为地图，添加到现有的CAD工程中。

![](http://hi.csdn.net/attachment/201202/7/0_1328596539aaOf.gif)

(2) ArcGIS Server

向现有的CAD工程中添加ArcGIS Server服务。

![](http://hi.csdn.net/attachment/201202/7/0_13285965457sCz.gif)


**2. CAD Feature Class**


此插件可以将 AutoCAD 作为 GIS 方案编辑器，用来将 CAD 数据组织为可供 GIS 使用的要素类。

类型对象过滤器是预定义的，用来约束ArcGIS Desktop支持的feature class与DWG 对象的对应关系。

DWG 对象与ArcGIS 要素的强制对应关系如下：




| Feature type | DWG object types   |
| Point | Point, Insert,  shape, Hatch, Proxy   |
| Polyline | Arc, Circle,  Ellipse, Line, Mline, polyline, 3D polyline Ray, spline, Xline, Trace, solid,  3Dface   |
| Polygon | Circle, Solid,  Ellipse, Face, closed polyline, closed 3D polyline, Mline   |
| Annotation | Text, Mtext,  Attribute, Attdef   |
| Multipatch   | Arc, Circle,  Ellipse, Line, Mline, polyline, 3D polyline Ray, spline, Xline, Trace, solid,  3Dface   |


**3.坐标系统**

插件使用的坐标系统是通过*.prj 文件来定义的。当给DWG文件定义坐标系后，这个有效的空间参考是可以被ArcGIS Server、ArcMap、ArcCatalog以及ArcGIS 地理处理工具识别的。


关于CAD与ArcGIS一体化的文章，后面会不断更新~

