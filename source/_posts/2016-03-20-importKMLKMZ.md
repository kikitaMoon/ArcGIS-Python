title: KML/KMZ到ArcGIS完全转化

categories:
  - 木工开物

date: 2012-02-07 13:50:13

tags: [Geodata]

---


在ArcGIS中，做KML（Keyhole Markup Language）的导入，我们可以使用两种方法：一是ArcToolbox中的转换工具；二是数据互操作扩展。本文将以ArcToolbox中的工具为例来导入KML或KMZ。当然如果没有数据互操作扩展的用户，第一种方法也是首选。 在ArcToolbox中有转换工具（Conversion Tools）下的由KML转出（From KML）下的KML转图层（KML to Layer）。 

![](http://hi.csdn.net/attachment/201202/7/0_1328593945F1fw.gif)

此工具将会把KML或KMZ文件的数据，转换到FileGDB中的数据集中，数据的展现符号化等信息存储在同名的图层文件（.lyr）中。 

![](http://hi.csdn.net/attachment/201202/7/0_1328593963qh7q.gif)

注意：此工具中，仅需要选择一个目的文件夹，GDB和lyr文件都会自行创建。 其实到这里，KML文件中包含的信息已经进入ArcGIS的怀抱了。 如果有特殊需要，就Export下，可以得到shape。 

![](http://hi.csdn.net/attachment/201202/7/0_1328593969H3qk.gif)

另外，ArcGIS 提供了导出成KML、KMZ的工具：       

- 图层转KML（Layer to KML）       
- 地图转KML（Map to KML）

