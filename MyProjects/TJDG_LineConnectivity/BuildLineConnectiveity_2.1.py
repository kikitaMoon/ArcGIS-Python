# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import time
from arcpy import da

# 参数示例：
# rlLine = r'D:\DemoData_1207.gdb\RL_Line'    # 管线数据
# rlPoint = r'D:\DemoData_1207.gdb\RL_Point'  # 管点数据
# pointType = 8   # 锅炉房点-8，管线起点/终点


### CMD Paramaters
rlLine = sys.argv[1]
rlPoint = sys.argv[2]
pointType = sys.argv[3]

nonecount = 0

# 更新出水起始管线的起点终点编号
def stratingline(linefc, pointfc, nodetype, linetype):
    with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID'], 'NodeType = {0}'.format(nodetype)) as cursorG:
        for pointGLF in cursorG:
            with da.UpdateCursor(linefc, ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID'],
                                 'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(linetype)) as cursorL:
                for lineRL in cursorL:
                    if lineRL[0].touches(pointGLF[0]):
                        lineRL[2] = pointGLF[1]
                        with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID'], 'NodeType <> {0}'.format(nodetype)) as cursorP:
                            for point in cursorP:
                                if lineRL[0].touches(point[0]):
                                    lineRL[3] = point[1]
                                    cursorL.updateRow(lineRL)
                                    print(u'  出水管<{0}>：起点<{1}>，终点<{2}>.'.format(lineRL[1], lineRL[2], lineRL[3]))
                        del cursorP
            del cursorL
    del cursorG

# 更新其他出水管线
def commonline(linefc, pointfc, linetype):
    fields = ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID']
    with da.SearchCursor(linefc, fields, 'HLType = {0} AND S_NodeID IS NOT NULL AND E_NodeID IS NOT NULL'.format(linetype)) as cursorL2:
        for lineRL2 in cursorL2:
            with da.UpdateCursor(linefc, fields, 'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(linetype)) as cursorL1:
                for lineRL1 in cursorL1:
                    if lineRL1[0].touches(lineRL2[0]):
                        with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID']) as cursorP:
                            for point in cursorP:
                                if point[0].touches(lineRL1[0]) and point[0].touches(lineRL2[0]):
                                    lineRL1[2] = point[1]
                                    with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID']) as cursorP2:
                                        for point2 in cursorP2:
                                            if point2[0].touches(lineRL1[0]) and lineRL1[2] != point2[1]:
                                                lineRL1[3] = point2[1]
                                                cursorL1.updateRow(lineRL1)
                                                print(u'  出水管<{0}>：起点<{1}>，终点<{2}>.'.format(lineRL1[1], lineRL1[2], lineRL1[3]))
                                    del cursorP2
                        del cursorP
            del cursorL1
    del cursorL2

# 更新回水末端管线的起点终点编号
def endingline(linefc, pointfc, nodetype, linetype):
    with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID'], 'NodeType = {0}'.format(nodetype)) as cursorG:
        for pointGLF in cursorG:
            with da.UpdateCursor(linefc, ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID'],
                     'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(linetype)) as cursorL:
                for lineRL in cursorL:
                    if lineRL[0].touches(pointGLF[0]):
                        lineRL[3] = pointGLF[1]
                        with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID'], 'NodeType <> {0}'.format(nodetype)) as cursorP:
                            for point in cursorP:
                                if lineRL[0].touches(point[0]):
                                    lineRL[2] = point[1]
                                    cursorL.updateRow(lineRL)
                                    print(u'  回水管<{0}>：起点<{1}>，终点<{2}>.'.format(lineRL[1], lineRL[2], lineRL[3]))
                        del cursorP
            del cursorL
    del cursorG

# 更新其他回水管线
def commonlinehs(linefc, pointfc, linetype):
    fields = ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID']
    with da.SearchCursor(linefc, fields, 'HLType = {0} AND S_NodeID IS NOT NULL AND E_NodeID IS NOT NULL'.format(linetype)) as cursorL2:
        for lineRL2 in cursorL2:
            with da.UpdateCursor(linefc, fields, 'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(linetype)) as cursorL1:
                for lineRL1 in cursorL1:
                    if lineRL1[0].touches(lineRL2[0]):
                        with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID']) as cursorP:
                            for point in cursorP:
                                if point[0].touches(lineRL1[0]) and point[0].touches(lineRL2[0]):
                                    lineRL1[3] = point[1]
                                    with da.SearchCursor(pointfc, ['SHAPE@', 'NodeID']) as cursorP2:
                                        for point2 in cursorP2:
                                            if point2[0].touches(lineRL1[0]) and lineRL1[3] != point2[1]:
                                                lineRL1[2] = point2[1]
                                                cursorL1.updateRow(lineRL1)
                                                print(u'  回水管<{0}>：起点<{1}>，终点<{2}>.'.format(lineRL1[1], lineRL1[2], lineRL1[3]))
                                    del cursorP2
                        del cursorP
            del cursorL1
    del cursorL2

# 求得起点编号、终点编号都为空的记录数
def nullcount(linefc, linetype):
    lyr = arcpy.MakeFeatureLayer_management(linefc, 'lyr',
                                      'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(linetype))

    result = arcpy.GetCount_management('lyr')
    count = int(result.getOutput(0))
    del lyr
    return(count)

### 通过记录数递归
def iteratelines(linefc, pointfc, lineType):
    global nonecount
    nonecount = nullcount(linefc, lineType)
    nonecountPre = nonecount
    while nonecount:
        if nonecount and lineType == 1:    # 出水管
            print(u'剩余{0}条出水管线尚未分配编号,即将执行；'.format(nonecount))
            commonline(linefc, pointfc, lineType)
        elif nonecount and lineType == 0:  # 回水管
            print(u'剩余{0}条回水管线尚未分配编号,即将执行；'.format(nonecount))
            commonlinehs(linefc, pointfc, lineType)
        nonecount = nullcount(linefc, lineType)
        if nonecount and nonecount < nonecountPre:
            iteratelines(linefc, pointfc, lineType)
        elif nonecount and nonecount == nonecountPre:
            print(u'仍然有{0}条管线没有处理，请检查这些数据是否符合规范，修正数据后重新执行脚本。'.format(nonecount))
            nonecount = 0


if __name__ == '__main__':
    arcpy.env.overwriteOutput = True
    statTime = time.time()
    print('{0} Starting...'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    rltype = [1, 0]         # 出水管-1，回水管-0
    for ltype in rltype:
        if ltype == 1:
            stratingline(rlLine, rlPoint, pointType, ltype)
            print(u'* 出水管线起始段完成；')
            iteratelines(rlLine, rlPoint, ltype)
            print(u'* 出水管线全部完成。')
        elif ltype == 0:
            endingline(rlLine, rlPoint, pointType, ltype)
            print(u'* 回水管线起始段完成；')
            iteratelines(rlLine, rlPoint, ltype)
            print(u'* 回水管线全部完成。')
    endTime = time.time()
    timeCost = (endTime - statTime)/60
    print(u'共耗时{}分钟...'.format(round(timeCost,2)))