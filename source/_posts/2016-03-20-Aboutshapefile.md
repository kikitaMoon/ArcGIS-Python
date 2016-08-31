title: 有关shape文件的说明

categories:
  - 木工开物

date: 2012-02-07 14:04:00
tags: [Geodata]

---



shapefile 是存储地理信息的简单文件格式，但是工作中，常会接到用户的很多问题，这里把常见的汇总下。

**一、shape 文件到底可以多大？**

shapefile 的每个文件都不能超过 2 GB。也就是说，存储数据的 .dbf 与.shp 分别不能超过 2GB。但是，所有文件的总大小可以超过 2 GB。

**二、 shape 文件是怎么构成的？**

shape 文件用 ArcGIS 查看仅显示一个文件，但是用 windows 资源管理器查看就可能看到以下文件。

* .shp - 存储要素几何的主文件；必需文件。
* .shx - 存储要素几何索引的索引文件；必需文件。
* .dbf - 存储要素属性信息的 dBASE 表；必需文件。
* .prj - 存储坐标系信息的文件；由 ArcGIS 使用。
* .xml - ArcGIS 的元数据 - 用于存储 shapefile 的相关信息。
* .sbn 和 .sbx - 存储要素空间索引的文件。
* .fbn 和 .fbx - 存储只读 shapefile 的要素空间索引的文件。
* .ain 和 .aih - 存储某个表中或专题属性表中活动字段属性索引的文件。
* .atx - .atx 文件针对各个 shapefile 或在 ArcCatalog 中创建的 dBASE属性索引而创建。
* .ixs - 读/写 shapefile 的地理编码索引。
* .mxs - 读/写 shapefile（ODB 格式）的地理编码索引。
* .cpg - 可选文件，指定用于标识要使用的字符集的代码页。
* 强烈建议，对shape操作时，在 ArcGIS 中进行。

**三、 shape 中创建字段注意什么？**

不能对现有字段修改，可以新建字段包括自定义数据类型；字段名长度不要超过10，超过会被截断。

新建字段时，有三个参数可供设置：

- precision（精度）—— 数字字段中可存储的位数；
- scale（标度）—— 浮点或双精度类型字段中数值的小数点右侧的位数；
- length（长度）—— 字符型字段的文本字段的长度。

注意，long integer 当精度超过 10 时，会自动转为 Double 型。

相关资料：

由于shape文件是公开数据格式，可以很好来作为交换格式，这里有个技术描述可供下载：

[shape文件技术描述](http://download.csdn.net/detail/kikitamoon/4049221)

