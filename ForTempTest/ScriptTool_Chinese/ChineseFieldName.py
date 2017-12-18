# -*- coding: cp936 -*-

import arcpy
input = arcpy.GetParameterAsText(0)
fieldName = "中文字段"
arcpy.AddField_management(input, fieldName, "TEXT")
