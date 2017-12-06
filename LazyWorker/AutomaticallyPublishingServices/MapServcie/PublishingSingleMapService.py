# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy, os

# Modify as your workspace
##########################
workSpace = r"D:\GitHubRepositories\ArcGIS-Python\LazyWorker\AutomaticallyPublishingServices\MapServcie"
mxdFile = 'forTest.mxd'
gisServer = 'kikita.mycloud.com'
gisPort = 6443
username = 'portaladmin'
password = 'Super123'
serverUrl = 'https://{0}:{1}/arcgis/admin'.format(gisServer, gisPort)
print(serverUrl)
###########################


# Create ArcGIS Server Connection File
outAGSName = 'ArcGISServerConnection.ags'
path = workSpace + '\\' + outAGSName
if os.path.exists(path):
    os.remove(path)
    print("Existing ArcGIS Server connection file deleted ... ")
arcpy.mapping.CreateGISServerConnectionFile(connection_type="ADMINISTER_GIS_SERVICES",
                                            out_folder_path=workSpace,
                                            out_name=outAGSName,
                                            server_url=serverUrl,
                                            server_type="ARCGIS_SERVER",
                                            use_arcgis_desktop_staging_folder=False,
                                            staging_folder_path=workSpace,
                                            username=username,
                                            password=password,
                                            save_username_password=True)
print('ArcGIS Server connection file created: {0}'.format(outAGSName))

# define local variables
mapDoc = arcpy.mapping.MapDocument(os.path.join(workSpace, mxdFile))
print('Map Document: {0}'.format(mapDoc.filePath))
service = mxdFile.split(".")[0]
sddraft = os.path.join(workSpace, service + '.sddraft')
sd = os.path.join(workSpace, service + '.sd')
summary = 'Publishing Map Service Using Python'
tags = 'python'

# create service definition draft
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER',
                                          outAGSName, True, None, summary, tags)
print('Service definition draft file created: {0}'.format(sddraft))

# stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
    if os.path.exists(sd):
        os.remove(sd)
        print("Existing service defination file deleted ... ")
    # Execute StageService
    arcpy.StageService_server(sddraft, sd)
    print('Service definition file created: {0}'.format(sd))
    # Execute UploadServiceDefinition
    print('Uploading service...')
    arcpy.UploadServiceDefinition_server(sd, outAGSName)
    print("Success!")
else:
    # if the sddraft analysis contained errors, display them
    print analysis['errors']