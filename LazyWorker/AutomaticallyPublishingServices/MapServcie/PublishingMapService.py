# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy, os

outFolderPath = os.getcwd()
print outFolderPath
outAGSName = 'ArcGISServerConnection.ags'
gisServer = '192.168.100.115'
gisPort = 6443
username = 'arcgis'
password = 'Super123'

serverUrl = 'https://{0}:{1}/arcgis/admin'.format(gisServer, gisPort)
print(serverUrl)

path = outFolderPath + '\\' + outAGSName
if os.path.exists(outFolderPath + '\\' + outAGSName):
    os.remove(path)


arcpy.mapping.CreateGISServerConnectionFile(connection_type="ADMINISTER_GIS_SERVICES",
                                            out_folder_path=outFolderPath,
                                            out_name=outAGSName,
                                            server_url=serverUrl,
                                            server_type="ARCGIS_SERVER",
                                            use_arcgis_desktop_staging_folder=False,
                                            staging_folder_path=outFolderPath,
                                            username=username,
                                            password=password,
                                            save_username_password=True)


# define local variables
wrkspc = 'C:/Project/'
mapDoc = arcpy.mapping.MapDocument(wrkspc + 'counties.mxd')
con = 'GIS Servers/arcgis on MyServer_6080 (publisher).ags'
service = 'Counties'
sddraft = wrkspc + service + '.sddraft'
sd = wrkspc + service + '.sd'
summary = 'Population Density by County'
tags = 'county, counties, population, density, census'

# create service definition draft
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER',
                                          con, True, None, summary, tags)

# stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
    # Execute StageService
    arcpy.StageService_server(sddraft, sd)
    # Execute UploadServiceDefinition
    arcpy.UploadServiceDefinition_server(sd, con)
else:
    # if the sddraft analysis contained errors, display them
    print analysis['errors']