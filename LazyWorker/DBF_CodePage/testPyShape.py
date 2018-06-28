#-*-coding:utf-8 -*-

__author__ = 'kikita'

import shapefile

w = shapefile.Writer(shapefile.POINT)
w.point(1,1)
w.point(3,1)
w.point(4,3)
w.point(2,2)
w.field('中文')
w.field('SECOND_FLD','C','40')
w.record('中文','Point')
w.record('Second','Point')
w.record('Third','Point')
w.record('Fourth','Point')

w.save(u'D:\IncidentSupport2015\AllforTest\CodePagesTest\ChineseField\ExportShapefiles\pyshape')

string = "中文"