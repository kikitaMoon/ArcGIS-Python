title: 在ArcGIS中创建Python工具（二）
categories:
  - 木工开物
date: 2015-09-02 22:19:20
tags: [Python,Geoprocessing]
---
上一篇中我们了解到有两种方式在 ArcGIS 中创建 Python工具，这一篇就来看看如何在标准工具箱中创建脚本工具。

<br>

ArcGIS Help 中脚本工具的帮助过于枯燥，在这里，我以一个具体的实例来总结构建脚本工具的过程，我要实现的需求是做个快速实现羽化边界效果的小工具，预期得到如下的效果：

![](http://img.blog.csdn.net/20150901105340859)


上面效果在ArcMap中完全可以手工运行几个工具实现，但是过程稍微繁琐，那么需求来了，如何做个自定的一键生成羽化边界的小工具？

<br>


<br>

# 1 准备Python脚本文件


第一步，先写好脚本工具的核心 —— python脚本文件。

<br>

>脚本中我希望根据指定环间距自动生成一个9环的缓冲面，然后添加一个字段，用于存储给各个缓冲面的透明度百分比。
>
>看下图就知道我想做什么了：
>
>![](http://img.blog.csdn.net/20150901114428476)


<br>

写一个py文件，将要用到的工具串联起来实现自己的需求，大致是下面的样子。这不是最终要做成脚本工具的版本，只是为了预先了解要如何实现，后面还要修改。

```python
__author__ = 'kikita'

# FileName: EasyFeathering.py

import arcpy
# arcpy.env.workspace = "D:\something\Data.gdb"

# Script Tool Parameters
InputFeature = "InterestArea"
OutputFeature = "OutFeathering"
SingleRingWidth = 10000

# Some Predefined Parameters
distances = []
level = 9
bufferUnit = "meters"
NewField = "Percent"


# My Easy Feathering function
for i in range(level):
    distances.append(SingleRingWidth*(i+1))
    i = i+1

print  str(distances)
print  "Distance Complete!"

arcpy.MultipleRingBuffer_analysis(InputFeature, OutputFeature, distances, bufferUnit, "", "ALL","OUTSIDE_ONLY")
print  "Success to execute Multi Ring Buffer."

arcpy.AddField_management(OutputFeature,NewField,"double")
print "Success to add Transparency Percent Field."

arcpy.CalculateField_management(OutputFeature, NewField, "!OBJECTID! *10", "PYTHON", "")
print "Success to Calculate Transparency Percent Field."
```

<br>

<br>

# 2 脚本工具参数配置

有了py文件之后，如何把它塞进工具箱里呢？

在ArcMap的Catalog窗口中，找一个自己喜欢的任意文件夹，新建一个Toolbox，然后右键  Add --> Script，进入向导，这些操作如果不了解，可以点 [**这里**](http://desktop.arcgis.com/zh-cn/desktop/latest/analyze/creating-tools/adding-a-script-tool.htm) 查查帮助，照着做即可，不赘述。

![](http://img.blog.csdn.net/20150902133957962)

这里我主要说说参数传递。

我希望做好的工具中，我只去指定三个参数，分别是：输入的兴趣区域面（input Feature ），多环缓冲的环间距（Single Ring width ），输出结果（output Feature ）。预览下工具界面：

![](http://img.blog.csdn.net/20150902103754748)

<br>

那么问题又来了，这三个参数如何从工具界面传给真正执行工具的 python 脚本？我们需要对前面的脚本参数定义部分做个修改，使用 arcpy 提供的 **`GetParameterAsText()`**函数即可在工具界面和脚本之间传递参数。用下面的代码替换前面对这三个参数的替换：

```python
# Script Tool Parameters
InputFeature = arcpy.GetParameterAsText(0)
SingleRingWidth = arcpy.GetParameterAsText(1)
OutputFeature = arcpy.GetParameterAsText(2)
```
对应的脚本工具参数配置：

![](http://img.blog.csdn.net/20150902221147899)


>为工具配置参数的时候，有2个原则需要遵守：
>
 - 工具对话框中的参数顺序必须与脚本中的**参数顺序一致**。
 - 每个脚本工具参数都有关联的**数据类型**。ArcGIS的地理处理不会将值发送给数据类型不正确的脚本，从这点上看，脚本工具比下一篇要说到的脚本工具箱多了一个优势，就是，在参数值发送给脚本之前会有数据类型检验。

<br>

修改Python脚本文件后，现在就运行工具，发现可以得到预期的结果：

![](http://img.blog.csdn.net/20150902103702924)

<br>

但是有点不完美，就是在工具的运行过程中，工具给我返回的信息并不充足，我只知道 “Running Script EasyFeathering …”，而不了解工具在做什么，执行到了哪个步骤。这不是好的体验。

![](http://img.blog.csdn.net/20150902103827046)


<br>

<br>

# 3 消息

工具和用户之间的所有沟通均通过消息来实现。接着上一步提出的问题，如何在工具进度窗口中传递消息给用户？

虽然在开始调试脚本的时候，如开头代码所示，我加了些 Print 语句，方便我了解自己的脚本独立执行时的状态，但是如果运行脚本工具，这些print语句是看不到的。可以使用 ArcPy中提供的有关消息的函数，`AddMessage`、`AddWarning`、`AddError`等向工具进度条界面发送消息。这里我做了个简单的步骤的消息性提示，以及，如果结果没有记录输出，会提示警告。

```python
__author__ = 'kikita'

# FileName: EasyFeathering.py

import arcpy

#arcpy.env.workspace = "D:\IncidentSupport2015\something\Data.gdb"

# Get the input values from tool UI
InputFeature = arcpy.GetParameterAsText(0)
SingleRingWidth = arcpy.GetParameterAsText(1)
OutputFeature = arcpy.GetParameterAsText(2)


# Some Predefined Parameters
distances = []
level = 9
bufferUnit = "meters"
NewField = "Percent"


# My Easy Feathering function
for i in range(level):
    distances.append(int(SingleRingWidth)*(i+1))
    i = i+1
arcpy.AddMessage("Step1 Distance list Complete!")


arcpy.MultipleRingBuffer_analysis(InputFeature, OutputFeature, distances, bufferUnit, "", "ALL","OUTSIDE_ONLY")
arcpy.AddMessage("Step2 Success to execute Multi Ring Buffer.")

arcpy.AddField_management(OutputFeature,NewField,"double")
arcpy.AddMessage("Step3 Success to add Transparency Percent Field.")

arcpy.CalculateField_management(OutputFeature, NewField, "!OBJECTID! *10", "PYTHON", "")

InputFeatureCount = int(arcpy.GetCount_management(OutputFeature).getOutput(0))
if InputFeatureCount == 0:
    arcpy.AddWarning("{0} has no features.".format(OutputFeature))
else:
    arcpy.AddMessage("Step4 Success to Calculate Transparency Percent Field.")

```

<br>

这样在工具的执行过程中，我就收到了消息：

![](http://img.blog.csdn.net/20150902132309261)

到这里，工具的功能部分就完成了。

<br>

<br>

# 4 显示结果图层

 我进一步希望脚本工具运行之后，自动显示在当前的地图文档中，从而避免重复设置透明度的操作。

<br>

1. 为输出参数配置模板图层。

![](http://img.blog.csdn.net/20150902221424828)

2. 在处理设置中，激活设置

![](http://img.blog.csdn.net/20150902133052065)

这样在运行工具之后，结果即自动添加显示。

![](http://img.blog.csdn.net/20150902133211213)

<br>

<br>


# 5 配置路径


如果是在本机使用脚本工具，一般我们会使用绝对路径，但是如果希望分享自己的工具给别人，就要考虑路径问题，也就是新用户运行脚本工具时，相关的脚本文件和其他用到的资源能否访问到。我的工具按照如下的结构组织：

![](http://img.blog.csdn.net/20150902221643912)

<br>

在脚本工具的属性中，可以配置存储相对路径引用 py 文件：

PS：但是不要想太多，这个设置仅仅会将脚本文件所在位置按照相对路径存储，而不会将脚本内部的路径进行转换。

![](http://img.blog.csdn.net/20150902160448246)

<br>

这个示例中我还需要用到一个图层文件作为模板，如果希望使用相对路径使用，就建议将符号化信息写在脚本内部，而不是在参数窗口中配置。所以，要继续修改下Python脚本文件。

在脚本文件的最后追加两行代码，我这里将获取与Python脚本文件在相同目录下的lyr文件：

```python
# Layer files are located in same folder as the .py file
PythonFilePath = os.path.dirname(__file__)
params = arcpy.GetParameterInfo()
params[2].symbology = os.path.join(PythonFilePath, "FeatheringEffectTemplate.lyr")

# Pass message 
arcpy.AddMessage("Finding Feathering Effect Template Layer ..." +"/n"+ os.path.join(PythonFilePath, "FeatheringEffectTemplate.lyr"))


```

OK，路径的问题就解决了。

<br>

<br>

# 6 帮助文档

还可以进一步为工具添加帮助文档，让更多的人了解如何使用这个工具。

在ArcCatalog 或者ArcMap的Catalog 中，在脚本工具上右键，点击 Item Description 菜单，点击 Edit 就可以对工具的帮助文档进行编辑。

![](http://img.blog.csdn.net/20150902141327675)


这样当别人打开你的工具时，就看到帮助喽。

![](http://img.blog.csdn.net/20150902141411941)

<br>

<br>

<br>

好啦，关于ArcGIS 中使用脚本工具的过程就说到这里。

