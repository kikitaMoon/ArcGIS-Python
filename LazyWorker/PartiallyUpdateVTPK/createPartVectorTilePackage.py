# -*- coding: utf-8 -*-
__author__ = 'mu_xiaoyan'
# !/usr/bin/python


import arcpy
import os


## Arcpy -- Create Partial VTPK in AOI
def create_partial_vtpk(workspace, indexPolygon, AOI, map, lodLevel, vtpkName, service_type, tiling_scheme):
    arcpy.env.workspace = workspace
    arcpy.AddMessage("Current workspace: {0}".format(arcpy.env.workspace))
    AOI_lyr = arcpy.MakeFeatureLayer_management(AOI, "AOI_lyr")
    IndexPolygon_lyr = arcpy.MakeFeatureLayer_management(indexPolygon, "IndexPolygon_lyr")
    arcpy.SelectLayerByLocation_management(IndexPolygon_lyr, 'intersect', AOI_lyr)
    arcpy.AddMessage("Start LOD level: {0}".format(lodLevel))
    arcpy.SelectLayerByAttribute_management(IndexPolygon_lyr, 'SUBSET_SELECTION', str(' "LOD" > ' + lodLevel))
    arcpy.CopyFeatures_management(IndexPolygon_lyr, 'NewIndex.shp')
    arcpy.AddMessage('New index layer has been generated.')
    IndexPolygon_lyr.visible = False
    AOI_lyr.visible = False
    try:
        arcpy.management.CreateVectorTilePackage(map, vtpkName, service_type, tiling_scheme,
                                             "INDEXED", 295828763.795777, 564.248588, 'NewIndex.shp', None, None)
    except Exception as err:
        arcpy.AddError(err)
        print(err)
    arcpy.Delete_management('NewIndex.shp')
    return True


# Input map in current project
mymap = arcpy.GetParameterAsText(0)
arcpy.AddMessage("Input map : {0}.".format(mymap))

# Specify name and workspace for new part vtpk
output_vtpk_path = arcpy.GetParameterAsText(1)
arcpy.AddMessage("Specify updating vector tile package workspace : {0}.".format(output_vtpk_path))
workspace = os.path.dirname(output_vtpk_path)
vtpkName = os.path.split(output_vtpk_path)[1]

# Input origin index polygon
indexPolygon = arcpy.GetParameterAsText(2)
arcpy.AddMessage("Input origin index polygon : {0}.".format(indexPolygon))

# Input AOI
AOI = arcpy.GetParameterAsText(3)
arcpy.AddMessage("Input AOI : {0}.".format(AOI))

# Specify level number of LOD
lodLevel = arcpy.GetParameterAsText(4)
arcpy.AddMessage("Specify level number of LOD : {0}.".format(lodLevel))



# Specify service type
service_type = arcpy.GetParameterAsText(5)
# Specify tiling skema
tiling_scheme = arcpy.GetParameterAsText(6)


# Excute create_partial_vtpk function
create_partial_vtpk(workspace, indexPolygon, AOI, mymap, lodLevel, vtpkName, service_type, tiling_scheme)


