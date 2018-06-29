# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Users\kikita\Desktop\TestExporting.mxd")
arcpy.mapping.ExportToJPEG(mxd, r"C:\Users\kikita\Desktop\Project3.jpg")
del mxd
