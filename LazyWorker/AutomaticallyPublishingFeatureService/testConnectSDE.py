# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import os

####  My Test
outFolderPath = r'D:\LearnAboutPython\MyPythonProject\PublicFeatureService20170220'
outName = 'oracleConnection.sde'
sdePath = outFolderPath + '\\' + outName
sdeIp = '192.168.220.131'
sdePort = ''
sdeServiceName = ''
dirInstance = sdeIp + ":" + sdePort + "/" + sdeServiceName
sdeUserName = 'lf'
sdePw = 'lf'

sdePath = outFolderPath + '\\' + outName
if os.path.exists(sdePath):
    os.remove(sdePath)

print(sdePath)
arcpy.CreateDatabaseConnection_management(out_folder_path=outFolderPath,
                                          out_name=outName,
                                          database_platform="ORACLE",
                                          instance="192.168.220.131/test",
                                          account_authentication="DATABASE_AUTH",
                                          username=sdeUserName,
                                          password=sdePw,
                                          save_user_pass="SAVE_USERNAME",
                                          database="#",
                                          schema="#",
                                          version_type='POINT_IN_TIME',
                                          version="#",
                                          date="#")

agsPath = outFolderPath + '\AGSConnection116.ags'
arcpy.AddDataStoreItem(connection_file=agsPath,
                       datastore_type="DATABASE",
                       connection_name="myDBConnectOracleSpatial",
                       server_path=sdePath)

for i in arcpy.ListDataStoreItems(agsPath, "DATABASE"):
    validity = arcpy.ValidateDataStoreItem(agsPath, "DATABASE", i[0])
    print("The data item '{}' is {}".format(i[0], validity))



