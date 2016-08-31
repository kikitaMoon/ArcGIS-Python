title: 单独打开CityEngine本地帮助
categories:
  - 木工开物
date: 2013-03-22 11:21:19
tags: [CityEngine]
---

CityEngine软件的自带帮助中有大量的信息可供查找学习，但是自带的 Help Content，正常是在启动CE后，再去打开才可以，这与 eclips 的帮助是一个道理。

有时仅仅为了看看帮助，而启动着庞大的CE，有点喧宾夺主喽。在老王的帮助指导下，找到了单独运行CE帮助的方法，磨刀不误砍柴工~ 在这里总结下。
	

<br>

# 一、设置系统环境变量

1. 在“系统变量中，设置3项属性，JAVA_HOME, PATH, CLASSPATH （大小写无所谓)）, 若已存在则点击“编辑”，不存在则点击“新建”；	

 - JAVA_HOME：例如：C:\Program Files\Esri\CityEngine（CE的安装目录即可，下面有 bin 和 jre 文件夹）
 - PATH：%JAVA_HOME%/bin;%JAVA_HOME%/jre/bin
 - %JAVA_HOME%/lib/dt.jar;%JAVA_HOME%/lib/tools.jar （要加.表示当前路径）

PS：%JAVA_HOME% 就是引用前面指定的JAVA_HOME；
	
关于配置环境变量的详情，可参阅：http://blog.csdn.net/huanghm88/article/details/3965218
	
![](http://img.my.csdn.net/uploads/201303/22/1363921744_3779.jpg)


2.键入命令 java，出现画面，说明环境变量配置成功；

![](http://img.my.csdn.net/uploads/201303/22/1363921765_9021.jpg)

<br>

# 二、单独运行帮助

制作个启动脚本--bat文件。

内容如下：

------
```
C:\Program Files\Esri\CityEngine
cd %ehome%
C:
java -classpath plugins\org.eclipse.help.base_3.5.2.v201009090800.jar org.eclipse.help.standalone.Help -command displayHelp
pause
```
------

PS：蓝色部分仍然是 CE 的安装目录，下面包含 jre，bin 等目录。

关于单独使用eclipse帮助的详情：http://hi.baidu.com/caichaowei/item/4ab4ccb8e8304cd385dd7917

<br>

# 三、更改CE程序文件名

上面的脚本运行之后，也许会报错，找不到 eclipse.exe。

可以将CityEngine.exe，做个副本，重命名之，变成一位伪eclipse.exe。

![](http://img.my.csdn.net/uploads/201303/22/1363922351_2165.jpg)	
然后运行上一步中的 bat 脚本，单独的CE帮助就跳出来了~

<br>

CE进入esri怀抱已久，相信风格会越来越接近 ArcGIS 核心产品，现有的WebHelp链接如下：

http://cehelp.esri.com/help/index.jsp?topic=/com.procedural.cityengine.help/html/toc.html	

<br>

**郑重鸣谢：~ ~ [菩提老王](http://blog.newnaw.com/) ~ ~**


