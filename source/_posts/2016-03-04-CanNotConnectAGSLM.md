title: “连不上ArcGIS License Manager” 的一点常用诊断方法
categories:
  - 木工开物
date: 2015-11-27 18:00:41
tags: [License,Deployment]
---
在 ArcGIS Desktop 的问题库中，有一类不算做核心技术问题，但却可能会位列“最常见的问题”之一。简言之一句话，”**许可服务器连不上怎么办？！**“ 下面就来演绎下问题的诊断过程。

> 本文仅适用于客户端 ArcGIS Administrator 访问 ArcGIS License Manager **正式版**许可的问题的诊断，目前适用于 ArcGIS for Desktop 10.x、ArcGIS Engine 10.x、CityEngine 201x 版本的浮动许可诊断问题。博主说，你可能很难找到第二篇与ArcGIS Desktop 正版授权有关的博客了…… **单机版和破解版请绕行。**  


<br>

# 问题现象

ArcGIS License Manager **已经授权完毕且成功**，可用性（Availability）栏目中总计（Total）和可用（Available）的数目正常，服务器状态也运行正常。

![](http://img.blog.csdn.net/20151116115601903)


> 图中的过期栏目中的日期可忽略，内部工作使用的正式许可是限定有效日期的。如果你使用的是购买得到的正式版许可，这里会显示 永久（Permanent），也就是许可是永久有效的。

<br>

然而，在通过局域网访问许可服务器的其它机器上的 ArcGIS Administrator 中，连接许可服务器失败。

常见错误提示： **“机器名或者IP”does not have a valid Licesne Manager. Please enter a valid License Manager Server.**


<br>


# 诊断思路

我们可以结合一些初级的网络知识，按照如下思路测试，大多数情况下，你不需要依次全做完，就发现问题已经解决或至少找到了问题的原因。

<br>

**1. 从许可服务器本机入手**

如果情况允许，最好在许可服务器本机也安装 ArcGIS Desktop 程序，然后使用 ArcGIS Administrator 连接本机许可服务器，各次分别填写 localhost，本机IP，本机机器名，检查是否有问题。一般如果本机连接不上，就不要期待其它机器可以正常连接了。

**常见处理方法： **
在ArcGIS License manger 中执行：重读许可服务 --> 停止许可服务 --> 启动许可服务 
确保 ArcGIS Administrator 中许可类型选择正确，如 Advanced ，Standard ，Basic。

<br>


**2. 确保网络连通**

可以使用**ipconfig /all**观察本地网络设置是否正确。

可以使用 **ping** 命令测试下网络情况

 - **ping 127.0.0.1** 如果本地址无法Ping通，则表明本地机TCP/IP协议不能正常工作。ArcGIS的许可走的是TCP/IP 协议
   
 - **ping本机IP地址** 这样是为了检查本机的IP地址是否设置有误
   
 - **ping本网网关或本网IP地址** 这样的是为了检查硬件设备是否有问题，也可以检查本机与本地网络连接是否正常

如果这时遇到错误提示，就该向自己单位的 IT 寻求帮助了。有了通畅的网络环境，ArcGIS许可才能有效通讯。

<br>

**3. 确认端口可用**

如果网络通畅，然而还是无法连接许可服务器，肿么办？！那就再稍微往下深一步，博主的知识量有限，但是好奇心和倔强还是迫使她尽可能地再努力多做一点。

在”[**许可服务管理器指南**](http://desktop.arcgis.com/zh-cn/desktop/latest/get-started/license-manager-guide/configure-the-arcgis-license-manager-to-work-through-a-firewall.htm)“中提到，”**默认情况下，将 lmgrd 后台程序设为端口 27000**“。那么，连不上许可服务器是因为端口被锁定了吗？ 有可能，动手查查才放心。

听说，netstat是控制台命令,是一个监控TCP/IP网络的非常有用的工具。那么动手吧。

以管理员的身份运行命令窗口，并输入命令：**`netstat -abn`** 

![](http://img.blog.csdn.net/20151116192648563)

如果找到 27000 和 lmgrd.exe 这个进程 ，并且状态 Established，可以认为端口正常。

![](http://img.blog.csdn.net/20151116193145451)

<br>

27000-27009是ArcGIS License Manger 的默认端口段，是相对不拥挤的段。但是，如果发现这个端口被其他程序占用了，那么就要修改ArcGIS许可服务器或者其它程序的端口了。在这里我就只能说说 ArcGIS 许可服务器的端口的修改方法了。

>**如何修改 ArcGIS 许可服务的端口？**
>在 ArcGIS license manager 的安装目录下，bin目录下，找到 service.txt，打开如下样子：
>![](http://img.blog.csdn.net/20151116194427255)
>
>修改这个配置文件，例如：在 SERVER 行的结尾处，您可选择直接在 ANY 后面指定端口号。在 VENDOR 行上，添加 PORT=####，其中 #### 是指定的特定端口号，用来将供应商后台程序锁定到特定端口，例如 1234。
>![](http://img.blog.csdn.net/20151116194749476)
>
>这样我们可以在客户端使用例如 **27004@许可服务器IP或机器名** 的方式访问许可。


<br>

再看客户端机器，如果机器上有 telnet 客户端，那么还可以试试 telnet 命令测试远程主机的端口是否可用。

例如：**`telnet 192.168.100.115 27000`**，其中假设许可服务器IP为 192.168.100.115。

如果返回黑屏，仅左上角光标闪烁，那么可以认为可用。

如果不幸提示，”Connecting to 192.168.100.115……Could not open connection
 to the host on port 27000. Connect Failed. ”

关掉许可服务器和客户端机器的防火墙试试，确认是否可以正常访问。如果真的是防火墙作祟，我们可以在防火墙上创建个例外规则，确保27000端口可以穿过防火墙。windows 防火墙的例外规则创建看看 windows 的帮助吧，点 [**这里**](http://windows.microsoft.com/zh-cn/windows/open-port-windows-firewall#1TC=windows-7)，我不叨叨了。如果单位里有更高级的防火墙或安全系统，需要配置例外规则，那么还是联系 IT 吧。

