__author__ = 'kikita'

import os

def printfile(file, number=0):
#    afile.seek(0)
    for line in file:
        number = number+1
        if line.find(":") > 0:
            print number,
            (role, spoke) = line.split(':',1)
            print role,
            print "said:",
            print spoke,
        else:
            print number,
            print "Noting!!!!!!"



if os.path.exists('sketch.txt'):
    afile = open('sketch.txt')
    printfile(afile)
    print "AAA"+line
    afile.close()
else:
    print 'Error!'
