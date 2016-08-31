title: ArcGIS Desktop 10.1 的系统自带的 prj 文件的去哪了?
categories:
  - 木工开物
date: 2013-04-22 09:33:33
tags: [Coordinate System]
---

在过去的版本，例如 9.31，10.0 我们在安装目录中可以找到存放系统 prj 的地址，例如 C:\Program Files (x86)\ArcGIS\Desktop10.0\Coordinate Systems\Projected Coordinate Systems。但是10.0之后，我们发现，这个文件夹消失了，那要得到其中的Prj文件怎么做呢？ 

现在的 Coordinate Systems 文件变成的虚拟的结构，prj 文件都存储在 projection engine library (pe.dll)。从安装包中去掉了4000+的 prj 文件，会提升安装的性能。

如果是自定义的 prj 文件， 可以将文件复制到 ArcMap Favorites 文件夹。 如果需要得到 prj 文件，可以将其添加到收藏，或者另存为副本。


收藏夹的位置：

`Win7 ：c:\Users\[login]\[Roaming | Local | etc]\AppData\ESRI\Desktop10.1\ArcMap\Coordinate Systems`

`WinXP： C:\Documents and Settings\[login]\Application Data\ESRI\Desktop10.1\ArcMap\Coordinate Systems`

文件夹中支持子文件夹进行分类。 

![](http://img.my.csdn.net/uploads/201304/22/1366594740_7184.jpg)

