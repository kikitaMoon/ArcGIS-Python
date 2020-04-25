# _*_ coding: utf-8 _*_
__author__ = 'makl'
# !/usr/bin/python


import os
import zipfile
import arcpy
import oss2
import shutil

# Change vtpk extension from .vtpk to .zip
def retype(newPartVtpkPath,newtype):
    try:
        filename = os.path.splitext(newPartVtpkPath)[0];  # file name
        filetype = os.path.splitext(newPartVtpkPath)[1];  # file type
        olddir = newPartVtpkPath
        newdir = filename + newtype
        os.rename(olddir, newdir)
        print("has changed:" + newdir)

        return newdir
    except:
        print("retype failed: please provide a validates path")

#uncompress the .zip file to folder
def unzip(newPartZipPath):
    try:
        file_zip = zipfile.ZipFile(newPartZipPath, 'r')
        for file in file_zip.namelist():
            # print "unziping..."
            extractFolder = os.path.splitext(newPartZipPath)[0]
            file_zip.extract(file, extractFolder)
        file_zip.close()
        os.remove(newPartZipPath)
        print("unzip succeed!")
        return extractFolder
    except:
        print("unzip failed, please provde a validates path")
        return False

def zip_and_retype(newPartZipPath):
    try:
        prelen = len(newPartZipPath)
        # print(prelen)
        print("zip root folder: " + newPartZipPath)

        zipDir = newPartZipPath + ".zip"
        fp = zipfile.ZipFile(zipDir, mode='w')
        for parent, dirnames, filenames in os.walk(newPartZipPath):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[prelen:].strip(os.path.sep)
                fp.write(pathfile, arcname, compress_type=zipfile.ZIP_STORED)
        fp.close()
        print("zipDir:" + zipDir)
        retype(zipDir,".vtpk")
        return True
    except:
        print("path or folderName not exit.")

def delete_zip_folder(newPartZipPath):
    shutil.rmtree(newPartZipPath)


# return the unzip local tile path include LODs
def get_local_tile_path(newPartVtpkPath):
    newPartZipPath = retype(newPartVtpkPath,".zip")
    extractFolder = unzip(newPartZipPath)
    # for mac path
    tilePath = extractFolder + '/p12/tile'
    # # for windows path
    # tilePath = os.path.join(extractFolder, 'p12\\tile')
    print("local new part tile path:", tilePath)
    return tilePath

# connect OSS by access_key_id, access_key_secrest, bucket_name, endpoint
def connect_OSS(access_key_id,access_key_secret,bucket_name,endpoint):
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', access_key_id)
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', access_key_secret)
    bucket_name = os.getenv('OSS_TEST_BUCKET', bucket_name)
    endpoint = os.getenv('OSS_TEST_ENDPOINT', endpoint)

    # 确认上面的参数都填写正确了
    for param in (access_key_id, access_key_secret, bucket_name, endpoint):
        assert '<' not in param, '请设置参数：' + param

    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    print("connect succeed: " + bucket_name)

    return bucket

# upload bundles from local bundle files to OSS cache directories
def oss_upload_bundles(bucket,filepath,bucket_path):
    file_list = os.listdir(filepath)
    for Level in file_list:
        lodPath = os.path.join(filepath,Level)
        bundles = os.listdir(lodPath)
        bucket_lod_path = os.path.join(bucket_path,Level)
        for bundle in bundles:
             local_bundle_path = os.path.join(lodPath,bundle)
             bucket_bundle_path = os.path.join(bucket_lod_path,bundle)
             result = bucket.put_object_from_file(bucket_bundle_path, local_bundle_path)
             print(local_bundle_path)
             print (bucket_bundle_path)
             print(result)
    return True

# execute method for OSS
def upload_bundle_In_OSS(filePath, bucketPath):
    access_key_id = '***'
    access_key_secret = '***'
    bucket_name = '***'
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'

    bucket = connect_OSS(access_key_id, access_key_secret, bucket_name, endpoint)
    result = oss_upload_bundles(bucket, filePath, bucketPath)
    return result


## Arcpy -- Create Partial VTPK in AOI
def create_partial_vtpk(newVtpkPath, indexPolygon, AOI, map, lodLevel):
    workspace = os.path.dirname(newVtpkPath)
    arcpy.env.workspace = workspace
    arcpy.AddMessage("current workspace: " + arcpy.env.workspace)
    _len = len(workspace)
    newVTPKName = os.path.splitext(newVtpkPath[_len:].strip(os.path.sep))[0]

    AOI_lyr = arcpy.MakeFeatureLayer_management(AOI, "AOI_lyr")
    IndexPolygon_lyr = arcpy.MakeFeatureLayer_management(indexPolygon, "IndexPolygon_lyr")
    arcpy.SelectLayerByLocation_management(IndexPolygon_lyr, 'intersect', AOI_lyr)
    arcpy.AddMessage(lodLevel)

    arcpy.SelectLayerByAttribute_management(IndexPolygon_lyr, 'SUBSET_SELECTION', str(' "LOD" > ' + lodLevel))
    arcpy.CopyFeatures_management(IndexPolygon_lyr, 'NewIndex.shp')
    arcpy.AddMessage('NewIndex')

    IndexPolygon_lyr.visible = False
    AOI_lyr.visible = False
    arcpy.management.CreateVectorTilePackage(map, newVTPKName, "ONLINE", None,
                                             "INDEXED", 295828763.795777, 564.248588, 'NewIndex.shp', None, None)
    arcpy.Delete_management('NewIndex.shp')

    return True

# get bucket cache path for specific service name
def get_bucket_path(serviceName):
    bucket_path= 'agssitecache/VectorCache/Hosted/' + serviceName + '/VectorTileServer/tile'
    return bucket_path

def execute(newPartVtpkPath, indexPolygon, AOI, map, lodLevel,bucket_path):
    try:
        result = create_partial_vtpk(newPartVtpkPath, indexPolygon, AOI, map, lodLevel)
        if result:
            filepath = get_local_tile_path(newPartVtpkPath)
            bucket_path = get_bucket_path(serviceName)
            result = upload_bundle_In_OSS(filepath,bucket_path)
            if result:
                zip_and_retype(newPartVtpkPath)
                delete_zip_folder(newPartVtpkPath)


# 输入当前打开工程中的map
map = arcpy.GetParameterAsText(0)
# 指定更新包路径
newParVtpkPath = arcpy.GetParameterAsText(1)
# 输入索引polygon
indexPolygon = arcpy.GetParameterAsText(2)
# 输入感兴趣区polygon
AOI = arcpy.GetParameterAsText(3)
# 输入更新的级别
lodLevel = arcpy.GetParameterAsText(4)
# 输入要更新的服务名
serviceName = arcpy.GetParameterAsText(5)


# serviceName = 'makltest'
# newPartVtpkPath = "/Users/maklmac/Desktop/newPart.vtpk"


