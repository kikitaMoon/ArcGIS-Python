title: Linux下安装绿色版Oracle客户端备忘录
categories:
  - 木工开物
date: 2015-05-26 12:40:27
tags: [Deployment,Linux]
---
> 环境及版本信息：
远程服务器- Redhat 6.4；Oracle 11g x64； ArcGIS Server 10.2；
本地机器- Windows 8.1

<br>
开始安装 12c 和 11g 的客户端，总是不满足系统需求，各种提示缺包，所以还是使用绿色版省心点。
<br>

# 1  

将Oracle绿色版客户端安装文件上传到 Linux 服务器（oracle-instantclient11.2-basic-11.2.0.1.0-1.x86_64.zip） ，并解压到自己指定的目录，如 Client。

![](http://img.blog.csdn.net/20150525154820077)


<br>


# 2  

由于安装Oracle客户端的目的是为了 ArcGIS Server 能够访问数据库服务器，所以对Client目录赋予 ArcGIS Server 账户（**arcgis**）的755权限。

![](http://img.blog.csdn.net/20150525155959691)


<br>

# 3 

修改环境变量，使得ArcGIS Server 能够使用这个客户端。

环境变量文件位于ArcGIS Server 安装目录中 usr文件夹下的 init_user_param.sh 。

![](http://img.blog.csdn.net/20150525175240628)

<br>

编辑init_user_param.sh，将Oracle客户端所在的目录配置到对应的环境变量中，保存退出。PS，不要忘记删除前面的**＃**……　默认所有的变量信息是被注释掉的。

![](http://img.blog.csdn.net/20150525175903506)


<br>

# 4  

重启 ArcGIS Server 服务。

![](http://img.blog.csdn.net/20150525180528976)

<br>


# 5   

然后到 ArcGIS Server Manger中或者 ArcGIS Desktop 的 Server Connection中去注册数据库试试。

![](http://img.blog.csdn.net/20150526123818581)


