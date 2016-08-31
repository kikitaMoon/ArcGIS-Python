title: Shapefile 的局限性
categories:
- 木工开物
date: 2014-02-27 11:10:06
tags: [Geodata]
---
Shapefile 是一种开放的非拓扑的简单几何数据类型，深受数据处理人员的喜爱。 Shapefile 利用 dBASE 文件格式（.dbf 文件）来存储属性，dBase这种上世纪80年代的数据格式，现在基本淡出舞台。 虽然Shapefile有万般好，但是，今天还是要来说说shapefile的局限性，也就是使用限制有什么，以便合理的选择使用Shapefile数据。



# **1. 文件容量限制：**

Shapefile 每个子文件都有大小最大不能超过 2 GB ，以点要素为例，最多约能存储 7000 万个。</span>



# **2. 不支持高级对象：**

Shapefile不支持注记要素类、关系类、拓扑关系、属性域和子类、坐标精度和分辨率等。

不支持通过参数定义的曲线（也称为圆弧曲线）。





# **3. 字段存储限制：**

Shapefile无法存储：空值，无法向上舍入数字，对 Unicode 字符串的支持不足，字段名称最长只能为 10 个字符，且在同一字段中无法同时存储日期和时间。

Shapefile支持的最大字段数为 255。若超出此上限，当转换为 shapefile 时只会转换前 255 个字段。

dBASE 文件不支持类型 blob、guid、全局 ID、坐标 ID 或栅格字段类型。

<br>

|包含空值的数据类型|空值替换|
|---|:---|
|数字 - 当工具需要输出“空”、无穷大或 NaN（非数字）时|-1.7976931348623158e+308（最大负值的 IEEE 标准）|
|数字（所有其他地理处理工具）|0|
|文本|“ ”（空白 - 无空格）|
|Date|存储为零，但显示为“<空>”|


# 4. 字段宽度限制：


|地理数据库数据类型|dBASE 字段类型|dBASE 字段宽度（字符数）|
|---|:---|:---:|
|对象 ID|数值|9|
|短整型|数值|4|
|长整型|数值|9|
|浮点型|浮点型|13|
|双精度|浮点型|13|
|文本|字符|254|
|Date|Date|8|


# **5. 性能限制&nbsp;**

由于形状压缩方法的不同，shapefile 所占用的空间可能为文件地理数据库或 SDE 的三到五倍。</span>

Shapefile 的空间索引效率较数据库低。这就意味着，同地理数据库要素类相比，空间查询耗时更长。当处理大量要素时，效率低。

dBASE 文件不支持 WHERE 子句，也不支持 SQL。

当保存所做编辑时属性索引会被删除，因此必须重新创建属性索引。


# **6. 多面体存储限制**

Shapefiles 支持多面体，但不支持以下多面体的高级功能：纹理坐标、纹理及部分色带、光线法向量。

详情参考：[http://resources.arcgis.com/en/help/main/10.2/index.html#/Geoprocessing_considerations_for_shapefile_output/005600000013000000/](http://resources.arcgis.com/en/help/main/10.2/index.html#/Geoprocessing_considerations_for_shapefile_output/005600000013000000/)