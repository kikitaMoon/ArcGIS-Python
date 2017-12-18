# -*- coding: utf-8 -*-
__author__ = 'kikita'
import arcpy
import xml.dom.minidom as DOM
import os

# Modify as your workspace
##########################
workSpace = r"D:\GitHubRepositories\ArcGIS-Python\LazyWorker\AutomaticallyPublishingServices"
mxdFile = 'SDESource.mxd'
portaluser = 'portaladmin'
psd = 'Super123'
###########################


# Publishing Feature Servcie
def publishingHostedFeatureService(workSpace, mxdFile):

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
                                              server_type='MY_HOSTED_SERVICES',
                                              connection_file_path='',
                                              copy_data_to_server=False,
                                              folder_name=None,
                                              summary=summary,
                                              tags=tags)

    # Modify the SDDraft from a MapService to a FeatureService.
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

    # Change service type from map service to feature service
    typeNames = doc.getElementsByTagName('TypeName')
    for typeName in typeNames:
        if typeName.firstChild.data == "MapServer":
            typeName.firstChild.data = "FeatureServer"

    # # Turn off caching
    configProps = doc.getElementsByTagName('ConfigurationProperties')[0]
    propArray = configProps.firstChild
    propSets = propArray.childNodes
    for propSet in propSets:
        keyValues = propSet.childNodes
        for keyValue in keyValues:
            if keyValue.tagName == 'Key':
                if keyValue.firstChild.data == "isCached":
                    keyValue.nextSibling.firstChild.data = "false"

    # # Turn on feature access capabilities
    configProps = doc.getElementsByTagName('Info')[0]
    propArray = configProps.firstChild
    propSets = propArray.childNodes
    for propSet in propSets:
        keyValues = propSet.childNodes
        for keyValue in keyValues:
            if keyValue.tagName == 'Key':
                if keyValue.firstChild.data == "WebCapabilities":
                    keyValue.nextSibling.firstChild.data = "Query,Create,Update,Delete,Uploads,Editing"

    # Write the new draft to disk
    f = open(newSDdraft, 'w')
    doc.writexml(f)
    f.close()
    # Analyze the service
    analysis = arcpy.mapping.AnalyzeForSD(newSDdraft)
    if analysis['errors'] == {}:
        if os.path.exists(sd):
            os.remove(sd)
            print("{0} already exists!  Deleted! ".format(sd))
        # Stage the service
        arcpy.StageService_server(newSDdraft, sd)
        # Upload the service.
        arcpy.UploadServiceDefinition_server(in_sd_file=sd, in_server="My Hosted Services")
        print "Uploaded and overwrote service"
    else:
        # If the sddraft analysis contained errors, display them and quit.
        print analysis['errors']


##### Main Script
if os.path.isdir(workSpace) == False:
    print "Not valid path..."
else:
    arcpy.SignInToPortal_server(portaluser, psd, "")
    print(arcpy.GetActivePortalURL())
    files = os.listdir(workSpace)
    for f in files:
        if f.endswith(".mxd"):
            # mxdPath = os.path.join(workSpace, f)
            print("publishing: "+f)
            publishingHostedFeatureService(workSpace, f)
            print(f+" Publishing Done !")
        else:
            continue