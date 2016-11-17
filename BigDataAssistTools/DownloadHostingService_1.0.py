# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import urllib, httplib, json
import sys,os
from arcpy import da

arcpy.env.workspace = 'D:\LearnAboutArcGIS\ArcGIS_Server\BigDataAnalyst\ForTest.gdb'
arcpy.env.overwriteOutput = True

# Request an administrative token from ArcGIS Server.
def GetToken(username, password, serverName, serverPort):
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    tokenURL = "/arcgis/admin/generateToken"
    # URL-encode the token parameters:-
    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # Connect to URL and post parameters
    httpConn = httplib.HTTPConnection(serverName, serverPort)
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

# Get total count of the Query
def GetCount(serviceName):
    # Feature Servcie URL address
    baseURL = r"http://wa.arcgisonline.cn/arcgis/rest/services/Hosted/"+serviceName+"/FeatureServer/0/"
    queryParam = "query?where=1%3D1&returnCountOnly=true&f=pjson"
    tokenParam = "&Token=" + myToken
    CountQueryURL = baseURL + queryParam + tokenParam
    # Get response
    CountResponse = urllib.urlopen(CountQueryURL)
    CountData = CountResponse.read()
    # JSON Dictionary
    JSONCountObj = json.loads(CountData)
    return(JSONCountObj['count'])

# Get Feature Service JSON
def FeatureServiceJSON(serviceName, fields, whereClause):
    # Feature Servcie URL address
    baseURL = r"http://wa.arcgisonline.cn/arcgis/rest/services/Hosted/"+serviceName+"/FeatureServer/0/"
    queryParam = "query?where={}&outFields={}&returnGeometry=true&f=pjson".format(whereClause, fields)
    tokenParam = "&Token=" + myToken
    GeometryQueryURL = baseURL + queryParam + tokenParam
    # Get response
    fsResponse = urllib.urlopen(GeometryQueryURL)
    fsData = fsResponse.read()
    # JSON Dictionary
    JSONdataObj = json.loads(fsData)
    return(JSONdataObj)

# Write down the JSON Query to Local Feature Class
def WriteLocalFC(JSONdataObj,localTarget):
    myJSONfeature = JSONdataObj['features']
    cursorFields = ['SHAPE@JSON']
    cursorFields.append(Fields)
    cursor = da.InsertCursor(localTarget, cursorFields)
    j = 0
    for feature in myJSONfeature:
        myJSONgeometry = myJSONfeature[j]['geometry']
        myJSONattr = myJSONfeature[j]['attributes']
        FineJson = (str({"rings": myJSONgeometry['rings']}))
        cursor.insertRow([FineJson, myJSONattr[Fields]])
        j = j+1


# The Script start here ...
if __name__ == "__main__":
    # Generate Token
    myToken = GetToken('siteadmin', 'esri@123', 'gis188.arcgisonline.cn', 6080)
    print('Token has been checked: ' + myToken)
    # Query JSON
    serviceName = 'chenyl_nyctaxi_trip_1km_1028'
    Fields = "COUNT"
    totalCount = GetCount(serviceName)
    print(totalCount)
    i = 0
    localTarget = 'chenyl_nyctaxi_trip_1km_1028'
    while i <= totalCount/1000+1:
        whereClause = "OBJECTID>="+str(i*1000)+" and OBJECTID<"+str((i+1)*1000)
        myJSON = FeatureServiceJSON(serviceName, Fields, whereClause)
        WriteLocalFC(myJSON, localTarget)
        i = i + 1
        print(whereClause + "   Done!!!")







