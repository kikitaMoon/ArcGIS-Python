title: 在Linux上安装ArcGIS许可管理器备忘录
categories:
  - 木工开物
date: 2015-06-10 13:00:00
tags: [License,Deployment,Linux]
---
> 这篇文章中使用的环境信息：
> 
> Red Hat Enterprise Linux Server release 6.4 
> Red Hat Enterprise Linux Server release 5.8
> ArcGIS License Manager 10.2.2
> Xmanager 5

<br>

#### **★ 安装之前一定要了解系统要求，这一步很重要，这里不啰嗦，详情点 [这里**](http://resources.arcgis.com/en/help/system-requirements/10.2/#/ArcGIS_10_2_for_Desktop/015100000002000000/)。


<br>


# 1. 准备安装文件

我的Linux服务器是虚拟机，没有光驱，选择ftp上传安装文件。一般在各种linux的发行版中，默认带有的ftp软件是vsftp。

检查vsftpd软件是否安装， **# rpm -qa|grep vsftp**
启动 vsftp 服务，**# service vsftpd start**

![](http://img.blog.csdn.net/20150609112137795)

使用ftp客户端上传 ArcGIS License Manager （LM）安装包。如果上传的 iso 镜像文件之后使用 mount 命令挂载，其实也可以仅将光盘中 LicenseManager 目录下的 linux 文件夹上传，此文件夹为 LM 的Linux安装包。

包含如下几个文件（夹）：

![](http://img.blog.csdn.net/20150609133902347)



<br>

<br>


# 2. 创建账户

ArcGIS License Manager 不允许 root 账户安装，因此要创建一个其它账户，例如：arcgis

![](http://img.blog.csdn.net/20150609135308102)



>PS : 如果使用 root 账户直接安装，则会遇到错误提示：
>
>![](http://img.blog.csdn.net/20150609134235240)



<br>

<br>

# 3. 创建 Trusted Storage目录并赋权

在安装 ArcGIS License Manager 之前，需要手动创建用于存储许可 Trusted Storage File (TSF) 的目录，具体目录为：“/usr/local/share/macrovision/storage” 

创建目录：

![](http://img.blog.csdn.net/20150609143802102)

为目录赋权：

![](http://img.blog.csdn.net/20150609143826797)


> 如果不创建这个目录而直接安装 LM 程序，就会遇到 Fatal Error 提示：
> 
> ![](http://img.blog.csdn.net/20150609150050870)

<br>

<br>


# 4. 安装 ArcGIS License Manager

<br>

有图形界面模式和静默模式两种安装模式，建议选择前者：

## **Option 1 图形界面安装**

安装 ArcGIS License Manager 需要 X Windows Display的支持来进行图形界面的交互。尽管我们可以选择使用静默安装和静默授权，但是在许可管理过程中，还是会用到图形界面。强烈建议安装个 Xmanager，来连接Linux主机。

设置DISPLAY环境变量 :  
例如： **$ export DISPLAY=*192.168.100.115*:0.0**

运行 Setup 文件开始安装，建议使用精细模式（Verbose Mode），这样如果安装失败，我们可以通过运行过程中的消息判断问题的所在。例如，没有创建必要的目录，没有安装必要地包，没有足够的权限，等等问题。

**$ ./Setup -v**

![](http://img.blog.csdn.net/20150610101655247)

稍等片刻，即弹出界面：

![](http://img.blog.csdn.net/20150610101939297)

后面按照向导，下一步即可，此处省略100字……


<br>

## **Option 2 静默安装**

如果选择静默安装也可以，例如：

**$ ./Setup -m silent -v -l Yes**

![](http://img.blog.csdn.net/20150609152846016)


>**如果需要了解安装ArcGIS 许可管理器的选项：**

> -m  silent/gui  静默安装/图形界面
> -v   精细模式
> -h   帮助
> -e   示例
> 静默安装专用选项：
> -l    Yes/No 是否同意许可条款
> -d   安装目录


<br>

<br>

# 5. 授权许可

LM安装完成之后，需要进行许可的授权，事先将自己的许可文件 *.prvs 上传到Linux主机中。

<br>



仍然建议GUI mode 授权，运行LM安装目录中的 SoftwareAuthorizationLS 程序：

![](http://img.blog.csdn.net/20150610104255198)


稍后弹出界面：

![](http://img.blog.csdn.net/20150610110055851)

后面按照向导，下一步即可，可以参考windows的授权手册，此处省略100字……

<br>

运行 LSAdmin 程序可以打开 License Manger ，查看和管理许可。

<br>

<br>

<br>

# 相关资源整理



FAQ:  What are the best practices when installing and troubleshooting Esri software on Linux?

http://support.esri.com/em/knowledgebase/techarticles/detail/42921

HowTo:  Silently authorize ArcGIS License Manager 10.x on Linux


http://support.esri.com/es/knowledgebase/techarticles/detail/38412

