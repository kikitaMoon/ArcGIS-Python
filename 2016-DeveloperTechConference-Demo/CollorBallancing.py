# -*- coding: utf-8 -*-

print 'Importing modules...'

import arcpy
import time
import os

StartTime = time.time()

arcpy.env.workspace = "D:\\My_Training\\Esri_China_UC&DevSummit\\2016_China_DS_ArcGIS平台的影像管理技术\\Demo4DS2016\\Demo_2_BuildingRasterGDB\\ImageGDB.gdb"
arcpy.env.overwriteOutput = True


# 定义变量
ImageGDB_gdb = arcpy.env.workspace
MosaicDataset = "MosaicDataset" +'_'+ time.strftime('%m%d',time.localtime(time.time()))



# 首次匀色处理
# arcpy.ColorBalanceMosaicDataset_management(MosaicDataset, "DODGING", "SECOND_ORDER","", "", "NONE", "1", "",)




# 指定一个目标栅格匀色处理

print u"执行色彩平衡..."

target_raster_workspace = r'D:\My_Training\Esri_China_UC&DevSummit\2016_China_DS_ArcGIS平台的影像管理技术\Demo4DS2016\Demo_2_BuildingRasterGDB'
target_raster = 'TemplateRaster.tif'

arcpy.ColorBalanceMosaicDataset_management(MosaicDataset,
                                           balancing_method = "DODGING",
                                           color_surface_type = "SECOND_ORDER",
                                           target_raster = os.path.join(target_raster_workspace,target_raster),
                                           exclude_raster = "",
                                           stretch_type = "",
                                           gamma = "",
                                           block_field = "")

print "             Done !"



# 创建概视图
print u"创建概视图..."
arcpy.BuildOverviews_management( MosaicDataset,
                                 where_clause = "",
                                 define_missing_tiles = "DEFINE_MISSING_TILES",
                                 generate_overviews = "GENERATE_OVERVIEWS",
                                 generate_missing_images = "IGNORE_MISSING_IMAGES",
                                 regenerate_stale_images = "IGNORE_STALE_IMAGES")
print "             Done !"


# 计时
EndTime = time.time()
print u'耗时:  ' + str(EndTime - StartTime) +  u' 秒 ...'



