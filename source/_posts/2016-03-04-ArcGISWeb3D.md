title: 实践 ArcGIS Web 3D
categories:
  - 木工开物
date: 2016-01-17 10:45:37
tags: [3D,Web,ArcGIS Pro]
---
ArcGIS 产品家族的 Web 3D 功能众多用户期待已久，从 ArcGIS 10.3.1 版本开始，Esri 放了个大招，千呼万唤始出来的 Web 3D 功能，终于不再犹抱琵琶半遮面了。 那到底如何将创建和发布3D场景呢？ 下面就把今天的测试过程记录下。

<br>



# 测试环境

**硬件**

- 处理器：Intel Core i7 4710MQ @ 2.50GHz
- 内存：16G
- 显卡：NVIDIA GeForce GT 730M

**OS**

- Windows  10  Pro

**软件**

 - ArcGIS Pro 1.1.1    **（必要）**
 - ArcGIS for Server 10.3.1   **（必要）**     
   包括：
  - Portal for ArcGIS 
  - ArcGIS Web Adpter (IIS)
  - ArcGIS Data Store
 - ArcGIS for Desktop 10.3.1
 - CityEgnine 2015.2

<br>

<br>


# 不可不知的先决条件

**1**.  首先确保自己的环境满足系统要求，这是非常重要的、不可忽略的条件之一，详情参考如下文档：

  **ArcGIS for Server 系统要求**
  http://server.arcgis.com/zh-cn/server/latest/install/windows/arcgis-for-server-system-requirements.htm

   **ArcGIS Pro 系统要求**
   http://pro.arcgis.com/zh-cn/pro-app/get-started/arcgis-pro-system-requirements.htm

<br>

**2**. ArcGIS 的 Scene Service 是一种新的 Web 服务类型，这种服务来自于 ArcGIS Pro，并且要求创建和发布 Scene Service 的**ArcGIS Pro是1.1或将来的更高版本**。  也就是说， 目前传统的ArcGIS for Desktop 是不能创建和发布Scene Service的。

<br>

**3**. 从 **ArcGIS for Server 10.3.1** 版本才开始了Scene Service 的支持。也就是，略早的 10.3 版本也是不可以的哦。为了发布3D数据（Multipatch）和2D数据作为门户中的托管场景图层，**必要的安装组件有 Portal for ArcGIS，ArcGIS Data Store** 。 其中，ArcGIS Data Store 用于存储 Scene Service 中所使用的场景图层切片缓存。

<br>

**4** 将 ArcGIS Server 与门户联合；并且将 ArcGIS Server 指定为门户的托管服务器。

![](http://img.blog.csdn.net/20160116212543218)

**具体如何配置？** 参考帮助文档，这里不赘述，虽然略有繁琐但有章可依：

**联合 ArcGIS Server 站点与门户**
http://server.arcgis.com/zh-cn/server/latest/administer/windows/federate-an-arcgis-server-site-with-your-portal.htm

**配置托管服务器**
http://server.arcgis.com/zh-cn/server/latest/administer/windows/configure-hosting-server-for-portal.htm



<br>

<br>

# 创建和发布Scene Service 的过程

<br>

**1. 打开 ArcGIS Pro ，创建场景，加入场景数据。其中建筑物模型为 File Geodatabase 中的 Multipatch Feature Class。**

   ![](http://img.blog.csdn.net/20160117094645043)


<br>

**2. 确保连接并激活 Portal，且自己的账户有创建内容、发布托管要素和发布托管场景的权限。**

    > 这里需要说明下，目前，只用 Portal for ArcGIS 才支持发布 Multipatch 数据源的 Scene Service。 ArcGIS Online 暂不支持。如果大家的 ArcGIS Pro 是60天试用版本的许可，默认激活的门户是ArcGIS Online，需要添加并切换到一个可用的Portal。
    

   ![](http://img.blog.csdn.net/20160117095515339)

<br>

**3. 确保ArcGIS Pro 中场景的打开方式是 Global View。如果是 Local View ，也可以切换。**

   ![](http://img.blog.csdn.net/20160117102209200)


<br>


**4. 分享场景，分析服务，确保没有 Error，如果有，需要事先修复。**

  ![](http://img.blog.csdn.net/20160117102833162)

<br>

**5. 等待完成，确保Job目录中所有任务全部成功完成。**

  ![](http://img.blog.csdn.net/20160117103404271)

  根据数据量的不同，带宽的不同，硬件配置的不同，整个发布服务的过程时间长短不一。

  我的这个测试中共89个精细程度不一的建筑物模型，发布全过程大约耗时1分钟，供参考。

  ![](http://img.blog.csdn.net/20160117104133951)



<br>

<br>


# Web 前端访问服务

ArcGIS Scene Viewer 需要支持 WebGL 的桌面 Web 浏览器，WebGL 是用于渲染 3D 图形的 web 技术标准。 

点 **[这里](get.webgl.org)** 测试浏览器是否启用了 WebGL，请打开 get.webgl.org； 要解决与 WebGL 相关的问题，请访问 WebGL [**疑难解答**](http://get.webgl.org/troubleshooting/)。

ArcGIS Scene Viewer 支持这些 web 浏览器：**Chrome，Firefox，Internet Explorer 11，Safari**。我这里使用的是 Chrome 是 Version 47.0.2526.111 m (64-bit)。

<br>

好像还不错哦

![](http://img.blog.csdn.net/20160117105659303)

表示树木的 Feature Layer 可以在 Web 端修改渲染

![](http://img.blog.csdn.net/20160117105852973)

再凑近看看细节

![](http://img.blog.csdn.net/20160117105734693)

再换换底图，做几个Slide

![](http://img.blog.csdn.net/20160117110003999)


<br>

<br>

刚好这个周末比较清闲，可以用比较连续的时间做了测试，效果还算令人满意，后面我会再做些大数据量的测试，有空再更新。

