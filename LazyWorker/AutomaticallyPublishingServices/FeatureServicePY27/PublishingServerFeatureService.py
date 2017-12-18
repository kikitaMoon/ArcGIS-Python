# -*- coding: utf-8 -*-
__author__ = 'kikita'
import arcpy
import xml.dom.minidom as DOM
import os

# batch publishing feature service

# Modify as your workspace
##########################
workSpace = r"D:\GitHubRepositories\ArcGIS-Python\LazyWorker\AutomaticallyPublishingServices"
gisServer = 'kikitapc.mycloud.com'
gisPort = 6443
username = 'portaladmin'
password = 'Super123'
serverUrl = 'https://{0}:{1}/arcgis/admin'.format(gisServer, gisPort)
print(serverUrl)
outAGSName = 'ArcGISServerConnection.ags'
###########################

# Create ArcGIS Server Connection File Function
def createAGSConnection(workSpace, outAGSName, serverUrl, username, password):
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
    return

# Publishing Feature Servcie
def publishingFeatureService(workSpace, mxdFile, outAGSName):

    # define local variables
    mapDoc = arcpy.mapping.MapDocument(os.path.join(workSpace, mxdFile))
    print('Map Document: {0}'.format(mapDoc.filePath))
    service = mxdFile.split(".")[0]
    sddraft = os.path.join(workSpace, service + '.sddraft')
    sd = os.path.join(workSpace, service + '.sd')
    summary = 'Publishing Feature Service Using Python'
    tags = 'python'
    newSDdraft = service + 'FS.sddraft'

    # create service definition draft
    analysis = arcpy.mapping.CreateMapSDDraft(map_document=mapDoc,
                                              out_sddraft=sddraft,
                                              service_name=service,
                                              server_type='ARCGIS_SERVER',
                                              connection_file_path=outAGSName,
                                              copy_data_to_server=False,
                                              folder_name=None,
                                              summary=summary,
                                              tags=tags)

    # # Modify the SDDraft from a MapService to a FeatureService.
    doc = DOM.parse(sddraft)
    tagsType = doc.getElementsByTagName('Type')
    for tagType in tagsType:
        if tagType.parentNode.tagName == 'SVCManifest':
            if tagType.hasChildNodes():
                tagType.firstChild.data = "esriServiceDefinitionType_Replacement"
    tagsState = doc.getElementsByTagName('State')
    for tagState in tagsState:
        if tagState.parentNode.tagName == 'SVCManifest':
            if tagState.hasChildNodes():
                tagState.firstChild.data = "esriSDState_Published"

    # Turn on feature access capabilities
    services___ = doc.getElementsByTagName('TypeName')
    for service__ in services___:
        if service__.firstChild.data == "FeatureServer":
            service__.parentNode.getElementsByTagName('Enabled')[0].firstChild.data = 'true'

    # Write the new draft to disk
    f = open(newSDdraft, 'w')
    doc.writexml(f)
    f.close()

    # Analyze the service
    analysis = arcpy.mapping.AnalyzeForSD(newSDdraft)
    if analysis['errors'] == {}:
        # Stage the service
        if os.path.exists(sd):
            os.remove(sd)
            print("{0} already exists!  Deleted! ".format(sd))
        arcpy.StageService_server(newSDdraft, sd)
        # Upload the service.
        arcpy.UploadServiceDefinition_server(sd, outAGSName, service)
        print "Uploaded and overwrote feature service"
    else:
        # If the sddraft analysis contained errors, display them and quit.
        print analysis['errors']


##### Main Script
if os.path.isdir(workSpace) == False:
    print "Not valid path..."
else:
    createAGSConnection(workSpace, outAGSName, serverUrl, username, password)
    files = os.listdir(workSpace)
    for f in files:
        if f.endswith(".mxd"):
            # mxdPath = os.path.join(workSpace, f)
            print "publishing: " + f
            publishingFeatureService(workSpace, f, outAGSName)
        else:
            continue