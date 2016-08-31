title: CityEngine 中的 Annotation
categories:
  - 木工开物
date: 2013-05-13 16:29:40
tags: [CityEngine]
---

CityEngine中的 Annotation 可以给规则和属性添加额外的信息，Annotation不会影响到规则本身的语法以及模型的产生，它主要影响的是用户界面的显示，例如：在Inspector 上，如何显示属性和规则。




**@StartRule:**

在起始规则选择器中标记起始规则，通常会变成粗体。

```
@StartRule
Start-->NIL
```

**@Hidden:**

标记一个属性或者规则隐藏，在 Inspector 中或者起始规则选择器中不显示。

```
@Hidden
attr hide_me = 0
```

**@Group("level_1-group", ..., "level_n-group"):**

设置属性的在 Inspector 中的分组显示。

```
@Group("First", "Second")
attr grouped = 0
```

**@Range(min, max):**

设置某个属性的最大、最小值，控制属性的范围。

```
@Range(5, 50)
attr height = 20
```

**@Range(item_1 = value, ..., item_n = value):**

设置某个属性的指定选择项，值可以是数值型或者文本型。

```
@Range(Low=0, Mid=1, High=2)
attr lod = 0
@Range(Red="#ff0000", Green="#00ff00", Blue="#0000ff")
attr color = "#000000"
```

**@Color:**

在 Inspector 中显示某个色彩属性使用色彩选择器。

```
@Color
attr userColor = "#000000"
```

**@File:**

将某个属性标记为一个文件名，在 Inspector 中以文件选择器显示。

```
@File
attr asset = "myfile.obj"
```

**@File("ext_1", ... , "ext_n"):** 

将某个属性标记为一个文件名，在 Inspector 中以文件选择器显示，规定指定的扩展名("ext_1", ... , "ext_n")。

```
@File("tif", "tiff")
attr texture = "tex0.tiff"
```

**@Directory:** 

将一个属性标记为路径名，在 inspector 中，会显示路径选择器。

```
@Directory
attr assets = "/assets/lod" + lod
```

**@Location(x, y):** 

为可视化 CGA 编辑器设置某个属性或者规则 2D 位置。

```
@Location(0, 0)
Init-->NIL
```

**@Order(order):**

设置在 Inspector 中属性的显示顺序。

```
@Order(1)
attr i_m_1st = 0
@Order(2)
attr i_m_2nd = 0
@Order(3)
attr i_m_3rd = 0
```

**@Description("description"):**

为某个属性或者规则添加描述，这些描述会在 Inspector 中产生工具提示，或者在起始规则选择器中，或者样式管理器中作为描述显示。

```
@Description("The building width")
attr width = 40
```

