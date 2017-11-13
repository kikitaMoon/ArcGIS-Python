# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import os

arcpy.env.workspace = r"\\192.168.220.162\TestData\My_data3DUIM_1.gdb"
OutFolder = r"\\192.168.220.162\TestData\MyProject1"
sddraftFile = os.path.join(OutFolder, "CopyFeature.sddraft")
sdFile = os.path.join(OutFolder, "CopyFeature.sd")

result = arcpy.CopyFeatures_management("NewBuilding2", "NewBuilding_Copy3")
print('Copy Feature Done !')

arcpy.CreateGPSDDraft(result, sddraftFile, "myGPservice")
print("GP Draft Done!")

arcpy.StageService_server(sddraftFile, sdFile)
print("GP SD Done!")

arcpy.UploadServiceDefinition_server(os.path.join(OutFolder, sdFile), 'My Hosted Services')
print('Done!')