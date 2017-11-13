# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import os

arcpy.env.workspace = r"\\192.168.220.162\TestData\My_data3DUIM_1.gdb"
arcpy.env.overwriteOutput = True

OutFolder = r"\\192.168.220.162\TestData\MyProject1"
sddraftFile = os.path.join(OutFolder, "CopyFeature.sddraft")
sdFile = os.path.join(OutFolder, "CopyFeature.sd")

result = arcpy.CopyFeatures_management("NewBuilding2", "NewBuilding_Copy4")
print('Copy Feature Done !')
print(result)

rlt = os.path.join(OutFolder, "CopyFeature.rlt")
result.saveToFile(rlt)

arcpy.PackageResult_management(rlt, os.path.join(OutFolder, "CopyFeature.gpkx"))



