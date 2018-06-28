#-*-coding:utf-8 -*-
__author__ = 'kikita'

import struct

dbf = r"C:\Users\kikita\Desktop\20180413数管乱码问题\20180413数管乱码问题\乱码数据\410403TDGHDL.dbf"
dat = open(dbf, 'rb').read(30)[29:]
id = struct.unpack('B', dat)[0]
print(struct.unpack('B', dat))
print(id, hex(id), bin(id), bin(77), type(id))


# WriteFileData = open(dbf, 'wb')
# WriteFileData.seek(30)
# WriteFileData.write(bin(77))
# WriteFileData.close()

# #import shapefile
# ID = struct.unpack('B', dat)[0]
# print(ID, hex(ID))

