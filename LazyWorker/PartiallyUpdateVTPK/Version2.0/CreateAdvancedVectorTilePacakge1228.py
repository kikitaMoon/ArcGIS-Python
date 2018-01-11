# -*- coding: utf-8 -*-
__author__ = 'mu_xiaoyan'
# !/usr/bin/python
# Version 2.0

import arcpy
import os
import xml.dom.minidom as DOM

# Input map in current project
in_map = arcpy.GetParameterAsText(0)
arcpy.AddMessage("Input map : {0}.".format(in_map))

# Specify name and workspace for the output vtpk
outVtpk = arcpy.GetParameterAsText(1)
arcpy.AddMessage("Output vtpk  : {0}.".format(outVtpk))


#  Specify service type
isOnline = arcpy.GetParameter(2)

# Specify maximum vertex count
vertex_count=arcpy.GetParameterAsText(3)
arcpy.AddMessage("Maximum vertex count : {0}.".format(vertex_count))

vtpkDir = os.path.dirname(outVtpk)
arcpy.AddMessage(vtpkDir)
tileScheme = vtpkDir+"\customizedScheme.xml"
indexPolygon = vtpkDir+"\masterIndex.shp"


# Create Vector Tile Package Scheme for Customize Coordinate System
def GenerateVtpkTilingScheme(in_map,tileScheme):
    scales = "295829355.454565;147914677.727283;73957338.8636413;36978669.4318207;18489334.7159103;9244667.35795516;4622333.67897758;2311166.83948879;1155583.4197444;577791.709872198;288895.854936099;144447.927468049;72223.9637340247;36111.9818670124;18055.9909335062;9027.99546675309;4513.99773337654;2256.99886668827;1128.49943334414;564.249716672068"
    arcpy.server.GenerateMapServerCacheTilingScheme(in_map=in_map,
                                                    tile_origin="-180.0 180.0",
                                                    output_tiling_scheme=tileScheme,
                                                    num_of_scales=20,
                                                    scales=scales,
                                                    dots_per_inch=96,
                                                    tile_size="512 x 512")
    arcpy.AddMessage("tileScheme Done!")
    # return tileScheme

# Modify Scheme File to Avoid the tile_Origin Issue
def modifyTilingSchmeFile(tileScheme):
    doc = DOM.parse(tileScheme)
    tileOriginX = doc.getElementsByTagName('X')
    tileOriginY = doc.getElementsByTagName('Y')
    tileOriginX[0].firstChild.data = '-180'
    tileOriginY[0].firstChild.data = '180'
    f = open(tileScheme, 'w+')
    doc.writexml(f)
    f.close()

# Create Vector Tile Index and then Create Vector Tile Package
def createVtpkIndexAndPackage(in_map,service_type,tileScheme,vertex_count,outVtpk):
    arcpy.management.CreateVectorTileIndex(in_map=in_map,
                                           out_featureclass=indexPolygon,
                                           service_type=service_type,
                                           tiling_scheme=tileScheme,
                                           vertex_count=vertex_count)
    arcpy.AddMessage("Index Done!")
    arcpy.management.CreateVectorTilePackage(in_map=in_map,
                                             output_file=outVtpk,
                                             service_type=service_type,
                                             tiling_scheme=tileScheme,
                                             tile_structure="INDEXED",
                                             min_cached_scale="",
                                             max_cached_scale="",
                                             index_polygons=indexPolygon,
                                             summary=None,
                                             tags=None)
    arcpy.AddMessage("vtpk done!")
    return outVtpk


arcpy.AddMessage("isOnline:"+str(isOnline))
if isOnline:
    service_type = "ONLINE"
    tileScheme = ""
    arcpy.AddMessage("service type:"+service_type)
    createVtpkIndexAndPackage(in_map,service_type,tileScheme,vertex_count,outVtpk)
else:
    service_type = "EXISTING"
    arcpy.AddMessage("service type:"+service_type)
    GenerateVtpkTilingScheme(in_map,tileScheme)
    arcpy.AddMessage(tileScheme)
    modifyTilingSchmeFile(tileScheme)
    createVtpkIndexAndPackage(in_map,service_type,tileScheme,vertex_count,outVtpk)
