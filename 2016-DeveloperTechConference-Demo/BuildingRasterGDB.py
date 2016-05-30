# -*- coding: utf-8 -*-

print 'Importing modules...'

import arcpy
import time

StartTime = time.time()

arcpy.env.workspace = "D:\\My_Training\\Esri_China_UC&DevSummit\\2016_China_DS_ArcGIS平台的影像管理技术\\Demo4DS2016\\Demo_2_BuildingRasterGDB\\ImageGDB.gdb"
arcpy.env.overwriteOutput = True


# 定义变量
ImageGDB_gdb = arcpy.env.workspace
MosaicDataset = "MosaicDataset" + '_'+time.strftime('%m%d',time.localtime(time.time()))
CoordinateSystem = arcpy.SpatialReference(3857)
SourceRasterWorkspace = "D:\\LearnAboutArcGIS\\ArcGIS_Desktop\\I_栅格数据管理\\DemoData\\E10_13_影像产品建库_Beijing\\processed_imagery"



# # 预处理 -- 构建原始栅格数据金字塔统计值

# includedir = "INCLUDE_SUBDIRECTORIES"
# buildpy = "BUILD_PYRAMIDS"
# calcstats = "CALCULATE_STATISTICS"
# buildsource = "NONE"
# blockfield = "#"
# estimatemd = "#"
# skipx = "1"
# skipy = "1"
# ignoreval = ""
# pylevel = "-1"
# skipfirst = "NONE"
# resample = "NEAREST"
# compress = "DEFAULT"
# quality = "75"
# skipexist = "SKIP_EXISTING"
# arcpy.BuildPyramidsandStatistics_management( SourceRasterWorkspace, includedir, buildpy, calcstats, buildsource,
#                                              blockfield,estimatemd, skipx, skipy, ignoreval, pylevel, skipfirst,
#                                              resample, compress, quality, skipexist)

# arcpy.BuildPyramidsandStatistics_management( RawRasterWorkspace,"INCLUDE_SUBDIRECTORIES","BUILD_PYRAMIDS","CALCULATE_STATISTICS",
#                                              "NONE","","NONE","1","1","","-1","NONE","NEAREST","DEFAULT","75","SKIP_EXISTING")




# Step1 创建镶嵌数据集
arcpy.CreateMosaicDataset_management( ImageGDB_gdb, MosaicDataset, CoordinateSystem, product_definition = "None" )
print u"Step1 创建镶嵌数据集 " + MosaicDataset + "- Done"


# Step2 加入栅格
arcpy.AddRastersToMosaicDataset_management( MosaicDataset,"Raster Dataset",SourceRasterWorkspace ,
                                            "UPDATE_CELL_SIZES","UPDATE_BOUNDARY","NO_OVERVIEWS","",
                                            "0","1500","","","SUBFOLDERS","ALLOW_DUPLICATES","NO_PYRAMIDS",
                                            "NO_STATISTICS","NO_THUMBNAILS","","NO_FORCE_SPATIAL_REFERENCE",
                                            "NO_STATISTICS", "")

print u"Step2 加入源栅格数据 - Done"



# Step3 除黑边 -- 定义无效值
arcpy.DefineMosaicDatasetNoData_management( MosaicDataset, "4", "ALL_BANDS 0", "", "", "#",)
print u"Step3 定义镶嵌数据集无效值 - Done"


# Step4 重新构建轮廓线
arcpy.BuildFootprints_management(MosaicDataset, "", "RADIOMETRY", "1", "255", "4", "1000", "NO_MAINTAIN_EDGES",
                                 "SKIP_DERIVED_IMAGES", "UPDATE_BOUNDARY", "2000", "100", "NONE", "", "20", "1")
print u"Step4 构建轮廓线 - Done"


# Step5 匀色处理

arcpy.ColorBalanceMosaicDataset_management(MosaicDataset, "DODGING", "SECOND_ORDER","", "", "NONE", "", "",)
print u"Step5 色彩平衡 - Done"


# Step6 创建概视图
#arcpy.BuildOverviews_management( MosaicDataset, "", "DEFINE_MISSING_TILES", "GENERATE_OVERVIEWS",
#                                 "GENERATE_MISSING_IMAGES", "REGENERATE_STALE_IMAGES")
#print u"Step6 创建概视图 - Done"


# 计时
EndTime = time.time()
print u'耗时:  ' + str(EndTime - StartTime) +  u' 秒 ...'



