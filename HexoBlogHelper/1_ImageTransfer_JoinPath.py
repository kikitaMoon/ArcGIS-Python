# -*- coding: utf-8 -*-
__author__ = 'Xiaoyan Mu'

import os

findpath = r"D:\HexokikitaMap\HexoBlogSync\source\images\blogImg"
wildcard = "ExplorerData"
blogpath = r"http://kikitamap.com/images/blogImg/"

def GetFileList(FindPath, Wildcard):
    FileList=[]
    FileNames=os.listdir(FindPath)
    for fn in FileNames:
        if fn.startswith(wildcard):
          print(blogpath+fn)


if __name__ == '__main__':
    GetFileList(findpath, wildcard)