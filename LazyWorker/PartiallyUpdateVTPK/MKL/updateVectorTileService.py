# _*_ coding: utf-8 _*_
__author__ = 'ma_keling'
# !/usr/bin/python

import os
import sys
import zipfile
import shutil
import requests
import json
import paramiko
from smb.SMBConnection import *
import arcpy


def main(argv=None):

    update_cache_path = arcpy.GetParameterAsText(0)
    service_url = arcpy.GetParameterAsText(1)
    ags_username = arcpy.GetParameterAsText(2)
    ags_password = arcpy.GetParameterAsText(3)
    share_hostname=arcpy.GetParameterAsText(4)
    share_admin = arcpy.GetParameterAsText(5)
    share_password = arcpy.GetParameterAsText(6)

    # local part vtpk from windows system
    # update_cache_path = r'C:\makl\testdata\NewPart.vtpk'

    # for vector tile service from arcgis server 10.5 for windows
    # service_url = r'https://120win105.esrichina.com/server/rest/services/Hosted/china400W_vtpk/VectorTileServer'

    # for vector tile service from arcgis server 10.5 for linux
    # service_url = r"https://123linux106.esrichina.com:6443/arcgis/rest/services/Hosted/china400W_vtpk/VectorTileServer"

    # for arcgis server admin account
    # ags_username = 'arcgis'
    # ags_password = 'Super123'

    #  cache directory stored in windows file system
    # share_hostname = '192.168.220.120'
    # share_admin = "administrator"
    # share_password = "Super123"

    # cache directory stored in linux file system
    # share_hostname = '192.168.220.123'
    # share_admin = "arcgis"
    # share_password = "Super123"

    execute(update_cache_path, service_url, ags_username, ags_password, share_hostname,
            share_admin, share_password)
#common http tools
#assistant method for submit request
def submit_request(url,params,item=""):
    err_flag = 'failed'
    try:
        r = requests.post(url, data=params, verify=False)

        if (r.status_code != 200):
            r.raise_for_status()
            print('request failed.')
            return err_flag
        else:
            data = r.text
            elapse_time = str(r.elapsed.microseconds/1000/1000) + 's'
            # Check that data returned is not an error object
            if not assertJsonSuccess(data):
                return
            # Extract service list from data
            result = json.loads(data)

            if item != "":
                last_result = result[item]
            else:
                last_result = result
            return elapse_time,last_result
    except :
        print("request failed")
        return err_flag

# assert response json
def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        print('Error: JSON object returns an error.' + str(obj))
        sys.exit(False)
    else:
        return True

# connect_remote_linux_path(hostname, username, password, filepath, cache_path)
def connect_remote_linux_path(hostname, username, password, filepath, cache_path):
    try:
        ##连接远程主机
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, 22, username, password)

        sftp = client.open_sftp()

        file_list = os.listdir(filepath)
        print(filepath)
        for Level in file_list:
            lodPath = os.path.join(filepath, Level)
            bundles = os.listdir(lodPath)
            server_lod_path = cache_path + '/' + Level
            for bundle in bundles:
                local_bundle_path = lodPath + os.sep + bundle
                server_bundle_path = server_lod_path + '/' + bundle
                print("local:",local_bundle_path)
                print("server:",server_bundle_path)
                sftp.put(local_bundle_path, server_bundle_path)


        client.close()
        return True
    except:
        print("upload bundle failed!")
        return False

# connect_remote_win_path(hostname,username,password,filepath,cache_path)
def connect_remote_win_path(hostname,username,password,filepath,cache_path):
    localserver = "local"
    domain = ""
    service_name = ''

    try:
        if cache_path[:2] == r"\\":
            ll = cache_path.split('\\')
            service_name = ll[3]
            print("service_name")
            new_cache_path = ""
            for i in range(len(ll)):
                if i > 3:
                    new_cache_path += "/"+ ll[i]
            print("new_cache_path:",new_cache_path)

        else:
            service_name = cache_path[:1] + "$"
            ll = cache_path.split('\\')
            new_cache_path = ""
            for i in range(len(ll)):
                if i > 0:
                    new_cache_path += "/" + ll[i]
            print("new_cache_path:", new_cache_path)

        print("connecting server")
        conn = SMBConnection(username,password,localserver,hostname,domain=domain,
                      use_ntlm_v2=True,sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,is_direct_tcp=True)

        conn.connect(hostname, 445)

        response = conn.listShares(timeout=30)  # obtain a list of shares
        print('Shares on: ' + hostname)

        for i in range(len(response)):  # iterate through the list of shares
            print("  Share[", i, "] =", response[i].name)

        print("filepath:", filepath)

        try:

            file_list = os.listdir(filepath)

            for Level in file_list:
                lodPath = os.path.join(filepath, Level)
                bundles = os.listdir(lodPath)
                server_lod_path = new_cache_path + "/" + Level
                for bundle in bundles:
                    local_bundle_path = lodPath + os.sep + bundle
                    server_bundle_path = server_lod_path + "/" + bundle
                    print("local:",local_bundle_path)
                    # print("server:", server_bundle_path)
                    file_obj = open(local_bundle_path,'rb')

                    # service_name = response[2].name
                    print("service_name:",service_name)
                    conn.storeFile(service_name, server_bundle_path, file_obj, timeout=60)
                    print("uploaded:", server_bundle_path)
                    file_obj.close()


        # print("upload over")
            conn.close()
            return True
        except:
            print("upload failed! Maybe there is no any tiles in the dir: "+filepath)
            conn.close()
            return False
    except:
        conn.close()
        return False

# get token by arcgis server
def generateToken(url, username, password):
    tokenUrl = url + '/admin/generateToken'
    print(tokenUrl)
    # , 'ip':'192.168.100.85'
    params = {'username': username, 'password': password, 'client': 'requestip', 'f': 'json'}

    item = 'token'

    r = submit_request(tokenUrl, params, item)

    return r[1]

def get_cahces_list(url,token):
    directory_url = url + '/admin/system/directories'
    print('directory_url', directory_url)

    d_params = {'token': token, 'f': 'json'}

    result = submit_request(directory_url, d_params)

    directories = result[1]['directories']

    cache_dirs = []

    for dir in directories:
        if dir['directoryType'] == 'CACHE':
            print(dir)
            cache_dirs.append(dir['physicalPath'])
            print(dir['physicalPath'])

    return cache_dirs

def get_cache_dir(url,token,service,item):
    # https://120win105.esrichina.com:6443/arcgis/admin/services/Hosted/mytest5000.VectorTileServer
    directory_url = url + '/admin/services/Hosted/'+service+".VectorTileServer"
    print('directory_url', directory_url)

    d_params = {'token': token, 'f': 'json'}

    result = submit_request(directory_url, d_params)

    # print("cache_result",result[1])
    cache_dir = ""

    cache_dir_main = result[1]['properties']['cacheDir']
    if cache_dir_main.__contains__('\\'):
        cache_dir = cache_dir_main + '\\VectorCache\\Hosted\\'+ service + '\\VectorTileServer\\tile'
    else:
        cache_dir = cache_dir_main + '/VectorCache/Hosted/'+ service + '/VectorTileServer/tile'
    return cache_dir

# Defines the entry point into the script

def parse_service_url(service_url):
    node_list = str(service_url).split('/')
    print(node_list)
    if len(node_list[2].split(":")) > 1:
        server_url = node_list[0]+'//'+node_list[2]+'/'+node_list[3]
        service_name = node_list[7]
    else:
        server_url = node_list[0]+'//'+node_list[2]+':6443/arcgis'
        service_name = node_list[7]


    return service_name,server_url

# Change vtpk extension from .vtpk to .zip
def retype(newPartVtpkPath,newtype):
    try:
        filename = os.path.splitext(newPartVtpkPath)[0];  # file name
        filetype = os.path.splitext(newPartVtpkPath)[1];  # file type

        olddir = newPartVtpkPath
        newdir = filename + newtype

        os.rename(olddir, newdir)

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
        return ""

#zip and retype file
def zip_and_retype(original_extract_path,new_vtpk_name):
    try:
        prelen = len(original_extract_path)
        # print(prelen)
        # print("zip root folder: " + original_extract_path)

        zipDir = original_extract_path + ".zip"
        fp = zipfile.ZipFile(zipDir, mode='w')
        for parent, dirnames, filenames in os.walk(original_extract_path):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[prelen:].strip(os.path.sep)
                fp.write(pathfile, arcname, compress_type=zipfile.ZIP_STORED)
        fp.close()
        # print("zipDir:" + zipDir)
        olddir = retype(zipDir,".vtpk")
        newdir = os.path.join(os.path.dirname(olddir), new_vtpk_name)
        # print("new dir:", newdir)
        os.rename(olddir, newdir)
        return True
    except:
        print("path or folderName not exit.")

def delete_zip_folder(delete_path):
    shutil.rmtree(delete_path)

# upload bundles from local bundle files to OSS cache directories
def upload_bundles(filepath, cache_path, hostname, username, password):
    result = False

    if cache_path[:1] == '/':
        result = connect_remote_linux_path(hostname, username, password, filepath, cache_path)
    elif cache_path[:2] == '\\':
        hostname_w = cache_path.split('\\')[2]
        result = connect_remote_win_path(hostname_w.username, password, filepath, cache_path)
    else:
        result = connect_remote_win_path(hostname, username, password, filepath, cache_path)

    return result

# get unzip local .vtpk file and return local cache path
def get_local_cache_path(upate_vtpk_path):
    zip_path = retype(upate_vtpk_path,'.zip')
    print("zip path:", zip_path)
    unzip_path = unzip(zip_path)
    if unzip_path[:1] == r"/":
        cache_path = os.path.join(unzip_path,'p12/tile')
    else:
        cache_path = os.path.join(unzip_path, 'p12\\tile')

    return cache_path

# execute method for arcgis gp tool
def execute(update_vtpk_path,service_url,ags_username,ags_password,share_hostname,admin_username,admin_password):
    # arcpy.AddMessage('update starting...')

    update_vtpk_name = os.path.split(update_vtpk_path)[1]
    # arcpy.AddMessage('get update vtpk name: '+update_vtpk_name)
    print('get update vtpk name: '+update_vtpk_name)

    local_cache_path = get_local_cache_path(update_vtpk_path)
    # arcpy.AddMessage('get local part vector tile cache dir:'+local_cache_path)
    print('get local part vector tile cache dir:'+local_cache_path)

    service_name, server_url = parse_service_url(service_url)
    print("get service name : "+ service_name)
    print("get service url: " + server_url)

    token = generateToken(server_url, username=ags_username, password=ags_password)

    # arcpy.AddMessage('get service token: '+ token)
    print('get service token: ' + token)

    vt_path = get_cache_dir(server_url, token, service_name, 'cacheDir')

    # arcpy.AddMessage('get service tile cache dir: '+vt_path)
    print('get service tile cache dir: '+vt_path)

    # arcpy.AddMessage('uploading service tiles ...')
    print('uploading service tiles ...')

    if upload_bundles(local_cache_path, vt_path, share_hostname,admin_username,admin_password):
        # arcpy.AddMessage('upload cache successfully!')
        print('upload cache successfully!')
        unzip_path = update_vtpk_path.split(sep='.')[0]
        if zip_and_retype(unzip_path,update_vtpk_name):
            delete_zip_folder(unzip_path)
        # arcpy.AddMessage('All the update task finished!')
        print('All the update task finished!')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))


