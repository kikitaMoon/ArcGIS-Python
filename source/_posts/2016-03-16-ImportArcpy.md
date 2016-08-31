title: 在ArcGIS Desktop 中导入 Arcpy
categories:
- 木工开物
date: 2013-07-02 16:01:37
tags: [Python]
---


在导入 ArcPy 之后，可以运行随 ArcGIS 安装的标准工具箱中的所有地理处理工具。

`import arcpy`

<br>

# 1.导入整个模块

模块通常是一个包含函数和类的 Python 文件。

ArcPy 包括数据访问模块 (arcpy.da)、制图模块 (arcpy.mapping)、ArcGIS Spatial Analyst 扩展模块模块 (arcpy.sa) 和 ArcGIS Network Analyst 扩展模块模块 (arcpy.na)。

```
import arcpy.mapping
```

Python 的核心 os 和 sys 模块，也可使用此命令。例如：

```
import os
import sys
```


<br>

# 2.导入模块的一部分 

如果只导入某一模块的一部分，可以使用 from-import 语句。

```
from arcpy import env
env.workspace = "c:/data"
```

使用from-import-as 的形式，为其制定名称。

```
from arcpy import env as ENV
ENV.workspace = "c:/data"
```

再来个例子：

```
from arcpy import mapping as MAP
mxd = MAP.MapDocument("C:/maps/basemap.mxd")
```

<br>

# 3. 导入模块全部内容

模块的内容将被直接导入到命名空间中，随后无需添加前缀。在某些情况下，from-import-* 可以简化代码。


```
# Import arcpy and the sa module as *

import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
# Get input parameters
#
inRaster1 = arcpy.GetParameterAsText(0)
inRaster2 = arcpy.GetParameterAsText(1)
inRaster3 = arcpy.GetParameterAsText(2)
outRaster = (Raster(inRaster1) + (Raster(inRaster2) - Raster(inRaster3)))
```