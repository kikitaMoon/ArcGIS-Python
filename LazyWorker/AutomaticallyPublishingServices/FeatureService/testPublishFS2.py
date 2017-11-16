# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import xml.dom.minidom as DOM

# Add Layer
arcpy.env.workspace = r'D:\LearnAboutPython\MyPythonProject\PublicFeatureService20170220'
arcpy.env.overwriteOutput = True

mxdFilePath = "onelayer.mxd"
sdeFile = 'oracleConnection.sde'
mxd = arcpy.mapping.MapDocument(mxdFilePath)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "", df)[0]
print(lyr.name)
print(lyr.dataSource)

## Replace Data Source -- Feature Class
lyr.replaceDataSource(workspace_path=sdeFile,
                      workspace_type="OLEDB_WORKSPACE",
                      dataset_name="LF.CITYWORLD",
                      validate=False)

mxd.saveACopy("onelayerNew5.mxd")

## Make Query Layer -- Feature Class

# arcpy.MakeQueryLayer_management(input_database=sdeFile,
#                                 out_layer_name="QueryCities",
#                                 query="select * from LF.CITYWORLD")
# lyr = arcpy.mapping.Layer("QueryCities")
# arcpy.ApplySymbologyFromLayer_management(lyr, "SDE.Symbole.lyr")
# lyr.save()
# arcpy.mapping.AddLayer(df, lyr, "AUTO_ARRANGE")
# mxd.saveACopy("onelayerNew4.mxd")
