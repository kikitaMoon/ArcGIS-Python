# -*- coding: utf-8 -*-
__author__ = 'kikita'

import arcpy
import urllib
import httplib, json, time
from arcpy import da

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "DownloadServiceData"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [DownloadFeatureService]

class DownloadFeatureService(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Download Feature Service"
        self.description = "Download Hosting Feature Service Data ..."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""

        param0 = arcpy.Parameter(
            displayName="Feature Service URL",
            name="ServiceURL",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="User Name",
            name="username",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        param2 = arcpy.Parameter(
            displayName="Password",
            name="passwords",
            datatype="GPStringHidden",
            parameterType="Required",
            direction="Input")

        param3 = arcpy.Parameter(
            displayName="OID Field",
            name="whereClauseField",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        param3.value = 'objectid'

        param4 = arcpy.Parameter(
        displayName="Output Feature Class Location",
        name="location",
        datatype="DEWorkspace",
        parameterType="Required",
        direction="Input")

        params = [param0,param1,param2,param3,param4]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        ### Get ArcGIS Server Admin Token
        def GetToken(username, password, agsservername, serverport):
            # Token URL is typically http://server[:port]/arcgis/admin/generateToken
            tokenURL = "/arcgis/admin/generateToken"
            # URL-encode the token parameters:-
            params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            # Connect to URL and post parameters
            httpConn = httplib.HTTPConnection(agsservername, int(serverport))
            httpConn.request("POST", tokenURL, params, headers)
            # Read response
            response = httpConn.getresponse()
            arcpy.AddMessage(response.status)
            if (response.status != 200):
                httpConn.close()
                arcpy.AddMessage("Error while fetch tokens from admin URL. Please check the URL and try again.")
                return
            else:
                data = response.read()
                httpConn.close()
                # Extract the token from it
                token = json.loads(data)
                arcpy.AddMessage(data)
                return token['token']

        ### Query the Total Count of the Feature Data
        def GetCount(servicename):
            # Feature Servcie URL address
            baseURL = ServiceURL
            queryParam = "/query?where=1%3D1&returnCountOnly=true&f=pjson"
            tokenParam = "&Token=" + myToken
            CountQueryURL = baseURL + queryParam + tokenParam
            # Get response
            CountResponse = urllib.urlopen(CountQueryURL)
            CountData = CountResponse.read()
            # JSON Dictionary
            JSONCountObj = json.loads(CountData)
            return(JSONCountObj['count'])

        ### Query the Maximum Value of OBJECTID
        def GetMaxOBJECTID():
            # Feature Servcie URL address
            baseURL = ServiceURL
            queryParam = "/query?where=1%3D1&outStatistics=%5B%7B%0D%0A++++%22statisticType%22%3A+%22max%22%2C%0D%0A++++%22onStatisticField%22%3A+%22"+whereClauseField+"%22%2C%0D%0A++++%22outStatisticFieldName%22%3A+%22Max_OID%22%0D%0A++%7D%5D&f=pjson"
            tokenParam = "&Token=" + myToken
            CountQueryURL = baseURL + queryParam + tokenParam
            # Get response
            CountResponse = urllib.urlopen(CountQueryURL)
            CountData = CountResponse.read()
            # JSON Dictionary
            JSONCountObj = json.loads(CountData)
            return(JSONCountObj['features'][0]['attributes']['Max_OID'])

        ### Query maxRecordCount
        def GetmaxRecordCount():
            # Feature Servcie URL address
            baseURL = ServiceURL+"/?f=pjson"
            tokenParam = "&Token=" + myToken
            MaxRCQueryURL = baseURL + tokenParam
            MaxRCResponse = urllib.urlopen(MaxRCQueryURL)
            fsData = MaxRCResponse.read()
            MaxRCobj = json.loads(fsData)
            return(MaxRCobj['maxRecordCount'])

        ### Request Feature Service JSON Object
        def FeatureServiceJSON(servicename, whereClause):
            # Feature Servcie URL address
            baseURL = ServiceURL
            queryParam = "/query?where={}&outFields=*&returnGeometry=true&f=pjson".format(whereClause)
            tokenParam = "&Token=" + myToken
            GeometryQueryURL = baseURL + queryParam + tokenParam
            # Get response
            fsResponse = urllib.urlopen(GeometryQueryURL)
            fsData = fsResponse.read()
            # JSON Dictionary
            JSONdataObj = json.loads(fsData)
            return(JSONdataObj)

        ### Create Local Feature Class
        def CreateLocalFeatureClass(location, fcname):
            # Feature Servcie URL address
            baseURL = ServiceURL+"/?f=pjson"
            tokenParam = "&Token=" + myToken
            geotypeQueryURL = baseURL + tokenParam
            fsResponse = urllib.urlopen(geotypeQueryURL)
            fsData = fsResponse.read()
            fsdescription = json.loads(fsData)
            global geotype
            geotype = fsdescription['geometryType'][12:].upper()
            fslayersr = fsdescription['extent']['spatialReference']['wkid']
            arcpy.CreateFeatureclass_management(location, fcname, geometry_type=geotype, spatial_reference=fslayersr )
            fields = fsdescription['fields']
            cursorFields = []
            for field in fields:
                if field['name'].upper() == 'OBJECTID':
                    continue
                elif field['type'][13:].upper() == 'DOUBLE':
                    fieldtype = 'DOUBLE'
                else:
                    fieldtype = 'TEXT'
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

        ### Analyzing JSON Object， and Write the data to local Feature Class with
        def WriteLocalFC(JSONdataObj, localTarget, cursorFields):
            myJSONfeature = JSONdataObj['features']
            cursor = da.InsertCursor(localTarget, cursorFields)
            j = 0
            for feature in myJSONfeature:
                # Get Attribute Field Value
                myJSONattr = myJSONfeature[j]['attributes']
                myJSONattrItems = myJSONattr.items()
                myJSONattrItems.sort()
                cursorValues = []
                for item in myJSONattrItems:
                    if item[0].upper() != 'OBJECTID':
                        if item[1] == None:
                            cursorValues.append(item[1])
                        else:
                            cursorValues.append(str(item[1]))
                # Get Geometry JSON
                myJSONgeometry = myJSONfeature[j]['geometry']
                # Construct JSON according to Geometry Type
                if geotype == 'POLYGON':
                    global geometryJsonStr
                    geometryJsonStr = (str({"rings": myJSONgeometry['rings']}))
                elif geotype == 'POINT':
                    # global geometryJsonStr
                    geometryJsonStr = (str({"x":myJSONgeometry['x'],"y":myJSONgeometry['y']}))
                elif geotype == 'POLYLINE':
                    # global geometryJsonStr
                    geometryJsonStr = (str({"paths": myJSONgeometry['paths']}))
                else:
                    arcpy.AddMessage("Unknown Geometry Type!")
                cursorValues.append(geometryJsonStr)
                cursor.insertRow(cursorValues)
                j = j+1
            arcpy.AddMessage(str(j)+' downloaded ...')
            del cursor


        if __name__ == "__main__":

            ServiceURL = parameters[0].valueAsText
            username = parameters[1].valueAsText
            passwords = parameters[2].valueAsText
            whereClauseField = parameters[3].valueAsText
            location = parameters[4].valueAsText

            ### Internal Parameters
            arcpy.env.workspace = location
            arcpy.env.overwriteOutput = True
            agsservername = ServiceURL.split('/')[2].split(':')[0]
            serverport = ServiceURL.split('/')[2].split(':')[1]
            servicename = ServiceURL.split('/')[-3]
            LayerIndex = ServiceURL.split('/')[-1]
            fcname = servicename+"_"+str(LayerIndex)
            arcpy.AddMessage('ArcGIS Server Name : {0} , Port : {1}.'.format(agsservername, serverport))
            arcpy.AddMessage('The layer <{1}> of the Service <{0}> will be downloaded soon.'.format(servicename, LayerIndex))

            ### Started Here
            # Clear Local Existing File ..
            if arcpy.Exists(fcname):
                arcpy.Delete_management(fcname)
            # Call GetToken Function
            myToken = GetToken(username, passwords, agsservername, serverport)
            arcpy.AddMessage('The token has been checked! ')
            # Creat Local Feature Class Skema
            cursorFields = CreateLocalFeatureClass(location, fcname)
            cursorFields.sort()
            cursorFields.append('SHAPE@JSON')
            arcpy.AddMessage("Local <{1}> Feature Class <{0}> has been created!".format(fcname,geotype))
            arcpy.AddMessage('Location : {0}'.format(location))
            # Write Local Feature Class
            maxOID = GetMaxOBJECTID()
            i = 0
            st = time.clock()
            maxRecordCount = GetmaxRecordCount()
            while i <= maxOID/maxRecordCount+1:
                whereClause = whereClauseField+">="+str(i*maxRecordCount)+" and "+whereClauseField+"<"+str((i+1)*maxRecordCount)
                myJSON = FeatureServiceJSON(servicename, whereClause)
                WriteLocalFC(myJSON, fcname, cursorFields)
                arcpy.AddMessage(whereClauseField+'('+str(i*maxRecordCount)+'-'+str((i+1)*maxRecordCount)+')'+'  Done !')
                i = i + 1
            et = time.clock()
            # Compare Service and Local File
            totalCountServer = GetCount(servicename)
            result = arcpy.GetCount_management(fcname)
            localCount = int(result.getOutput(0))
            arcpy.AddMessage("Service Total Data Count:"+str(totalCountServer))
            arcpy.AddMessage("Max OBJECTID:"+str(maxOID))
            arcpy.AddMessage("Actually Download:"+str(localCount))
            print   str((time.clock() - st)) + " Seconds..."

        return


