title: 浅谈使用ArcPy执行大数据量处理任务
categories:
  - 木工开物
date: 2016-04-28 12:31:40
tags: [Geoprocessing,Python]
---



Python功能强大而易于学习。对于ArcGIS for Desktop用户来讲，Python是提高工作效率的不二选择。 

[Arcpy](http://desktop.arcgis.com/zh-cn/arcmap/latest/analyze/arcpy/what-is-arcpy-.htm)是esri提供的用于高效数据处理分析、制图等的Python站点包。 利用ArcPy，我们可以在ArcMap的Python窗口交互执行脚本，还可以创建自定义脚本工具或脚本工具箱，还可以在ArcGIS之外运行独立脚本，享受更纯正的python体验。

这一篇说说如何利用Python批量执行数据处理任务，这个问题也是前段时间遇到的用户的实际问题，比较有价值。


# 需求

还是从实例开始……

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_BatchClip.png-kikitaMaps)

有一个简单但耗体力的裁剪任务，希望通过大量面分割（逐一裁剪）大量的数据，类似Split工具要完成的任务，并且要按照一定的规则命名将分割结果输出到指定的位置，例如要求有指定前缀。



# 实现

例如，一种思路是逐一遍历面要素，然后去裁剪目标数据再输出，这时你可能会遇到下面的小问题：

**我如何通过ArcPy获取要素的几何？**

在ArcPy中提供了一个数据访问模块/Data Access (arcpy.da)，我们可以通过游标（Cursor）来查询要素的几何或属性。在这个需求中是逐一遍历面要素的几何，我们选择 SearchCursor，通过 **`SHAPE@`** 可以访问要素的几何。 

语法： `SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})`

了解详细的帮助信息点[这里](http://desktop.arcgis.com/zh-cn/arcmap/latest/analyze/arcpy-data-access/searchcursor-class.htm)。

那么可以把函数主体定义成这样，即可实现需求：


```python
def MyBatchClip(Parameter):
    # 参数
    inputFC = Parameter[0]
    ClipArea = Parameter[1]
    OutputWS = Parameter[2]
    Prefix = Parameter[3]
    # 字段列表，SHAPE@ 访问要素几何对象
    Fields = ['FID','SHAPE@']
    # 遍历面要素逐一裁剪目标数据并输出自定义前缀的结果。
    with arcpy.da.SearchCursor(ClipArea,Fields) as cursor:
        for row in cursor:
            outputFC = os.path.join(OutputWS, Prefix+str(row[0])+'.shp')
            arcpy.Clip_analysis(inputFC, row[1], outputFC)

```


# 多进程

如果这个批量任务是大量的，**如何更高效地开动起来？**

这里按照esri以前的一篇 [Blog](https://blogs.esri.com/esri/arcgis/2012/09/26/distributed-processing-with-arcgis-part-1/) 提到的方法分享给大家，使用Multiprocessing模块并行处理。 [Multiprocessing](https://docs.python.org/2/library/multiprocessing.html#) 模块是Python的一个标准库，通过这个库，我们可以利用多核CPU，来实现多进程处理大数据量的任务。 

可以通过 `multiprocessing.Pool` 来使用进程池，Pool类可以管理固定数目的进程，默认是开启和机器CPU数目相同的进程。

> 语法：
> `multiprocessing.Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])` 
> processes表示pool中进程的数目，默认地为当前CPU的核数。
> initializer表示新进程的初始化函数。
> initargs表示新进程的初始化函数的参数。
> maxtasksperchild表示每个进程执行task的最大数目



把脚本修改下，加上多进程处理的部分：


```python
# -*- coding:utf-8 -*-
__author__ = 'kikita'

import arcpy
import timeit
import time
import multiprocessing
import os

arcpy.env.workspace =  r'D:\LearnAboutPython\MyPythonProject\UsingCurser\DemoDataS.gdb'
arcpy.env.overwriteOutput = True

# 批量裁剪函数
def MyBatchClip(Parameter):
    # 参数
    inputFC = Parameter[0]
    ClipArea = Parameter[1]
    OutputWS = Parameter[2]
    Prefix = Parameter[3]
    # 字段列表，其中 SHAPE@用于访问数据几何
    Fields = ['OBJECTID','SHAPE@']
    with arcpy.da.SearchCursor(ClipArea,Fields) as cursor:
        for row in cursor:
            outputFC = os.path.join(OutputWS, Prefix+str(row[0])+'.shp')
            arcpy.Clip_analysis(inputFC, row[1], outputFC)
            print Prefix+str(row[0])+'.shp'


if __name__ == '__main__':
    # 参数
    OutputWS = r'D:\LearnAboutPython\MyPythonProject\UsingCurser\OutputWS'
    # SDE库输出
    #OutputWS = r'C:\Connection131.sde'
    Parameter1 = ['CountyPoints','Area_A',OutputWS, 'AAA_']
    Parameter2 = ['hyd_line','Area_B',OutputWS, 'BBB_']
    Parameter3 = ['River_line.shp','Area_C.shp',OutputWS,'CCC_']
    Parameters = [Parameter1,Parameter2,Parameter3]
    # 当前CPU核数
    print 'CPU Count:' + str(multiprocessing.cpu_count())
    # 进程池
    MyGPpool = multiprocessing.Pool()
    # 多进程并行处理
    StartTime = time.time()
    results = MyGPpool.map(MyBatchClip,Parameters)
    EndTime = time.time()
    print 'Elapsed:  ' + str(EndTime - StartTime) + '  Seconds...'

```

**结果**

```
CPU Count:8
AAA_0.shp
BBB_0.shp
CCC_0.shp
BBB_1.shp
AAA_1.shp
CCC_1.shp
BBB_2.shp
AAA_2.shp
CCC_2.shp
……
……
……
BBB_28.shp
AAA_27.shp
BBB_29.shp
CCC_28.shp
CCC_29.shp
AAA_28.shp
BBB_30.shp
CCC_30.shp
AAA_29.shp
AAA_30.shp
Elapsed:  28.628000021  Seconds...
```

# 一点有用的提示：

1.在使用Multiprocessing时，注意数据锁定（Schema Lock）的问题，例如这个例子中，当输出工作空间选择为FileGDB时出现异常。 使用文件夹输出 Shapefile，或者以SDE数据库作为输出工作空间，都是可以的。

2.我在代码中也加入了计时，用于比较并行与否的耗时情况。 但是有时确实会发现，较简单的处理任务时，多进程并行并不比单进程快，因为导入模块和启动进程都需要花时间。 


**参考：**
https://blogs.esri.com/esri/arcgis/2012/09/26/distributed-processing-with-arcgis-part-1/
https://docs.python.org/2/library/multiprocessing.html#using-a-pool-of-workers
https://www.binpress.com/tutorial/simple-python-parallelism/121
http://cloga.info/python/2014/01/12/PythonMultiprocessingintro/
http://kmdouglass.github.io/posts/learning-pythons-multiprocessing-module.html
http://broadcast.oreilly.com/2009/04/pymotw-multiprocessing-part-2.html