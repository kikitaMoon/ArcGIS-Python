# _*_ coding: utf-8 _*_
__author__ = 'makl'
# !/usr/bin/python


import os
import sys
import zipfile
import arcpy
import oss2
import shutil

# Defines the entry point into the script
def main(argv=None):
    # input new part vtpk name
    newPartVtpkPath = arcpy.GetParameterAsText(0)

    # input update service name
    serviceName = arcpy.GetParameterAsText(1)

    # input oss access key id
    access_key_id = arcpy.GetParameterAsText(2)

    # input oss key password
    access_key_secret = arcpy.GetParameterAsText(3)

    # input bucket name
    bucket_name = arcpy.GetParameterAsText(4)

    # input endpoint
    endpoint = arcpy.GetParameterAsText(5)

    # testing parameters
    # newPartVtpkPath = "/Users/maklmac/Desktop/newPart.vtpk"
    # serviceName = 'makltest'
    # access_key_id = '***'
    # access_key_secret = '***'
    # bucket_name = 'zhoun'
    # endpoint = 'http://oss-cn-shanghai.aliyuncs.com'

    execute(newPartVtpkPath, serviceName, access_key_id, access_key_secret, bucket_name, endpoint)

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
    # verify parameters
    for param in (access_key_id, access_key_secret, bucket_name, endpoint):
        assert '<' not in param, '请设置参数：' + param

    # create Bucket object
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
def upload_bundle_In_OSS(filePath, bucketPath,access_key_id, access_key_secret, bucket_name,endpoint):

    bucket = connect_OSS(access_key_id, access_key_secret, bucket_name, endpoint)
    result = oss_upload_bundles(bucket, filePath, bucketPath)
    return result

# get bucket cache path for specific service name
def get_bucket_path(serviceName):
    bucket_path= 'agssitecache/VectorCache/Hosted/' + serviceName + '/VectorTileServer/tile'
    return bucket_path


def execute(newPartVtpkPath, serviceName, access_key_id, access_key_secret, bucket_name,endpoint):

    try:
        #get local vector tile cache path
        filepath = get_local_tile_path(newPartVtpkPath)

        #get oss bucket path
        bucket_path = get_bucket_path(serviceName)

        #upload local vector tile cache to oss bucket store
        result = upload_bundle_In_OSS(filepath,bucket_path,access_key_id, access_key_secret, bucket_name,endpoint)

        if result:
            #zip newPathVTPKPath
            zip_and_retype(newPartVtpkPath)
            #delect zip folder
            delete_zip_folder(newPartVtpkPath)
    except:
        print("execute failed!")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))



