title: CGA：自动判断模型间关系的3D建模方法
categories:
  - 木工开物
date: 2016-04-01 10:29:27
tags: [CityEngine,CGA,3D]
---

# 背景

最近遇到一个有趣的问题，**如何在CityEgnine中判断有接触或相交关系的模型，从而自动进行建模？**

这个问题有点抽象，我们来看个实例，了解下问题的背景:

以往绝大多数情况下，我们拿到的2D建筑物底面（FootPrint）都是一个建筑对应一个面，也就是这样的：

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_SimpleFootPrint.png-kikitaMaps)


实际生活中的的建筑物可能是更复杂的，例如商场、大型会议中心、复杂居民楼等参差不齐的多栋联合建筑，我们可以采集多个底面来表示建筑物，例如这样：

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_MultiFootprint.png-kikitaMaps)


使用多个底面表示一栋复杂建筑物的做法可以很大程度上简化建模的工作，因此无可厚非。 但是问题来了，因为是彼此独立的Footprint，建模时若不加判断，就会出现如下图所示的情况，好像“空中地下室”。这样的房子既不美观也不实际。

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ModelOverlap.png-kikitaMaps)

<br>

# 解决方法

CityEngine的真正魅力在于“动态”建模，这是CE的创作者一直想要传播的理念。 CityEgnine提供很多内置函数解决这些问题，其中有一组为：**Occlusion Functions**，包含：`inside`，`overlaps`，`touches` 三个函数。 我们可以利用 `touches()` 来实现判断。

先写段简单的来了解下函数用法：

```applescript
Init --> 
     extrude(40) Mass
Mass -->
     comp(f){top:NIL| side:Side} 
Side --> 
     case touches(): color(1,0,0) ShareSide
     else: Walls
```


![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ShareSide.png-kikitaMaps)



针对前面“空中地下室”的问题，可以在楼层切割到窗户和墙体的时候做个判断，楼层不touch其他楼层时，再进行分割。

可以实现这个样子：

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ModelTouchSolve.png-kikitaMaps)

全部 CGA 代码共享给大家：


```applescript
/**
 * File:    TestTouches.cga
 * Created: 1 Apr 2016 13:00:24 GMT
 * Author:  kikita
 */

version "2015.2"

# Define Attributes
attr AVG_HEIGHT = 0
attr WindowsWidth = 8
attr WallWidth = 2.5

# Building Schmetic
Init --> 
     extrude(AVG_HEIGHT) Mass
Mass -->
     comp(f){top:Top|side:Walls}
Walls -->
     split(y) { 15 : GroundFloor | {~10 : UpperFloors } * }

# Ground Floor
GroundFloor --> 
   setupProjection(0, scope.xy, '1, '1)
   projectUV(0) 
   texture("GroundFloor.jpg") 

# All Upper Floors
UpperFloors --> 

# Use touches() function
	case touches():
         setupProjection(0, scope.xy, 10, 10)
         projectUV(0) 
         texture("Wall/wall_grey.jpg")
	else:
	     split(x){ ~WallWidth : AllWalls |
                 { ~WindowsWidth : WindowTiles |
                   ~WallWidth : AllWalls } * }                 
	     WindowTiles -->
		    split(y){ ~WallWidth/2: AllWalls |
			          ~WindowsWidth : Windows|
			          ~WallWidth/2 :AllWalls }

# Wall Texture      
AllWalls -->    
      setupProjection(0, scope.xy, 10, 10)
      projectUV(0) 
      texture("Wall/wall_grey.jpg")

# Windows  
Windows --> 
      color("DAFAF3")
      i("Windows/sash_window.obj") 
      s('1,'1,'2)          

# Roofs
Top --> 
      offset(-0.5)
      comp(f){ border : RoofEdge | inside : RoofFlat }     
RoofFlat -->
      setupProjection(0, scope.xy, '1, '1)
      projectUV(0) 
      texture("flatroof6.bw.jpg")     
RoofEdge --> 
      extrude(1) 

```


明天就放假了

节日愉快

我说的是愚人节

哈