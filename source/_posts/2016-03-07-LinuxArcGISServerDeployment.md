title: Linux 下安装 ArcGIS Server 前的准备工作备忘录
categories:
  - 木工开物
date: 2015-05-08 16:55:01
tags: [Linux,Deployment]
---
>**安装环境： ArcGIS for Server Linux 10.2.2 ， Redhat 6**



因为是在网络虚拟机中安装部署，首先需要一个远程Linux的客户端，这里使用 putty，可以在官方的 [www.putty.org](http://www.putty.org/) 下载，但是貌似网站被墙了，我也放了一份在[我的资源](http://download.csdn.net/detail/kikitamoon/8675531)中。


**1） 运行 putty.exe ,登陆linux服务器**：

![](http://img.blog.csdn.net/20150508115206894)


**2） 输入用户名密码，登入服务器：**

![](http://img.blog.csdn.net/20150508115217999)


**3） 查询主机的 IP 地址：**

![](http://img.blog.csdn.net/20150508115648332)


**4） 查询 hostname：**

![](http://img.blog.csdn.net/20150508134333079)

**5） 编辑hosts文件，映射IP地址和主机名：**

![](http://img.blog.csdn.net/20150508134841008)


**6） 创建 ArcGIS Server 账户：**

![](http://img.blog.csdn.net/20150508135007495)

>备注： 
/etc/group 中存储了用户组信息，格式如下：
用户组名:组密码:GID:组内帐号（多个帐号用逗号分隔）
/etc/passwd 中存储了用户账户信息，格式如下：
用户名:密码:UID:GID:用户信息:HOME目录路径:用户shell
其中UID为0则是用户root，1～499为系统用户，500以上为普通用户


**7） 为ArcGIS Server 账户设置密码：**

![](http://img.blog.csdn.net/20150508135449733)


**8）在home目录下创建ArcGISServer目录，授权 ArcGIS Server账户对文件夹的权限：**

![](http://img.blog.csdn.net/20150508145916462)

**9）文件句柄和进程的硬限制要求**

要增加软限制和硬限制，需要使用超级用户访问权限编辑 /etc/security/limits.conf 文件。例如，添加以下四行：

![](http://img.blog.csdn.net/20150508151219321)

**10） 将安装程序上传到Linux主机**

Linux主机是个网络虚拟机，也没有光驱，就用上传安装包（iso镜像）的方式安装了。一般在各种linux的发行版中，默认带有的ftp软件是vsftp。

检查vsftpd软件是否安装， # **rpm -qa|grep vsftp**

![](http://img.blog.csdn.net/20150508140953677)

启动 vsftp 服务，# **service vsftpd start**

![](http://img.blog.csdn.net/20150508140842226)

其它命令：
      停止ftp：service vsftpd stop
      重启ftp：service vsftpd restart

软后用ftp客户端连接服务器即可，这里我用了以前一直用的 FileZilla.

![](http://img.blog.csdn.net/20150508145639903)


**11） 挂载 ISO映像**

![](http://img.blog.csdn.net/20150508153633696)
PS：第一次mount没写完整的路径信息，文件没找到，请忽略，看最后一行。

**12）执行安装前的环境检测**

![](http://img.blog.csdn.net/20150508165045601)


各项检测通过，可以安装 ArcGIS Server 了。