title: Troubleshooting： 有防火墙的情况下你需要如何部署许可服务器？
categories:
  - 木工开物
date: 2016-06-17 16:11:33
tags: [License,Deployment]
---


防火墙是一种有效的安全策略，如果部署ArcGIS许可的环境中不允许关闭防火墙，你可能会遇到这个错误：ArcGIS administrator 连不到许可服务器，提示错误， “ *“xxx.xxx.xxx.xxx”没有有效的许可管理器。请输入一个有效的许可管理器服务器。* ”

那么，如何解决这个问题？ 如下。


<br>


# 1  找到 Service.txt 文件

在许可服务器所在的机器上，默认位于：C:\Program Files (x86)\ArcGIS\License10.x\bin 目录下。 打开之后，类似下图：

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ServiceTXT1.png-kikitaMaps)

通过修改此配置文件可以控制ArcGIS许可服务器后台进程使用哪个端口。


<br>


# 1Plus   知其所以然

如果你对问题的原因不感兴趣，那么直接跳至2。  

ArcGIS License Server Administrator（旧称ArcGIS License Manager）的后台进程有两个：**lmgrd.exe** 和 **ArcGIS.exe**，用于响应客户端获取许可的请求。

> 在 Service.txt 文档中：
>
> 第一行配置的是 **lmgrd.exe** 这个进程的端口，默认是 27000，自 10.3 版本之后，有效范围仅可以是 27000-27009 这个几个端口号之一；
> 
> 第二行是用于 **ArcGIS.exe** 进程的端口配置，**默然情况下，这个端口是动态的，系统可以使用任何监听到的空闲端口**。 



我们用个小工具来检测一下，**Process Explorer**，官网下载点**[这里](https://technet.microsoft.com/en-us/sysinternals/processexplorer.aspx "Process Explorer")**，即可一目了然。在安装有 ArcGIS License Manger 的测试机上的执行小工具，抓取有用的信息：


![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_lmgrd.png-kikitaMaps)



从结果中可以得到，ArcGIS.exe 采用了 49479 这个端口与其他客户端通信。 在下次 ArcGIS License Service 启动时，这个端口会动态选择另一个。 这也就是问题的 key point，为什么用户即使在防火墙中开放了27000，甚至 27000-27009段的端口，然而许可服务器还是连不上。

<br>


# 2  锁定后台进程端口号

前文提到 ArcGIS.exe 端口是动态的，为了方便防火墙的设置，锁定端口是最简单有效的方法。

在 Service.txt 文件中，第二行结尾增加 PORT=<端口号> 的参数。 例如我选择 50000 ，如下图：

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ServiceTXT2.png-kikitaMaps)


修改完成，保存txt，重启 ArcGIS License Service ，然后过一会再去抓信息，发现 ArcGIS.exe 的端口号已经被锁定为 50000 ，变成静态。

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ArcGIS_Daemon.png)


<br>


# 3  在防火墙中创建规则放行端口

现在需要做的仅是，在防火墙上建立白名单，设置规则允许 27000 和 50000 端口的 TCP/IP 协议通信即可。 

<br>

这个配置方法在 [**官方文档**](http://desktop.arcgis.com/en/license-manager/latest/configure-the-arcgis-license-manager-to-work-through-a-firewall.htm) 中有很清楚的说明，如果感兴趣也一起看看。


