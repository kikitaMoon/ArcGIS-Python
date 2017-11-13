# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy,time
from arcpy import da

# What's  New in 2.0 ...
# 增加回水管逻辑

arcpy.env.workspace = r'D:\kikitaDIY\TJDG_Data\TJDG_BAK_20161123.gdb'
pointFC = 'RL_Point'   # 管点
LineFC = 'RL_Line'     # 管线
arcpy.env.overwriteOutput = True

# 更新起始管线的起点终点编号
def GetStartingLine(glfID, rhID):
    with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID', 'NodeType'], 'NodeType = {0} OR NodeType = {1}'.format(glfID, rhID)) as cursorOrigin:
        for pointOrigin in cursorOrigin:
            # 如果是锅炉房点，则遍历出水管
            if pointOrigin[2] == glfID:
                hltype = 1
                with da.UpdateCursor(LineFC, ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID'], 'HLType = {0}'.format(hltype)) as cursorL:
                    for lineRL in cursorL:
                        if lineRL[2] == None and lineRL[3] == None:
                            if lineRL[0].touches(pointOrigin[0]) == True:
                                # 起点编号
                                lineRL[2] = pointOrigin[1]
                                # 终点编号
                                with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID'], 'NodeType <> {0}'.format(pointOrigin[2])) as cursorP:
                                    for point in cursorP:
                                        if lineRL[0].touches(point[0]) == True:
                                            lineRL[3] = point[1]
                                            cursorL.updateRow(lineRL)
                                            print(u'出水管<{0}>：起点 <{1}>，终点 <{2}>.'.format(lineRL[1],lineRL[2],lineRL[3]))
            # 入户点，则遍历回水管
            elif pointOrigin[2] == rhID:
                hltype = 0
                with da.UpdateCursor(LineFC, ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID'], 'HLType = {0}'.format(hltype)) as cursorL:
                    for lineRL in cursorL:
                        if lineRL[2] == None and lineRL[3] == None:
                            if lineRL[0].touches(pointOrigin[0]) == True:
                                # 起点编号
                                lineRL[3] = pointOrigin[1]
                                # 终点编号
                                with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID'], 'NodeType <> {0}'.format(pointOrigin[2])) as cursorP:
                                    for point in cursorP:
                                        if lineRL[0].touches(point[0]) == True:
                                            lineRL[2] = point[1]
                                            cursorL.updateRow(lineRL)
                                            print(u'回水管<{0}>：起点 <{1}>，终点 <{2}>.'.format(lineRL[1],lineRL[2],lineRL[3]))


def UpdateLineAttribute():
    # 遍历的 lineRL2 出水管的起点编号和终点编号都 非空
    fields = ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID', 'HLType']
    with da.SearchCursor(LineFC, fields, 'S_NodeID IS NOT NULL AND E_NodeID IS NOT NULL') as cursorL2:
        for lineRL2 in cursorL2:
            # 遍历的 lineRL1 出水管的起点编号和终点编号都 空
            with da.UpdateCursor(LineFC, fields, 'HLType = {0} AND S_NodeID IS NULL AND E_NodeID IS NULL'.format(lineRL2[4])) as cursorL1:
                for lineRL1 in cursorL1:
                    # 如果两条线相连接
                    if lineRL1[0].touches(lineRL2[0]):
                        if lineRL1[4] == 1:         # 出水管起点
                            lineRL1[2] = lineRL2[3]
                        elif lineRL1[4] == 0:       # 回水管终点
                            lineRL1[3] = lineRL2[3]
                        with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID']) as cursorP2:
                            # 遍历所有管点
                            for point2 in cursorP2:
                                # 如果管点与空线touch，且不是线起点，则为终点赋值
                                if point2[0].touches(lineRL1[0]) and lineRL1[2] != point2[1]:
                                    if lineRL1[4] == 1:        # 出水管
                                        lineRL1[3] = point2[1]
                                    elif lineRL1[4] == 0:      # 回水管
                                        lineRL1[2] = point2[1]
                                    cursorL1.updateRow(lineRL1)
                                    print(u'## <{0}>: 起点 <{1}>，终点 <{2}>.'.format(lineRL1[1], lineRL1[2], lineRL1[3]))
            del lineRL1
            del cursorL1


# 求得起点编号、终点编号都为空的记录数
def NoneCount(fc):
    arcpy.MakeFeatureLayer_management(LineFC, 'lineFC_lyr', 'S_NodeID IS NULL AND E_NodeID IS NULL')
    result = arcpy.GetCount_management('lineFC_lyr')
    count = int(result.getOutput(0))
    return(count, fc)


# 通过记录数递归
def IterateLines():
    nonecount = NoneCount(LineFC)[0]
    print(u'剩余{}条管线尚未分配编号,即将执行...'.format(nonecount))
    while nonecount:
            UpdateLineAttribute()
            if NoneCount(LineFC)[0] < nonecount:
                IterateLines()


if __name__ == '__main__':
    statTime = time.time()
    print('{0} Starting...'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    GetStartingLine(8, 6)   # 锅炉房点-8，入户点-6
    print(u'管线起始段赋值完成。')
    IterateLines()
    endTime = time.time()
    timeCost = endTime - statTime
    print(u'共耗时{}分钟...'.format(timeCost))