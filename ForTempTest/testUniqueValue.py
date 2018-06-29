# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Users\kikita\Desktop\Untitled.mxd")
lyr = arcpy.mapping.ListLayers(mxd, "Cities")[0]
if lyr.symbologyType == "UNIQUE_VALUES":
  lyr.symbology.addAllValues()
# arcpy.RefreshActiveView()
# arcpy.RefreshTOC()
# Add save method
mxd.save()
del mxd

