# -*- coding: utf-8 -*-
__author__ = 'mu_xiaoyan'
# !/usr/bin/python

import os
import zipfile
import arcpy

## Arcpy -- Create Partial VTPK in AOI
def create_partial_vtpk(workspace, indexPolygon, AOI, map, lodLevel, vtpkName):
    arcpy.env.workspace = workspace
    arcpy.AddMessage("current workspace: " + arcpy.env.workspace)
    AOI_lyr = arcpy.MakeFeatureLayer_management(AOI, "AOI_lyr")
    IndexPolygon_lyr = arcpy.MakeFeatureLayer_management(indexPolygon, "IndexPolygon_lyr")
    arcpy.SelectLayerByLocation_management(IndexPolygon_lyr, 'intersect', AOI_lyr)
    arcpy.AddMessage("Start LOD Level" + lodLevel)
    arcpy.SelectLayerByAttribute_management(IndexPolygon_lyr, 'SUBSET_SELECTION', str(' "LOD" > ' + lodLevel))
    arcpy.CopyFeatures_management(IndexPolygon_lyr, 'NewIndex.shp')
    arcpy.AddMessage('generate new Index layer')
    IndexPolygon_lyr.visible = False
    AOI_lyr.visible = False
    try:
        arcpy.management.CreateVectorTilePackage(map, vtpkName, "ONLINE", None,
                                            "INDEXED", 295828763.795777, 564.248588, 'NewIndex.shp', None, None)
    except Exception as err:
        arcpy.AddError(err)
        print(err)
    arcpy.Delete_management('NewIndex.shp')
    return True

#  input map from current open project
map = arcpy.GetParameterAsText(0)

# input index polygon
indexPolygon = arcpy.GetParameterAsText(1)

# input area of interest polygon
AOI = arcpy.GetParameterAsText(2)

# input workspace for new part vtpk
output_vtpk_path = arcpy.GetParameterAsText(3)

# input the start lod for update
lodLevel = arcpy.GetParameterAsText(4)

workspace = os.path.dirname(output_vtpk_path)
vtpkName = os.path.split(output_vtpk_path)[1]

create_partial_vtpk(workspace, indexPolygon, AOI, map, lodLevel, vtpkName)




