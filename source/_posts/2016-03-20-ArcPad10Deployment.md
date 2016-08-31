title: ArcPad 10 的安装部署

categories:
  - 木工开物

date: 2012-03-28 09:19:00
tags: [ArcPad]

---

ArcPad是安装在手持设备或者移动终端的一个外业ArcGIS产品，也就是说ArcPad是Esri的一款软件产品，而不是硬件设备哦。虽然不比ArcGIS Desktop功能复杂缤纷，但是对于野外作业、数据采集等工作来说，算是功能十分丰富了。

说到安装，首先要了解系统要求，[http://resources.arcgis.com/zh-cn/content/arcpad/10.0/system-requirements](http://resources.arcgis.com/zh-cn/content/arcpad/10.0/system-requirements)。ArcPad 仅支持 Windows Mobile 移动平台（5.0以上），最高可使用Windows Mobile 6.5。

<br>

> **说明：**

>   本文及后续有关ArcPad文章的截图说明的环境：
>     ArcPad 10.0.2 （Build 30）；
>     Windows Mobile 6.5 模拟器，[下载地址](http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=17284) ；
>     Windows Mobile 5.0 基于移动设备 Trimble Juno ST；
>     Windows 7 。





# 在PC上安装ArcPad

运行光盘，安装ArcPad。

![](http://my.csdn.net/uploads/201203/27/1332835219_3182.jpg)


页面中还有一项”ArcGIS Server ArcPad Extension“，此项可以先不安装，在用到添加ArcGIS Server 服务、同步数据时才会用的这一项。关于这一部分的功能、要求、应用等，以后抽时间整理一下。安装过程很简单不赘述。

安装过程中，提示填写注册码，可以忽略，那ArcPad就进入了评估模式，评估模式一切功能和正式版是相同的，只是使用时间为20分钟，超过20分钟ArcPad会自动退出。如果为了方便长时间使用，需要填写**注册码**。自己学习研究，就用这个吧：**~@RCP@DD00R~**。当然，商业用途和项目开发等要使用正式版的……


安装完成后，开始菜单中会出现：

![](http://my.csdn.net/uploads/201203/27/1332837066_9137.jpg)

其中，第一项ArcPad 10 for Windows 是PC端的ArcPad程序，功能上与移动端ArcPad是一致的。

第二项 ArcPad Deployment Manager 就是用来向手持设备部署ArcPad的。

<rb>

# **手持端 ArcPad 部署**

1.首先安装windows同步程序。

> Windows XP： 安装 Microsoft ActiveSync ；
> Windows vista 或 Windows 7： 安装 Windows Mobile Device Center。

2.上述程序安装好后，连接移动设备和PC，保证连接状态正常。

![](http://my.csdn.net/uploads/201203/27/1332839836_2746.png)  ![](http://my.csdn.net/uploads/201203/27/1332839828_5470.png)



3.打开 开始 — ArcGIS — ArcPad 10 — ArcPad Deployment Manager。

![](http://my.csdn.net/uploads/201203/27/1332840144_8460.jpg)


在这个窗口勾选需要安装的项即可：

**Arcpad for Windows Mobile** 是**必然**需要安装的；

- 如果需要移动设备的“桌面快捷方式“，**今日插件（Today-Plugin）**可以选择安装；
- 如果需要 ArcPad 中文界面，可以勾选安装相应**语言包**；
- **Samples**，示例数据是初学者探索Arcpad 的学习资源，如果需要并且存储足够，推荐安装；
- 如果需要用到数据的check in 、check out，**SQL Server Compact**也需要安装了；
- 如果涉及到一些脚本的应用 **VBScript Runtime**也需要安装；
- 剩下两个没说到的，**Streetmap **和 **Datum **的，不需要安装，不适宜国内用户的需求。



做好选择之后，点击”Deploy“，就开始了Arcpad的自动部署。当然过程中不要忘记响应移动设备的询问。


4.至此，Arcpad 安装完成。

在移动设备的 开始 -- 程序 中，打开ArcPad：

![](http://my.csdn.net/uploads/201203/27/1332857307_4859.gif)


<br>

O了，可以开始使用ArcPad了。

学习资源主要还是ArcPad 官方帮助，在线帮助：[http://help.arcgis.com/en/arcpad/10.0/help/index.html](http://help.arcgis.com/en/arcpad/10.0/help/index.html)。















