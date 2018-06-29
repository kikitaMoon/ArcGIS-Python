# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import arcpy
arcpy.env.workspace = r'D:\ArcGISProProject\Web3DTest\Web3DScene\Web3DScene.gdb'
gtf_name = "testforarcpy0227"
arcpy.management.CreateCustomGeoTransformation(gtf_name,
                                               "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                               "GEOGCS['GCS_Xian_1980',DATUM['D_Xian_1980',SPHEROID['Xian_1980',6378140.0,298.257]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                               "Null")
arcpy.management.Project(in_dataset = r"D:\LearnAboutArcGIS\ArcGIS_Desktop\E_投影与坐标系统\CGCS2000软件测评\UserData_ForTest\New File Geodatabase.gdb\XIAN1980",
                         out_dataset = "XIAN1980_Project_022702",
                         out_coor_system = "GEOGCS['GCS_China_Geodetic_Coordinate_System_2000',DATUM['D_China_2000',SPHEROID['CGCS2000',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                         transform_method = gtf_name)