__author__ = 'kikita'

import os

try:
    afile = open('sketch.txt')

    for line in afile:

        try:
            (role, spoke) = line.split(':', 1)
            print role,
            print "said:",
            print spoke,
        except ValueError:
            print "^^^  Oh!NO~O~ Error! Take care if the content of the file ! "

    afile.close()

except IOError:
    print "There is not such a file !"
