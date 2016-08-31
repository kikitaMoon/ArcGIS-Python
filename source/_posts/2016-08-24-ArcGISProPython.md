title: 在ArcGIS Pro 1.3之外运行arcpy独立脚本
categories:
  - 木工开物
date: 2016-08-31 09:06:23
tags: [Python,ArcGIS Pro]
---

# 背景

ArcGIS Pro像ArcMap一样，其中也嵌入了Python。 不同在于ArcGIS Pro采用了python较新的版本3.4，ArcMap仍然沿用2.x版本。 ArcGIS Pro 1.3版本开始Python环境有点小变化，为了方便包管理esri开始采用Conda。 并且不像开始 ArcGIS Pro 1.1，1.2 版本，需要单独安装Python for ArcGIS Pro，在1.3版本python包随ArcGIS Pro一同自行安装。

文档的原文摘过来能更好的理解esri采用Conda的意图：

> Python has a rich ecosystem of preexisting packages that can be leveraged within ArcGIS, but managing which packages are installed on a system can be a complex and time-consuming task, especially when working on multiple projects or trying to share code with others.
> 
> To leverage this versatility, the Python community has created methods to easily create projects in multiple versions of Python and simplifies the process of installing nearly all publicly available Python packages. Conda is the most popular and widely used Python package manager.

看到这里，你也也许和我有一样的疑问，**啥是Conda？** 点 [**这里**](http://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-conda.htm) 。这页文档是esri刚更新的内容，需要在英文语言版本文档中才能找到。

<br>

# 执行脚本

这些改变，对于习惯在 ArcGIS Pro 内部的脚本命令行中执行脚本的用户并没有多大影响。 但是如果已经习惯了在ArcGIS Pro 之外独立执行脚本，那如下的改变要注意下了。

ArcGIS Pro 的Python包不再是ArcMap默认安装的位置 `C:\Python27` ，而是安装在 `ArcGIS Pro的安装目录\bin\Python` 。

ArcGIS Pro 采用了的Conda环境为 **arcgispro-py3**，有几个方式可以访问这个环境。

<br>

## 1. **交互式执行python命令**

打开ArcGIS Pro安装目录下propy.bat文件，默认位于:
`"C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\propy.bat"`

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ProPythonCommand.png-kikitaMaps)

## 2 **执行py文件**


CMD打开命令行窗口，通过propy文件执行脚本，例如默认位置：
`"C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\propy" myscript.py` 
![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ProPythonPY.png-kikitaMaps) 
备注：MyScript内容就两行： `import arcpy`, `print("arcpy imported")`

## 3 **批处理py文件**

通过 call 函数来调用 propy 

`@echo Run my Python script
call "%PROGRAMFILES%\ArcGIS\Pro\bin\Python\Scripts\propy" myscript.py
@echo Finished`

例子：   
![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ProPythonBat.png-kikitaMaps)
备注： 三个脚本分别打印 AAA, BBB, CCC。

<br>

<br>

# 使用Python IDE

有一个好用IDE是件美好的事情，大家应该都有各自的真爱，我就不做任何推荐啦。 在Pro之外独立执行脚本导入arcpy站点包的时候，只要注意将Python解释器的路径指向正确即可。

如果你的机器上既安装了ArcGIS Desktop，又安装了ArcGIS Server或者ArcGIS Desktop的后台64位补丁包，并且又安装了ArcGIS Pro， 那么可能在机器上有多个Python环境。

我自己在用 Pycharm ，在需要导入 ArcGIS Pro 的python站点包时，注意指向： `"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"`

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ProPythonPycharm.png-kikitaMaps)


<br>

注意，在python IDE 中**不要**将解释器指向这个 python.exe , `["C:\Program Files\ArcGIS\Pro\bin\Python\python.exe"]`

否则你在导入 arcpy 模块时会遇到找不到模块的错误： **ImportError: No module named 'arcpy'**


<br>

最后推荐 [一篇esri的Blog](https://geonet.esri.com/docs/DOC-8359)，也详细的阐述的这件事。