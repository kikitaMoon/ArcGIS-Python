# -*- coding: utf-8 -*-
__author__ = 'kikita'
import arcpy
import xml.dom.minidom as DOM

# Add Layer
arcpy.env.workspace = r'D:\LearnAboutPython\MyPythonProject\PublicFeatureService20170220'
mxdFilePath = "onelayer.mxd"
mxd = arcpy.mapping.MapDocument(mxdFilePath)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.Layer("SDE.testSDOgeometry.lyr")

# ##### Wrong
# outFolderPath = r'D:\LearnAboutPython\MyPythonProject\PublicFeatureService20170220'
# outName = 'oracleConnection.sde'
# sdePath = outFolderPath + '\\' + outName
# print(sdePath + "\LF.sdoCity")
# lyr = arcpy.mapping.Layer(sdePath + "\LF.sdoCity")
# ##### Wrong

arcpy.mapping.AddLayer(df, lyr, "AUTO_ARRANGE")
mxd.saveACopy("onelayerNew2.mxd")



# Publishing Feature Servcie
service = 'myFeatureSerice'
sddraft = service + '.sddraft'
SD = service + '.sd'
summary = 'test'
tags = 'test'

newSDdraft = service + 'FS.sddraft'

# create service definition draft
analysis = arcpy.mapping.CreateMapSDDraft(map_document="onelayerNew.mxd",
                                          out_sddraft=sddraft,
                                          service_name=service,
                                          server_type='ARCGIS_SERVER',
                                          connection_file_path='AGSConnection.ags',
                                          copy_data_to_server=False,
                                          folder_name=None,
                                          summary=summary,
                                          tags=tags)
if analysis['errors'] == {}:
    arcpy.StageService_server(sddraft, sd)
    arcpy.UploadServiceDefinition_server(sd, 'AGSConnection.ags')
else:
    print analysis['errors']


# The follow 5 code pieces modify the SDDraft from a new MapService
# with caching capabilities to a FeatureService with Query,Create,
# Update,Delete,Uploads,Editing capabilities. The first two code
# pieces handle overwriting an existing service. The last three pieces
# change Map to Feature Service, disable caching and set appropriate
# capabilities. You can customize the capabilities by removing items.
# Note you cannot disable Query from a Feature Service.

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

# Turn off caching
configProps = doc.getElementsByTagName('ConfigurationProperties')[0]
propArray = configProps.firstChild
propSets = propArray.childNodes
for propSet in propSets:
    keyValues = propSet.childNodes
    for keyValue in keyValues:
        if keyValue.tagName == 'Key':
            if keyValue.firstChild.data == "isCached":
                keyValue.nextSibling.firstChild.data = "false"

# Turn on feature access capabilities
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
    # Stage the service
    arcpy.StageService_server(newSDdraft, SD)

    # Upload the service. The OVERRIDE_DEFINITION parameter allows you to override the
    # sharing properties set in the service definition with new values. In this case,
    # the feature service will be shared to everyone on ArcGIS.com by specifying the
    # SHARE_ONLINE and PUBLIC parameters. Optionally you can share to specific groups
    # using the last parameter, in_groups.
    arcpy.UploadServiceDefinition_server(SD, "My Hosted Services", serviceName,
                                         "", "", "", "", "OVERRIDE_DEFINITION", "SHARE_ONLINE",
                                         "PUBLIC", "SHARE_ORGANIZATION", "")

    print "Uploaded and overwrote service"

else:
    # If the sddraft analysis contained errors, display them and quit.
    print analysis['errors']
