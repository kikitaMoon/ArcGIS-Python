# -*- coding: utf-8 -*-
__author__ = 'Mu Xiaoyan'

import arcpy
import math
import os

lineFC = arcpy.GetParameterAsText(0)
Step = arcpy.GetParameterAsText(1)
BufferSize = arcpy.GetParameterAsText(2)
SplitedBuffer = arcpy.GetParameterAsText(3)

arcpy.env.overwriteOutput = True
print(arcpy.env.scratchGDB)

# lineFC = 'SingleLine'
# Step = 1000
# BufferSize = 600


# Judge Coordinate System First
desc = arcpy.Describe(lineFC)
sr = desc.spatialReference
if sr.type == "Projected":
    # Create Perpendicular Dash line
    LineGeometryList = []
    with arcpy.da.SearchCursor(lineFC, ['SHAPE@']) as cursor:
        for row in cursor:
            Position = 0
            while  Position < row[0].length:
                # point position
                pointGeometry = row[0].positionAlongLine(Position)
                # point position + 1
                PositionNext = Position + 0.1
                pointGeometryNext = row[0].positionAlongLine(PositionNext)
                # Calculate Angle
                if pointGeometryNext.centroid.X-pointGeometry.centroid.X != 0:
                    Angle = math.atan((pointGeometryNext.centroid.Y-pointGeometry.centroid.Y)/(pointGeometryNext.centroid.X-pointGeometry.centroid.X))
                    AngleDegree = Angle*180.0/math.pi
                else:
                    Angle = 0
                print(AngleDegree)
                # Construct Perpendicular line
                PerpendicularPoint1 = pointGeometry.pointFromAngleAndDistance(180-AngleDegree, float(BufferSize)+1.0)
                PerpendicularPoint2 = pointGeometry.pointFromAngleAndDistance(180-AngleDegree, -float(BufferSize)-1.0)
                LineGeometry = arcpy.Polyline(arcpy.Array([PerpendicularPoint1.centroid, pointGeometry.centroid, PerpendicularPoint2.centroid]))
                LineGeometryList.append(LineGeometry)
                Position = float(Position) + float(Step)

    arcpy.CopyFeatures_management(LineGeometryList, os.path.join(arcpy.env.scratchGDB, "PerpenResult"))

    # Line Buffer
    arcpy.Buffer_analysis(in_features = lineFC, out_feature_class = os.path.join(arcpy.env.scratchGDB,"buffer"),buffer_distance_or_field = BufferSize,
                          line_side = "FULL", line_end_type = "ROUND", dissolve_option = "ALL", dissolve_field = "", method="PLANAR")

    # Split Buffer
    arcpy.FeatureToPolygon_management(in_features=[os.path.join(arcpy.env.scratchGDB, "buffer"), os.path.join(arcpy.env.scratchGDB, "PerpenResult")],
                                      out_feature_class=os.path.join(arcpy.env.scratchGDB,"SplitedBufferAll"), cluster_tolerance="",
                                      attributes="ATTRIBUTES", label_features="")

    # Select Buffer and Export
    arcpy.MakeFeatureLayer_management(os.path.join(arcpy.env.scratchGDB,"SplitedBufferAll"), "SplitedBufferAllLayer")
    arcpy.SelectLayerByLocation_management(in_layer="SplitedBufferAllLayer", overlap_type="INTERSECT",select_features=lineFC,
                                           search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")
    arcpy.CopyFeatures_management("SplitedBufferAllLayer", SplitedBuffer)

else:
    arcpy.AddError("Input line feature class <{0}> does not have a projected coordinate system.".format(lineFC))