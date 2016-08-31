title: Make Query Layer在Model Builder中的使用
categories:
  - 木工开物
date: 2016-06-30 18:11:33
tags: [Geodata]
---


前两天碰到一个关于在 Model Builder 中使用 Make Query Layer 工具的问题，“如何把Make Query Layer结果输入到下一个工具中？”  


> **TIPS**: 什么是 Query Layer？
> 
> 在ArcMap中，我们可以通过定义SQL语句创建Query Layer，来查询存储在DBMS中的空间数据或者非空间数据。 每次在ArcMap中显示或使用Query Layer时，都会执行查询，因此无需生成数据的副本或快照便可显示最新的信息，这尤其适用于处理频繁更改的动态信息。 Query Layer功能适用于 ArcGIS支持的所有DBMS。
> ~ 详请点这里看 [**帮助**](http://desktop.arcgis.com/en/arcmap/10.3/map/working-with-layers/what-is-a-query-layer-.htm)。


下面通过一个实例先来说明下Query Layer的使用场景。

为了阐述方便，我找了一份数据稍作修改来模拟这个问题，数据位于基于Oracle的ArcSDE数据库，一个空间数据为点要素类，一个非空间表。

点数据表示事件，每发生一次事件（例如报警电话）就记录一个点，假设理想情况下同一个地址的事件都是重合点，如下图高亮的记录； 非空间表中记录了各个地址的某项分值（例如警力配备得分）。

打开脑洞，假设你是警察局长，需求是，获取每个有完整信息的地址（例如，点位于路的左侧或右侧的信息）的报警电话数，并对比警力配备分值，用于后续的工作，例如指挥调配或者空间统计工作等等。这时，使用Query Layer是个好选择。

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_FeatureTable.png-kikitaMaps)

<br>

Query Layer 返回的记录集可以是包含空间信息的 Feature Query Layer ，也可以是非空间信息的 StandAlone Table。 那么，其实在回到文章开头的问题，**“如何把Make Query Layer结果输入到下一个工具中？” 这取决于“下一个工具” 接受的输入数据的类型是什么。**

<br>

假如后续工作中需要用到空间数据，例如进行热点分析，评估下犯罪高发区，那么就需要查询SHAPE空间字段。 如果忽略了空间字段，普通的非空间表是没办法将记录集传递给后续空间处理的工具的。

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_MakeQueryLayerModel.png-kikitaMaps)

Make Feature Layer 中的 SQL语句：

```sql
select  c.SHAPE,
        c.ADDRESS,
        count(c.ADDRESS) as CallNum, 
        min(s.SCORE) as MinScore, 
        c.POINT_X, 
        c.POINT_Y
from SDE.kikita_Calls c 

left join SDE.kikita_ScoreTable s 
on c.ADDRESS=s.ADDRESS

where c.AV_SIDE in ('R','L')

group by c.SHAPE,c.ADDRESS,c.POINT_X, c.POINT_Y
order by CallNum DESC
```

<br>


附一张结果图：


![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_QureyLayerReault.png)