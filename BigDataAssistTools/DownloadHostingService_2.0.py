# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import urllib, httplib, json
import time
from arcpy import da

# Python工具参数
# AGSserverName = arcpy.GetParameterAsText(0)
# username = arcpy.GetParameterAsText(1)
# password = arcpy.GetParameterAsText(2)
# servicename = arcpy.GetParameterAsText(3)

# 测试用常量参数
agsservername = 'gis188.arcgisonline.cn'
serverport = 6080
username = 'siteadmin'
passwords = 'esri@123'
servicename = 'chenyl_guangzhouditie_join_1112'
location = 'D:\LearnAboutArcGIS\ArcGIS_Server\BigDataAnalyst\ForTest.gdb'
whereClauseField = 'OBJECTID1'


arcpy.env.workspace = location
arcpy.env.overwriteOutput = True

### 通过 Server Admin 获取 ArcGIS Server Token
def GetToken(username, password, agsservername, serverport):
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    tokenURL = "/arcgis/admin/generateToken"
    # URL-encode the token parameters:-
    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # Connect to URL and post parameters
    httpConn = httplib.HTTPConnection(agsservername, serverport)
    httpConn.request("POST", tokenURL, params, headers)
    # Read response
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print "Error while fetch tokens from admin URL. Please check the URL and try again."
        return
    else:
        data = response.read()
        httpConn.close()
        # Extract the token from it
        token = json.loads(data)
        return token['token']


### 查询需要下载的数据的总条数
def GetCount(servicename):
    # Feature Servcie URL address
    baseURL = r"http://"+agsservername+":"+str(serverport)+"/arcgis/rest/services/Hosted/"+servicename+"/FeatureServer/0/"
    queryParam = "query?where=1%3D1&returnCountOnly=true&f=pjson"
    tokenParam = "&Token=" + myToken
    CountQueryURL = baseURL + queryParam + tokenParam
    # Get response
    CountResponse = urllib.urlopen(CountQueryURL)
    CountData = CountResponse.read()
    # JSON Dictionary
    JSONCountObj = json.loads(CountData)
    return(JSONCountObj['count'])


### 查询要素服务的JSON对象
def FeatureServiceJSON(servicename, whereClause):
    # Feature Servcie URL address
    baseURL = r"http://"+agsservername+":"+str(serverport)+"/arcgis/rest/services/Hosted/"+servicename+"/FeatureServer/0/"
    queryParam = "query?where={}&outFields=*&returnGeometry=true&f=pjson".format(whereClause)
    tokenParam = "&Token=" + myToken
    GeometryQueryURL = baseURL + queryParam + tokenParam
    # print(GeometryQueryURL)
    # Get response
    fsResponse = urllib.urlopen(GeometryQueryURL)
    fsData = fsResponse.read()
    # JSON Dictionary
    JSONdataObj = json.loads(fsData)
    return(JSONdataObj)


### 创建本地要素类及创建Skema
def CreateLocalFeatureClass(location, fcname):
    baseURL = r"http://"+agsservername+":"+str(serverport)+"/arcgis/rest/services/Hosted/"+servicename+"/FeatureServer/0/?f=pjson"
    tokenParam = "&Token=" + myToken
    geotypeQueryURL = baseURL + tokenParam
    fsResponse = urllib.urlopen(geotypeQueryURL)
    fsData = fsResponse.read()
    fsdescription = json.loads(fsData)
    geotype = fsdescription['geometryType'][12:].upper()
    fslayersr = fsdescription['extent']['spatialReference']['wkid']
    arcpy.CreateFeatureclass_management(location, fcname, geometry_type=geotype, spatial_reference=fslayersr )
    fields = fsdescription['fields']
    cursorFields = []
    for field in fields:
        if field['name'].upper() != 'OBJECTID':
            fieldtype = 'TEXT'
        else:
            continue
        # 字段类型映射上目前简单处理，统一为字符串
        # if field['type'][13:] == 'String':
        #     fieldtype = 'TEXT'
        # elif field['name'].upper() == 'OBJECTID':
        #     continue
        # else:
        #     fieldtype = field['type'][13:].upper()
        cursorFields.append(field['name'])
        arcpy.AddField_management(in_table=fcname, field_name=field['name'], field_type=fieldtype, field_alias=field['alias'] )
    return(cursorFields)

### 将JSON对象解析，通过Cursor写入本地要素类
def WriteLocalFC(JSONdataObj, localTarget, cursorFields):
    myJSONfeature = JSONdataObj['features']
    print('#####')
    # print(cursorFields)
    cursor = da.InsertCursor(localTarget, cursorFields)
    j = 0
    for feature in myJSONfeature:
        # Attribute Field Value
        myJSONattr = myJSONfeature[j]['attributes']
        myJSONattrItems = myJSONattr.items()
        myJSONattrItems.sort()
        cursorValues = []
        for item in myJSONattrItems:
            if item[0].upper() != 'OBJECTID':
                cursorValues.append(item[1])
        # Geometry JSON
        myJSONgeometry = myJSONfeature[j]['geometry']
        # print(myJSONgeometry)
        # point
        FineJson = (str({"x":myJSONgeometry['x'],"y":myJSONgeometry['y']}))
        # print(FineJson)
        # Polygon
        # FineJson = (str({"rings": myJSONgeometry['rings']}))
        cursorValues.append(FineJson)
        # print(cursorValues)
        # print(len(cursorValues))
        cursor.insertRow(cursorValues)
        print(j)
        j = j+1
    del cursor



# 脚本从这里开始执行
if __name__ == "__main__":
    myToken = GetToken(username, passwords, agsservername, serverport)
    print('Token - checked! ' )
    cursorFields = CreateLocalFeatureClass(location, servicename)
    cursorFields.sort()
    cursorFields.append('SHAPE@JSON')
    # print(cursorFields)
    # print(len(cursorFields))
    print(servicename+" - Created!")
    totalCount = GetCount(servicename)
    #totalCount = 112585143
    print("To be downloaded:"+str(totalCount))
    i = 0
    st = time.clock()
    while i <= totalCount/2000+1:
        whereClause = whereClauseField+">="+str(i*2000)+" and "+whereClauseField+"<"+str((i+1)*2000)
        myJSON = FeatureServiceJSON(servicename, whereClause)
        WriteLocalFC(myJSON, servicename,cursorFields)
        i = i + 1
        print(whereClause + "   Done!!!")
        # break
    et = time.clock()
    print   str((time.clock() - st)/60.0) + "minutes.."






