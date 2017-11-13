# -*- coding: utf-8 -*-
__author__ = 'kikita'

from site import addsitedir
from sys import executable
from os import path
interpreter = executable
sitepkg = path.dirname(interpreter) + "\\site-packages"
print(sitepkg)
addsitedir(sitepkg)

def main():
    import arcpy
    arcpy.env.workspace = r"D:\a.gdb"
    arcpy.env.overwriteOutput = True
    FeatureClasses = arcpy.ListFeatureClasses()
    OutCS = arcpy.SpatialReference(3857)
    print(OutCS)
    for FeatureClass in FeatureClasses:
        arcpy.Project_management(FeatureClass, "Prj_" + FeatureClass, OutCS)
        print(FeatureClass + ' has been projected ...')
    print('End Processing ...')

if __name__ == "__main__":
    print('Start Processing ...')
    main()
    raw_input("Enter enter key to exit...")
