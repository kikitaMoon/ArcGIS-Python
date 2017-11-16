# -*- coding: utf-8 -*-
__author__ = 'kikita'



import os
import zipfile
import arcpy

def createpartialvtpk(originvtpkpath, indexPolygon, AOI, map):
    arcpy.AddMessage(originvtpkpath)
    workspace = os.path.dirname(originvtpkpath)
    arcpy.AddMessage(workspace)
    arcpy.env.workspace = workspace
    AOI_lyr = arcpy.MakeFeatureLayer_management(AOI, "AOI_lyr")
    IndexPolygon_lyr = arcpy.MakeFeatureLayer_management(indexPolygon, "IndexPolygon_lyr")

    arcpy.SelectLayerByLocation_management(IndexPolygon_lyr, 'intersect', AOI_lyr)

    arcpy.CopyFeatures_management(IndexPolygon_lyr, 'testCopyfeature')

    IndexPolygon_lyr.visible = False
    AOI_lyr.visible = False
    arcpy.management.CreateVectorTilePackage(map, "newPart.vtpk", "ONLINE", None,
                                             "INDEXED", 295828763.795777, 564.248588, IndexPolygon_lyr, None, None)

def retype(path=None, oldtype=None, newtype=None):
    try:
        file_list = os.listdir(path)  # list all the files in this path

        for files in file_list:
            olddir = os.path.join(path, files);
            if os.path.isdir(files):
                continue;
            filename = os.path.splitext(files)[0];  # file name
            filetype = os.path.splitext(files)[1];  # file type
            print('filename:' + filename)
            print('filetype:' + filetype)
            if filetype == oldtype:
                newdir = os.path.join(path, filename + newtype);
                os.rename(olddir, newdir);
                print("has changed:" + newdir)
        return True
    except:
        print("retype failed: please provide a validates path")


def renameziptovtpk(file=None):
    try:
        filename = os.path.splitext(file)[0];  # file name
        filetype = os.path.splitext(file)[1];  # file type
        if filetype == ".zip":
            newdir = filename + ".vtpk"
            os.rename(file, newdir)
            print("update vtpk is :" + newdir)

    except:
        print("file not exit!")
        return False


def unzip(path=None):
    try:
        file_list = os.listdir(path)
        for file_name in file_list:
            if os.path.splitext(file_name)[1] == ".zip":
                fullName = os.path.join(path, file_name)
                print(fullName)
                file_zip = zipfile.ZipFile(fullName, 'r')
                for file in file_zip.namelist():
                    # print "unziping..."
                    extractFolder = os.path.splitext(fullName)[0]
                    file_zip.extract(file, extractFolder)
                file_zip.close()
                os.remove(fullName)
        print("unzip succeed!")
        return True
    except:
        print("unzip failed, please provde a validates path")
        return False


def getvectortilespath(path=None, vtpkName=None):
    vtpkpath = os.path.join(path, vtpkName)
    tilepath = os.path.join(vtpkpath, 'p12\\tile')
    print("tilepath: " + tilepath)
    return tilepath


def copyFiles(oldvtpath=None, newvtpath=None):
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
                copyFiles(targetF, sourceF)

        print("Copy Succeed!")
        return True
    except:
        print("input vector tile path not exit")
        return False


def zip(path=None, folderName=None):
    try:
        rootDir = os.path.join(path, folderName)
        # prelen = len(os.path.dirname(rootDir))+9
        prelen = len(rootDir)
        # print(prelen)
        print("zip root folder: " + rootDir)

        zipDir = os.path.join(path, folderName) + ".zip"

        fp = zipfile.ZipFile(zipDir, mode='w')

        for parent, dirnames, filenames in os.walk(rootDir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                # arcname = pathfile[prelen:].strip(os.path.sep)   #相对路径
                arcname = pathfile[prelen:].strip(os.path.sep)

                print(arcname)
                fp.write(pathfile, arcname, compress_type=zipfile.ZIP_STORED)
                # fp.write(pathfile, filename,compress_type=zipfile.ZIP_STORED)
        fp.close()
        print("zipDir:" + zipDir)
        print("zip succed!")
        return zipDir
    except:
        print("path or folderName not exit.")


def mkworkspace(path=None, oldVTPKName=None, newVTPKName=None):
    try:
        workspace = os.path.join(path, "workspace")
        os.mkdir(workspace)
        print(workspace)
        sourceOldfile = os.path.join(path, oldVTPKName) + ".vtpk"
        sourceNewfile = os.path.join(path, newVTPKName) + ".vtpk"

        oldVTPKfile = os.path.join(workspace, oldVTPKName) + ".vtpk"
        newVTPKfile = os.path.join(workspace, newVTPKName) + ".vtpk"
        open(oldVTPKfile, "wb").write(open(sourceOldfile, "rb").read())
        open(newVTPKfile, "wb").write(open(sourceNewfile, "rb").read())
        print("make workspace dir succeed!")
        return workspace
    except:
        print("make workspace folder failed: please provide validate path!")
        return False


def executeupdate(wokspace=None, oldVTPKName=None, newVTPKName=None):

    retyperesult = retype(wokspace, ".vtpk", ".zip")
    if retyperesult:
        unzipresult = unzip(wokspace)
        if unzipresult:
            oldVTPath = getvectortilespath(wokspace, oldVTPKName)
            newVTPath = getvectortilespath(wokspace, newVTPKName)
            copyresult = copyFiles(oldVTPath, newVTPath)
            if copyresult:
                newzipfile = zip(wokspace, oldVTPKName)
                renameziptovtpk(newzipfile)


## Add -- Create Partial VTPK in AOI
def createpartialvtpk(workspace, indexPolygon, AOI, map):
    arcpy.env.workspace = workspace
    AOI_lyr = arcpy.MakeFeatureLayer_management(AOI, "AOI_lyr")
    IndexPolygon_lyr = arcpy.MakeFeatureLayer_management(indexPolygon, "IndexPolygon_lyr")

    arcpy.SelectLayerByLocation_management(IndexPolygon_lyr, 'intersect', AOI_lyr)

    arcpy.CopyFeatures_management(IndexPolygon_lyr, 'testCopyfeature')

    IndexPolygon_lyr.visible = False
    AOI_lyr.visible = False
    arcpy.management.CreateVectorTilePackage(map, "newPart.vtpk", "ONLINE", None,
                                             "INDEXED", 295828763.795777, 564.248588, IndexPolygon_lyr, None, None)
    return True

map = arcpy.GetParameterAsText(0)
originvtpkpath = arcpy.GetParameterAsText(1)
indexPolygon = arcpy.GetParameterAsText(2)
AOI = arcpy.GetParameterAsText(3)


path = r"D:\updateVT"
oldVTPKName = "vallnew"
newVTPKName = "part"
workspace = mkworkspace(path, oldVTPKName, newVTPKName)
CreatePartialVTPK(workspace,)
executeupdate(workspace, oldVTPKName, newVTPKName)

createpartialvtpk(originvtpkpath, indexPolygon, AOI, map)

def execute(originvtpkpath, indexPolygon, AOI, map):
    arcpy.AddMessage("original vtpk path ;" +  riginvtpkpath)
    workspace = os.path.dirname(originvtpkpath)
    arcpy.AddMessage("get original work space ;" + workspace)
    originalVTPKName = originvtpkpath[len(workspace):].split(os.path.sep)[0]
    if createpartialvtpk(workspace, indexPolygon, AOI, map):



