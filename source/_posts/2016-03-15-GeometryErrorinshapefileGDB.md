title: shapefile与GDB中不能允许存在的几何错误
categories:
  - 木工开物
date: 2013-12-05 11:36:17
tags: [Geodata]
---
每种软件都有自己的数据规范，ArcGIS也不例外，当数据不满足ArcGIS的规范时，就会遇到各种无响应和崩溃。

有关数据几何错误总是问题相对较多的部分。其中，shapefile作为一种开放的格式，除了ArcGIS程序可以读写，也可以按照数据规范在非ArcGIS环境中生产。后者生产的数据通常包含这样那样的问题，这些问题都是几何错误的范畴。

帮助原文说的精辟：

> The shapefile is an open format to which many software packages write. Unfortunately, some of these software packages—sometimes due to bugs, sometimes due to lack of knowledge—do not follow the documented specification of the shapefile format.

简单罗列下ArcGIS中不能允许的几何错误类型：

**短线段/Short segment**
Some segments are shorter than allowed by the system units of the spatial reference associated with the geometry.
 

**空几何/Null geometry**
The feature has no geometry or nothing in the SHAPE field.

**不正确的环顺序/Incorrect ring ordering**
The polygon is topologically simple, but its rings may not be oriented correctly (outer rings—clockwise, inner rings—counterclockwise).

不正确的线段方向/Incorrect segment orientation
Individual segments are not consistently oriented. The "to" point of seg i should be incident on the "from" point of seg i+1.

**自相交/Self intersections**
A polygon must not intersect itself.

**非封闭环/Unclosed rings**
The last segment in a ring must have its "to" point incident on the "from" point of the first segment.

**空部分/Empty parts**
The geometry has multiple parts and one of them is empty (has no geometry).

**重复折点/Duplicate vertex**
The geometry has two or more vertices with identical coordinates.

**属性不匹配/Mismatched attributes**
The Z or M coordinate of a line segment's endpoint does not match the Z or M coordinate of the coincident endpoint on the next segment.

**不连续部分/Discontinuous parts**
One of the geometry's part is made up of disconnected or discontinuous parts.

**空Z值/Empty Z values**
The geometry has one or more vertex with empty Z value (NaN, for example).



以上的错误，可以用使用工具 Check Geometry 进行检查，工具会生成有关几何错误的报表。使用 Repaired Geometry 工具进行修复。