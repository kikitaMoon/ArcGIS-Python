# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import datetime
starttime = datetime.datetime.now()
#long running
import arcpy
endtime = datetime.datetime.now()

t = endtime - starttime

print(t.seconds)