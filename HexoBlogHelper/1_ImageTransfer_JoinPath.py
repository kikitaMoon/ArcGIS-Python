# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import os

# Specify the wildcars
wildcard = "CompactCache"

# Static Information
findpath = r"D:\HexokikitaMap\HexoBlogSync\source\images\blogImg"
blogpath = r"http://kikitamap.com/images/blogImg/"

def GetFileList(FindPath, Wildcard):
    FileList=[]
    FileNames=os.listdir(FindPath)
    for fn in FileNames:
        #if fn.startswith(wildcard):
        if wildcard in fn:
          print(blogpath+fn)



if __name__ == '__main__':
    GetFileList(findpath, wildcard)