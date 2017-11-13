#**********************************************************************
# Description:
#    Unzips the contents of a zip file into an existing folder.
# Arguments:
#  0 - Input zip file
#  1 - Input folder - path to existing folder that will contain 
#      the contents of the zip file. 
#**********************************************************************

# Import modules and create the geoprocessor
#
import sys, zipfile, arcpy, os, traceback
from os.path import isdir, join, normpath, split

# Function to unzipping the contents of the zip file
#
def unzip(path, zip):
    # If the output location does not yet exist, create it
    #
    if not isdir(path):
        os.makedirs(path)    

    for each in zip.namelist():
        arcpy.AddMessage("Extracting " + os.path.basename(each) + " ...")
        
        # Check to see if the item was written to the zip file with an
        # archive name that includes a parent directory. If it does, create
        # the parent folder in the output workspace and then write the file,
        # otherwise, just write the file to the workspace.
        #
        if not each.endswith('/'): 
            root, name = split(each)
            directory = normpath(join(path, root))
            if not isdir(directory):
                os.makedirs(directory)
            file(join(directory, name), 'wb').write(zip.read(each))

if __name__ == '__main__':
    try:
        # Get the tool parameter values
        #
        infile = arcpy.GetParameterAsText(0)
        outfol = arcpy.GetParameterAsText(1)

        # Create the zipfile handle for reading and unzip it
        #
        zip = zipfile.ZipFile(infile, 'r')
        unzip(outfol, zip)
        zip.close()


    except:
        # Return any Python specific errors and any error returned by the geoprocessor
        #
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + \
                str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        arcpy.AddError(pymsg)

        msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(msgs)