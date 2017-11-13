# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy,time
from arcpy import da

arcpy.env.workspace = r'D:\kikitaDIY\TJDG_Data\TJDG_BAK_20161123.gdb\TJDG'
pointFC = 'RL_Point'   #其他管点
LineFC = 'RL_Line'     #管线
lyr = 'lineFC_lyr'
lastNoneCount = 0

arcpy.env.overwriteOutput = True


def UpdateLineAttribute():
    # 遍历的 lineRL2 出水管的起点编号和终点编号都 非空
    fields = ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID']
    with da.SearchCursor(LineFC, fields, 'HLType = 1 AND S_NodeID IS NOT NULL AND E_NodeID IS NOT NULL') as cursorL2:
        for lineRL2 in cursorL2:
            # 遍历的 lineRL1 出水管的起点编号和终点编号都 空
            with da.UpdateCursor(LineFC, fields, 'HLType = 1 AND S_NodeID IS NULL AND E_NodeID IS NULL') as cursorL1:
                for lineRL1 in cursorL1:
                    # 如果两条线相连接
                    if lineRL1[0].touches(lineRL2[0]):
                        # 未赋值的线的起点为已赋值的线的终点
                        lineRL1[2] = lineRL2[3]
                        with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID']) as cursorP2:
                            # 遍历所有管点
                            for point2 in cursorP2:
                                # 如果管点与空线touch，且不是线起点，则为终点赋值
                                if point2[0].touches(lineRL1[0]) and lineRL1[2] != point2[1]:
                                    lineRL1[3] = point2[1]
                                    cursorL1.updateRow(lineRL1)
                                    print(u'#### <{0}>的起点编号是<{1}>，终点编号是<{2}>.'.format(lineRL1[1],lineRL1[2],lineRL1[3]))
            del lineRL1
            del cursorL1


# 求得起点编号、终点编号都为空的记录数
def NoneCount(fc):
    arcpy.MakeFeatureLayer_management(LineFC, lyr, 'HLType = 1 AND S_NodeID IS NULL AND E_NodeID IS NULL')
    result = arcpy.GetCount_management(lyr)
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



statTime = time.time()
print('Starting...')
# 遍历锅炉房点数据,首次更新线属性
with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID'], 'NodeType = 8') as cursorG:
    for pointGLF in cursorG:
        # 遍历出水管线
        with da.UpdateCursor(LineFC, ['SHAPE@', 'LineID', 'S_NodeID', 'E_NodeID'], 'HLType = 1') as cursorL:
            for lineRL in cursorL:
                if lineRL[2] == None and lineRL[3] == None:
                    if lineRL[0].touches(pointGLF[0]) == True:
                        # 起点编号
                        lineRL[2] = pointGLF[1]
                        # 终点编号
                        with da.SearchCursor(pointFC, ['SHAPE@', 'NodeID'], 'NodeType <> 8') as cursorP:
                            for point in cursorP:
                                if lineRL[0].touches(point[0]) == True:
                                    lineRL[3] = point[1]
                                    cursorL.updateRow(lineRL)
                                    print(u'<{0}>的起点编号是<{1}>，终点编号是<{2}>.'.format(lineRL[1],lineRL[2],lineRL[3]))

# 执行自动顺序赋值函数
IterateLines()
endTime = time.time()
timeCost = endTime - statTime
print(u'共耗时{}分钟...'.format(timeCost))