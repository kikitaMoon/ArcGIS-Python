# -*- coding: utf-8 -*-

print 'Importing modules...'

import arcpy
import time
import os

StartTime = time.time()



# 定义变量
ImageGDB_gdb = "D:\\My_Training\\Esri_China_UC&DevSummit\\2016_China_DS_ArcGIS平台的影像管理技术\\Demo4DS2016\\Demo_2_BuildingRasterGDB\\ImageGDB.gdb"
MosaicDataset = "MosaicDataset" + '_'+ time.strftime('%m%d',time.localtime(time.time()))


# 生成接缝线

print u"构建接缝线..."

# 参数
cellsize = "28.5"
sortmethod = "NORTH_WEST"
sortorder = "ASCENDING"
orderattribute = ""
orderbase = ""
viewpnt = ""
computemethod = "RADIOMETRY"
blendwidth = "5"
blendtype = "INSIDE"
requestsize = "1000"

# 执行工具
arcpy.BuildSeamlines_management(os.path.join(ImageGDB_gdb,MosaicDataset), cellsize, sortmethod, sortorder,
                                orderattribute,orderbase, viewpnt, computemethod, blendwidth, blendtype,requestsize)

print "             Done !"




# 创建概视图
print u"创建概视图..."
arcpy.BuildOverviews_management( os.path.join(ImageGDB_gdb,MosaicDataset),
                                 where_clause = "",
                                 define_missing_tiles = "DEFINE_MISSING_TILES",
                                 generate_overviews = "GENERATE_OVERVIEWS",
                                 generate_missing_images = "IGNORE_MISSING_IMAGES",
                                 regenerate_stale_images = "IGNORE_STALE_IMAGES")
print "             Done !"


# 计时
EndTime = time.time()
print u'耗时:  ' + str(EndTime - StartTime) +  u' 秒 ...'



