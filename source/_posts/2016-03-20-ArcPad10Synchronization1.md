title: ArcPad 10 使用与同步 ArcGIS Server 的数据全攻略（二）

categories:
  - 木工开物

date: 2012-04-10 09:16:00
tags: [ArcPad]

---


继续上个话题，数据准备好了，我们就开始发布服务吧~

# **三、发布 ArcGIS Server 服务**

在进行到这一步的时候，我遇到过很多问题，有配置的问题，有数据的问题，有自己不够仔细的问题。这里总结下注意事项，帮助大家少走弯路。

> **TIPS：**
> **首先，ArcGIS Server服务器要安装ArcPad扩展，这个扩展在ArcPad安装光盘中有。**
> **ArcGIS Desktop 与 ArcPad 版本一定要对应：ArcPad 10.0对应ArcGIS Desktop、ArcGIS Server 10.0（.NET）; ArcPad 8.0对应ArcGIS Desktop、ArcGIS Server 9.3.1（.NET）。**
> **必须使用 ArcGIS Server for .NET Framework ，不支持 Java，许可级别必须是 Advanced版。**
> **将前面制作的MXD以及通过上一步方法得到的同名apo放置到C盘根目录文件夹下，例如C:/MXD。**
> **数据尽量使用ArcGIS Tutorial Data，以防止是数据本身问题导致服务发不成，以后调通了，再用自己的数据。**
> **发布服务，在你的GIS服务器连接上，右键 Add new Services。而不要直接在你的mxd上右键发布服务。**


好，记住了这些，就开始发布服务吧，步骤和以前发布服务的方法几乎没有差异，GO ON……

添加服务：

![](http://my.csdn.net/uploads/201204/01/1333264611_3056.png)

![](http://my.csdn.net/uploads/201204/01/1333264616_5607.png)

![](http://my.csdn.net/uploads/201204/01/1333264621_6414.png)

注意这一步要勾选 **ArcPad**，使得发布的 Map Service 可以被ArcPad所支持：

![](http://my.csdn.net/uploads/201204/01/1333264628_6586.png)

后面几步可以保持默认……

最后发布成功。

<br>

# **四、Arcpad 加载 ArcGIS Server 服务并使用数据**

保证移动设备网络与Server连通，可以使用Wifi、USB等等……

在移动设备上打开ArcPad：

![](http://my.csdn.net/uploads/201204/01/1333265757_2991.jpg)

在添加数据下拉列表中，选择”Add Data from Server“

![](http://my.csdn.net/uploads/201204/01/1333265650_7644.png)

类型选择 ArcGIS Server ArcPad Service，地址填写服务器地址，点击刷新按钮可以显示服务列表，注意服务器地址填写完整：

![](http://my.csdn.net/uploads/201204/01/1333265936_3696.jpg)

等待片刻，服务加载成功：

![](http://my.csdn.net/uploads/201204/01/1333266712_2138.jpg)


