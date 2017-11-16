   # -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import os

####  My Test

outFolderPath = r'D:\LearnAboutPython\MyPythonProject\PublicFeatureService20170220'
outName = 'AGSConnection116.ags'
gisIp = '192.168.220.116'
gisPort = 6080
serverUrl = 'http://{0}:{1}/arcgis/admin'.format(gisIp, gisPort)

username = 'arcgis'
password = 'Super123'

path = outFolderPath+'\\'+outName
if os.path.exists(path):
    os.remove(path)

print(serverUrl)
arcpy.mapping.CreateGISServerConnectionFile(connection_type="ADMINISTER_GIS_SERVICES",
                                            out_folder_path=outFolderPath,
                                            out_name=outName,
                                            server_url=serverUrl,
                                            server_type="ARCGIS_SERVER",
                                            use_arcgis_desktop_staging_folder=False,
                                            staging_folder_path=outFolderPath,
                                            username=username,
                                            password=password,
                                            save_username_password=True)
