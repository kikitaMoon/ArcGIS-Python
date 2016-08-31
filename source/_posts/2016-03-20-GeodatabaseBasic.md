title: Geodatabase之基础

categories:
  - 木工开物

date: 2012-02-07 14:25:00
tags: [Geodata]

---


Geodatabase是用来表达和管理地理信息的复杂数据模型，是ArcGIS的主要存储数据方式，主要存储了 featureclasses、 rasterdatasets、attributes、具有行为的高级GIS数据对象、 管理空间完整性的规则、要素栅格属性关系工具。

**一、Geodatabase 的种类：**

就其种类呢，无非是三种：File Geodatabase，PersonalGeodatabase，ArcSDEGeodatabase。 

1、 FileGeodatabase：以文件夹形式存储。每个Dataset作为一个文件存储，最大可达1T。对于PGDB更推荐FGDB。单用户，同一个Dataset 、独立的featureclass或者table，并发只能有一人写操作，可以多人读操作。支持跨平台。

2、PersonalGeodatabase：所有的Dataset都存储在MicrosoftAccess数据文件中,最大大小不超过2 GB。单用户，一个人写多人读。仅支持Windows。

3、ArcSDEGeodatabase：储存在关系数据库中，可使用 Oracle,MicrosoftSQL Server, IBM DB2, IBM Informix,PostgreSQL。这些多用户的数据库要求使用ArcSDE，不限制大小和用户的数量。平台支持：Windows, UNIX,Linux。

**二、Geodatabase中的Dateset**

Geodatabase 中包含基本的dataset，包括：feature classes、 rasterdatasets、attributes。还包含高级地理数据类型：coordinate systems, coordinateresolution, feature classes,topologies, networks, raster catalogs,relationships, domains。

**1、Table**

用于存储属性等。字段类型包含：Numbers（长整型、短整型、单精度、双精度）、Text、Date（日期时间型）、BLOBs（二进制大对象，例如Symbol、CAD几何要素）、GlobalID（全局标识符）、XML。

**2、Feature Class**

Feature Class以一张单独的表存储，每个要素是一条记录。种类： Points、Lines、Polygons、Annotation、 Dimensions（尺寸）、MultiPoints（由多个点组成的要素，如雷达激光点）、MultiPatches（多面体）。

其中要素坐标可包含Z值，表示垂直测量结果；线状要素可以包含M值，表示线性测量结果。路径是指具有唯一标识符和通用测量系统的任意线状要素（如城市街道、公路、河流或管线）。

与FeatureClass相关的：FeatureDataset，subtype，AttributeDomain，RelationshipClasses，Topology，Network Dataset，Geometric network，TerrainDataset，Linear referencing，Cartographicrepresentation，versioning。

**3、Raster**

栅格的地理属性通常包括：坐标系，参考坐标或 X,Y 位置（通常在栅格左上角或左下角），单元大小，行计数和列计数。
地理数据库可以针对多种用途管理栅格：作为单个数据集、数据集的逻辑集合和表中的图片属性.

