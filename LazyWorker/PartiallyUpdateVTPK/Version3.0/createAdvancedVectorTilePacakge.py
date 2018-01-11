# -*- coding: utf-8 -*-
__author__ = 'mu_xiaoyan'
# !/usr/bin/python
# Version 3.0
# What's New in 3.0 ?'
# Package the scheme file and Index polygon to the vtpk automatically.

import arcpy
import os
import xml.dom.minidom as DOM
import zipfile
import shutil
import sys

# Create Vector Tile Package Scheme for Customize Geographic Coordinate System
# Using 20 fixed Level for the first Version.  It can be better in future version, if necessary.
def GenerateVtpkTilingScheme(in_map,tileScheme):
    try:
        scales = "295829355.454565;147914677.727283;73957338.8636413;36978669.4318207;18489334.7159103;9244667.35795516;4622333.67897758;2311166.83948879;1155583.4197444;577791.709872198;288895.854936099;144447.927468049;72223.9637340247;36111.9818670124;18055.9909335062;9027.99546675309;4513.99773337654;2256.99886668827;1128.49943334414;564.249716672068"
        arcpy.server.GenerateMapServerCacheTilingScheme(in_map=in_map,
                                                        tile_origin="-180.0 180.0",
                                                        output_tiling_scheme=tileScheme,
                                                        num_of_scales=20,
                                                        scales=scales,
                                                        dots_per_inch=96,
                                                        tile_size="512 x 512")
        arcpy.AddMessage("tile scheme - ready.")
        return tileScheme
    except:
        arcpy.AddMessage("input map for tiling scheme invalid.")

# Modify Scheme File to Avoid the tile_Origin Specification Bug of the Pro Tool
def modifyTilingSchemeFile(tileScheme):
    try:
        doc = DOM.parse(tileScheme)
        tileOriginX = doc.getElementsByTagName('X')
        tileOriginY = doc.getElementsByTagName('Y')
        tileOriginX[0].firstChild.data = '-180'
        tileOriginY[0].firstChild.data = '180'
        f = open(tileScheme, 'w+')
        doc.writexml(f)
        f.close()
        return True
    except:
        arcpy.AddMessage("tile scheme XML file does not exist.")

# Create Vector Tile Index and then Create Vector Tile Package
def createVtpkIndexAndPackage(in_map,service_type,tileScheme,vertex_count,indexPolygon,outVtpk):
    try:
        arcpy.management.CreateVectorTileIndex(in_map=in_map,
                                               out_featureclass=indexPolygon,
                                               service_type=service_type,
                                               tiling_scheme=tileScheme,
                                               vertex_count=vertex_count)
        arcpy.AddMessage("tile index - ready.")
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
        arcpy.AddMessage("Pro standard tile package - ready!")
        return outVtpk
    except:
        arcpy.AddMessage("input map for packaging invalid. Check the coordinate system of the input map.")

# Append the tiling scheme and index polygon to the standard vtpk
def add_to_zip(original_zip, newfolder):
    try:
        # print("zip file: " + original_zip)
        folder = os.path.dirname(original_zip)
        prelen = len(folder)
        fp = zipfile.ZipFile(original_zip, mode='a')
        for parent, dirnames, filenames in os.walk(newfolder):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                # print("pathfile",pathfile)
                arcname = pathfile[prelen:].strip(os.path.sep)
                # print("arcname",arcname)
                fp.write(pathfile, arcname)
        fp.close()
        return True
    except:
        print("path or folderName not exist.")

# Clear the scratch data
def delete_zip_folder(delete_path):
    shutil.rmtree(delete_path)

# the main method of this script
def execute(in_map,outVtpk,isOnline,vertex_count):
    vtpkDir = os.path.join(os.path.dirname(outVtpk), "AdvVtpkAuxFiles")
    # arcpy.AddMessage("TempFolder"+vtpkDir)
    if not os.path.exists(vtpkDir):
        os.makedirs(vtpkDir)
    tileScheme = vtpkDir + "\customizedScheme.xml"
    indexPolygon = vtpkDir + "\originMasterIndex.shp"
    if isOnline:
        service_type = "ONLINE"
        tileScheme = ""
        arcpy.AddMessage("service type:"+service_type)
    else:
        service_type = "EXISTING"
        arcpy.AddMessage("service type:"+service_type)
        GenerateVtpkTilingScheme(in_map,tileScheme)
        arcpy.AddMessage(tileScheme)
        modifyTilingSchemeFile(tileScheme)

    originalVTPK = createVtpkIndexAndPackage(in_map,service_type,tileScheme,vertex_count,indexPolygon,outVtpk)
    if add_to_zip(originalVTPK, vtpkDir):
        delete_zip_folder(vtpkDir)

    arcpy.AddMessage("advanced vector tile package has been generated.")


def main(argv=None):
    # Input map in current project
    in_map = arcpy.GetParameterAsText(0)
    arcpy.AddMessage("Input map : {0}.".format(in_map))

    # Specify name and workspace for the output vtpk
    outVtpk = arcpy.GetParameterAsText(1)
    arcpy.AddMessage("Output advanced vtpk  : {0}.".format(outVtpk))

    #  Specify service type
    isOnline = arcpy.GetParameter(2)
    arcpy.AddMessage("isOnline:"+str(isOnline))

    # Specify maximum vertex count
    vertex_count = arcpy.GetParameterAsText(3)
    arcpy.AddMessage("Maximum vertex count : {0}.".format(vertex_count))

    execute(in_map,outVtpk,isOnline,vertex_count)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))