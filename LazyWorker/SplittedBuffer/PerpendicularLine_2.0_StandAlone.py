# -*- coding: utf-8 -*-
__author__ = 'Mu Xiaoyan'

## What's New in 2.0 ?
## 1. Support double line by using arcpy Geometry method and attribute.
## 2. Additionally, optionally output perpendicular line.

# linefc = arcpy.GetParameterAsText(0)
# step = arcpy.GetParameterAsText(1)
# buffersize = arcpy.GetParameterAsText(2)
# splitedbuffer = arcpy.GetParameterAsText(3)
# perplinefc = arcpy.GetParameterAsText(4)

import arcpy
import os
arcpy.env.workspace = r'D:\kikitaDIY\2016技术创新\SplittedBuffer\toZAZAmama.gdb'
arcpy.env.overwriteOutput = True

linefc = 'DemoData'
step = 100
buffersize = 50
splitedbuffer = linefc + '_splittedbuffer'
perplinefc = linefc + '_perpline'


# Get Perpendicular Line at Specific Position
def perpendicularline(lineGeometry, spatialReference, Position, bufferSize):
    import math
    # a Specific Position
    pointGeometry = lineGeometry.positionAlongLine(Position)
    # an tiny offset Specific Position
    PositionNext = Position + 0.1
    pointGeometryNext = lineGeometry.positionAlongLine(PositionNext)
    # Calculate Angle
    if pointGeometryNext.centroid.X-pointGeometry.centroid.X != 0:
        Angle = math.atan((pointGeometryNext.centroid.Y-pointGeometry.centroid.Y) /
                          (pointGeometryNext.centroid.X-pointGeometry.centroid.X))
        AngleDegree = Angle*180.0/math.pi
    else:
        AngleDegree = 0
    # Construct Perpendicular Line
    PerpendicularPoint1 = pointGeometry.pointFromAngleAndDistance(180-AngleDegree, float(bufferSize)+1.0)
    PerpendicularPoint2 = pointGeometry.pointFromAngleAndDistance(180-AngleDegree, -float(bufferSize)-1.0)
    perpGeometry = arcpy.Polyline(arcpy.Array([PerpendicularPoint1.centroid,
                                           pointGeometry.centroid, PerpendicularPoint2.centroid]), spatialReference)
    return(perpGeometry)


# Create Feature Classes for the Results
def createSplittedbufferfc(splitedBuffer, spatialReference):
    if arcpy.Exists(splitedBuffer):
        arcpy.Delete_management(splitedBuffer)
    arcpy.CreateFeatureclass_management(out_path=arcpy.env.workspace, out_name=splitedBuffer,
                                        geometry_type='POLYGON', spatial_reference=spatialReference)
    if perplinefc:
        if arcpy.Exists(perplinefc):
            arcpy.Delete_management(perplinefc)
        arcpy.CreateFeatureclass_management(out_path=arcpy.env.workspace, out_name=perplinefc,
                                            geometry_type='POLYLINE', spatial_reference=spatialReference)

desc = arcpy.Describe(linefc)
sr = desc.spatialReference
arcpy.AddMessage(u'当前坐标系统是 {0}'.format(sr.name))

# Judge Coordinate System Type, only Projected Coordinate System works.
if sr.type == "Projected":
    arcpy.AddMessage(' Starting ...')
    createSplittedbufferfc(splitedbuffer, sr)
    with arcpy.da.SearchCursor(linefc, ['SHAPE@', 'OBJECTID']) as linecursor:
        for linerow in linecursor:
            Position = 0
            perplinelist = []
            bufferPolygon = linerow[0].buffer(buffersize)
            arcpy.CopyFeatures_management(bufferPolygon, 'in_memory\\bufferpolygon')
            print(linerow[1])
            while Position < linerow[0].length:
                perpline = perpendicularline(linerow[0], sr, Position, buffersize)
                perplinelist.append(perpline)
                Position = float(Position) + float(step)
            arcpy.CopyFeatures_management(perplinelist, 'in_memory\\perplinelist')
            if perplinefc:
                arcpy.Append_management('in_memory\\perplinelist', perplinefc, 'NO_TEST')
            arcpy.FeatureToPolygon_management(['in_memory\\perplinelist', 'in_memory\\bufferpolygon'], 'in_memory\\splittedbufferitem')
            arcpy.Append_management('in_memory\\splittedbufferitem', splitedbuffer, 'NO_TEST')
            arcpy.Delete_management("in_memory")
else:
    arcpy.AddError(u"输入要素类 <{0}> 需要具有投影坐标系定义.".format(linefc))