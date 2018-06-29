import arcpy

# Create token for portal 此处好像获取不到，我们这里直接请求
token = arcpy.GetSigninToken()
if token is not None:
	print(token['token'])
tokenstr=token['token']

#print('********************获取token 开始**************************')
#import urllib,ssl,json
# 取消ssl 验证
#ssl._create_default_https_context = ssl._create_unverified_context
#textmod = urllib.parse.urlencode({'username' : 'arcgis','password' : 'arcgis123','client' : 'referer','referer': 'https://instance.esri.com/arcgis','expiration': 60,'f' : 'json'}).encode(encoding='UTF8')
#print(textmod)
#输出内容:{'username' : 'arcgis','password' : 'arcgis123','client' : 'referer','referer': 'https://instance.esri.com/arcgis','expiration': 60,'f' : 'json'}
#ssl._create_default_https_context = ssl._create_unverified_context
#f = urllib.request.urlopen('https://instance.esri.com/arcgis/sharing/rest/generateToken',textmod)

#type(aa) byte
#aa = f.read()
# type(bb) str
#bb = aa.decode()

# type (cc) dict
#cc =json.loads(bb)
#tokenstr = cc['token']
#print('********************获取token 结束**************************')

print('********************开始 intersect 分析**************************')
# Create an empty FeatureSet object
#
xzq = arcpy.GetParameterAsText(1)
dltb = arcpy.GetParameterAsText(0)
output_name = arcpy.GetParameterAsText(2)

featSetStr2 = '%s?token=%s' %(xzq,tokenstr)
featSetStr = '%s?token=%s' %(dltb,tokenstr)
print('********************开始获取feature图层信息**************************')
print('DLTB地址:'+featSetStr)
print(featSetStr2)
featSet2 = arcpy.FeatureSet(featSetStr2)
featSet = arcpy.FeatureSet(featSetStr)
print('********************结束获取feature图层信息**************************')

arcpy.Intersect_analysis ([featSet,featSet2], output_name, "ALL", "", "")

print('********************结束 intersect 分析**************************')
