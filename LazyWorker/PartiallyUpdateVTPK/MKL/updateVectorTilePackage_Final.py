﻿# _*_ coding: Unicode _*_
__author__ = 'ma_keling'
# !/usr/bin/python


import os
import zipfile
# import arcpy
import shutil
import sys


# Defines the entry point into the script
def main(argv=None):
    # original_vtpk_path = arcpy.GetParameterAsText(0)
    # update_vtpk_path = arcpy.GetParameterAsText(1)
    # new_vtpk_path = arcpy.GetParameterAsText(2)

    original_vtpk_path = r'D:\updateVT\workspace\china_100index.vtpk'
    update_vtpk_path = r'D:\updateVT\workspace\newPart.vtpk'
    new_vtpk_path = r'D:\updateVT\workspace\workspace\china_100index_new.vtpk'

    execute(new_vtpk_path, original_vtpk_path, update_vtpk_path)


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
        return ""

def zip_and_retype(original_extract_path,new_vtpk_name):
    try:
        prelen = len(original_extract_path)
        # print(prelen)
        print("zip root folder: " + original_extract_path)

        zipDir = original_extract_path + ".zip"
        fp = zipfile.ZipFile(zipDir, mode='w')
        for parent, dirnames, filenames in os.walk(original_extract_path):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[prelen:].strip(os.path.sep)
                fp.write(pathfile, arcname, compress_type=zipfile.ZIP_STORED)
        fp.close()
        print("zipDir:" + zipDir)
        olddir = retype(zipDir,".vtpk")
        newdir = os.path.join(os.path.dirname(olddir), new_vtpk_name)
        print("new dir:", newdir)
        os.rename(olddir, newdir)
        return True
    except:
        print("path or folderName not exit.")

def delete_zip_folder(delete_path):
    shutil.rmtree(delete_path)

def copy_files(oldvtpath=None, newvtpath=None):
    try:
        sourceDir = newvtpath
        targetDir = oldvtpath

        for f in os.listdir(sourceDir):
            sourceF = os.path.join(sourceDir, f)
            targetF = os.path.join(targetDir, f)

            if os.path.isfile(sourceF):
                if os.path.exists(targetF):
                    open(targetF, "wb").write(open(sourceF, "rb").read())
                    print("copy :" + targetF)
            elif os.path.isdir(sourceF):
                if not os.path.exists(targetDir):
                    os.mkdirs(targetDir)
                copy_files(targetF, sourceF)

        print("Copy Succeed!")
        return True
    except:
        print("input vector tile path not exit")
        return False

# return the unzip local tile path include LODs
def get_tile_path(extract_folder):
    # # for windows path
    tilePath = os.path.join(extract_folder, 'p12\\tile')
    print("local new part tile path:", tilePath)
    return tilePath


def make_workspace(workspace,original_vtpk_path,update_vtpk_path):
    original_vtpk_name = os.path.split(original_vtpk_path)[1]
    update_vtpk_name = os.path.split(update_vtpk_path)[1]
    original_vtpk_new_path = os.path.join(workspace,original_vtpk_name)
    update_vtpk_new_path = os.path.join(workspace,update_vtpk_name)
    open(original_vtpk_new_path,'wb').write(open(original_vtpk_path,'rb').read())
    open(update_vtpk_new_path,'wb').write(open(update_vtpk_path,'rb').read())
    print("new workspace created succeed!",workspace,original_vtpk_new_path,update_vtpk_new_path)
    return True
    # try:
    #
    # except:
    #     print("create new workspace failed!")


def execute(new_vtpk_path,original_vtpk_path,update_vtpk_path):
    workspace = os.path.dirname(new_vtpk_path)
    original_vtpk_name = os.path.split(original_vtpk_path)[1]
    update_vtpk_name = os.path.split(update_vtpk_path)[1]
    new_vtpk_name = os.path.split(new_vtpk_path)[1]
    # arcpy.AddMessage("creating workspace:" + workspace)
    result = make_workspace(workspace,original_vtpk_path, update_vtpk_path)
    # arcpy.AddMessage("current workspace:" + workspace)
    if result:
        original_vtpk_new_path = os.path.join(workspace,original_vtpk_name)
        update_vtpk_new_path = os.path.join(workspace,update_vtpk_name)
        original_zip_path = retype(original_vtpk_new_path,".zip")
        update_zip_path = retype(update_vtpk_new_path,".zip")
        # arcpy.AddMessage("retype the extension from .vtpk to .zip")
        print("original_zip_path:", original_zip_path)
        print("update_zip_path:", update_zip_path)
        original_unzip_path = unzip(original_zip_path)
        update_unzip_path = unzip(update_zip_path)
        # arcpy.AddMessage("uncompress the zip files")
        print("original_unzip_path:" ,original_unzip_path)
        print("update_unzip_path:" ,update_unzip_path)
        original_tiles = get_tile_path(original_unzip_path)
        new_tiles = get_tile_path(update_unzip_path)
        # arcpy.AddMessage("get the tiles path for update")
        print("original_tiles", original_tiles)
        print("new_tiles",new_tiles)
        # arcpy.AddMessage("updating.......")
        copy_files(original_tiles,new_tiles)
        if zip_and_retype(original_unzip_path,new_vtpk_name):
            delete_zip_folder(original_unzip_path)
            delete_zip_folder(update_unzip_path)
        # arcpy.AddMessage("update successfully!")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

