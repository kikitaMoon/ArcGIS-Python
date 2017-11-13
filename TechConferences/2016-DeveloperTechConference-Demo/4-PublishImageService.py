# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import os
import time

StartTime = time.time()

generalfolder = r'D:\My_Training\Esri_China_UC&DevSummit\2016_China_DS_ArcGIS平台的影像管理技术\Demo4DS2016'
servicename = 'MyFirstImageServicebyPython'
mdpath = os.path.join(generalfolder,
                      r'Demo_2_BuildingRasterGDB\ImageGDB.gdb\MosaicDataset' +'_'+ time.strftime('%m%d',time.localtime(time.time())))


# Step1 创建GIS服务器连接文件

print u'Step1 创建GIS服务器连接文件...'

connecttype = 'ADMINISTER_GIS_SERVICES'
outdir = os.path.join(generalfolder, 'Demo_4_PublishImageService')
out_folder_path = outdir
out_name = 'ConnectToArcGISServer.ags'
server_url = 'https://kikita.mycloud.com:6443/arcgis/admin'
use_staging_folder = False
staging_folder_path = outdir
username = 'kikitamoon'
password = 'kikitamoon123'

arcpy.mapping.CreateGISServerConnectionFile(connecttype,
                                            out_folder_path,
                                            out_name,
                                            server_url,
                                            "ARCGIS_SERVER",
                                            use_staging_folder,
                                            staging_folder_path,
                                            username,
                                            password,
                                            "SAVE_USERNAME")

print '      '+ out_name.decode('utf-8') + u' 已创建'



# Step2 创建影像服务定义草稿文件(.sddraft)

print u'Step2 创建影像服务定义草稿文件...'

connoctionfile = os.path.join(outdir,out_name)
service = servicename
sddraft = os.path.join(outdir , service + '.sddraft')

arcpy.CreateImageSDDraft(mdpath, sddraft, service, 'ARCGIS_SERVER', copy_data_to_server=False)
print '      '+ service + '.sddraft' + u'  已创建'



# Step3 分析服务定义草稿
print u'Step3 分析服务定义草稿文件...'
analysis = arcpy.mapping.AnalyzeForSD(sddraft)

print(u"      分析服务定义草稿结果:")
for key in list(analysis.keys()):
    print("      ---{}---".format(key.upper()))
    for ((message, code), layerlist) in analysis[key].items():
        print("        (CODE {})  {} ".format(code,message))



# Step4 过渡 sddraft 到服务定义文件sd
print u'Step4 过渡sddraft 到服务定义文件sd...'
outSDfile = os.path.join(outdir,service+".sd")

arcpy.StageService_server(sddraft,outSDfile )
print u'      Done!'



# Step5 将服务定义文件发布到服务器
print u'Step5 将服务定义文件发布到服务器...'
inSdFile = outSDfile
inServer = connoctionfile
inServiceName = service

arcpy.UploadServiceDefinition_server(inSdFile, inServer, inServiceName)
print u'      Done!'



# 计时
EndTime = time.time()
print u'耗时:  ' + str(EndTime - StartTime) +  u' 秒 ...'