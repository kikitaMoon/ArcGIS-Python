# -*- coding:utf-8 -*-
__author__ = 'kikita'

import arcpy
import timeit
import time
import multiprocessing
import os

arcpy.env.workspace =  r'D:\LearnAboutPython\MyPythonProject\UsingCurser\DemoDataS.gdb'
arcpy.env.overwriteOutput = True

# Batch Clip Function
def MyBatchClip(Parameter):
    # Parameters
    inputFC = Parameter[0]
    ClipArea = Parameter[1]
    OutputWS = Parameter[2]
    Prefix = Parameter[3]
    # Cursor Fields
    Fields = ['OBJECTID','SHAPE@']
    with arcpy.da.SearchCursor(ClipArea,Fields) as cursor:
        for row in cursor:
            outputFC = os.path.join(OutputWS, Prefix+str(row[0]))
            arcpy.Clip_analysis(inputFC, row[1], outputFC)
            print Prefix+str(row[0])


if __name__ == '__main__':
    # Parameters
    OutputWS = r'D:\LearnAboutPython\MyPythonProject\UsingCurser\OutputWS'
    # OutputWS = r'C:\Users\kikit\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to 192.168.220.131.sde'
    Parameter1 = ['CountyPoints','Area_A',OutputWS, 'AAA_']
    Parameter2 = ['hyd_line','Area_B',OutputWS, 'BBB_']
    # Parameter3 = ['River_line.shp','Area_C.shp',OutputWS,'CCC_']
    Parameters = [Parameter1, Parameter2]
    # current CPU counts
    print 'CPU Count:' + str(multiprocessing.cpu_count())
    # processing pool
    MyGPpool = multiprocessing.Pool()
    # multiprocessing
    StartTime = time.time()
    results = MyGPpool.map(MyBatchClip,Parameters)
    EndTime = time.time()

    print 'Elapsed:  ' + str(EndTime - StartTime) + '  Seconds...'


    #timer = timeit.Timer("MyBatchClip()", setup="from __main__ import MyBatchClip")
    #print timer.timeit(1)