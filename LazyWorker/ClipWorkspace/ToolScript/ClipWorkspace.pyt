'''
Source Name:   ClipWorkspace.pyt
Author:        Kikita
Description:   Python tool to clip spatial data in the same workspace by batch.
'''

import arcpy
import os

import ConversionUtils as CU


# The class name must be "Toolbox" ...
class Toolbox(object):

    def __init__(self):

        self.label = "Clip Workspace Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [ClipWorkspace]



class ClipWorkspace(object):

    def __init__(self):
        self.label = "Clip Workspace"
        self.description = "clip spatial data in the same workspace by batch."
        self.canRunInBackground = True

    def getParameterInfo(self):

        # Parameter Definitions
        # First parameter - Input Workspace
        param0 = arcpy.Parameter(
            displayName="Input Workspace",
            name="inWorkspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        # Second parameter - Clip Area
        param1 = arcpy.Parameter(
            displayName="Clip Area",
            name="CLipArea",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input")

        # Third parameter - Output Workspace
        param2 = arcpy.Parameter(
            displayName="Output Workspace",
            name="outWorkspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        params = [param0,param1,param2]
        return params


    def execute(self, parameters, messages):

        """The source code of the tool."""

        # Get tool parameters
        inWorkspace = parameters[0].valueAsText
        arcpy.AddMessage("###Input Workspace is {0}".format(inWorkspace))

        ClipArea = parameters[1].valueAsText
        arcpy.AddMessage("###Clip Area is {0}".format(ClipArea))

        outWorkspace =  parameters[2].valueAsText
        arcpy.AddMessage("###Out Workspace is {0}".format(outWorkspace))


        # Clip Feature by Batch
        arcpy.env.workspace = inWorkspace

        # Clip Vector
        FeatureClasses = arcpy.ListFeatureClasses()
        arcpy.AddMessage("Input Workspace contains {0}".format(FeatureClasses))
        for fc in FeatureClasses:
            arcpy.AddMessage(">> Clipping  {0}".format(fc))
            arcpy.Clip_analysis(fc,ClipArea, os.path.join(outWorkspace,fc))
            arcpy.AddMessage("{0} has been clipped.".format(os.path.join(outWorkspace,fc)))

        # Clip Raster
        Rasters = arcpy.ListRasters()
        arcpy.AddMessage("Input Workspace contains {0}".format(Rasters))
        for Raster in Rasters:
            arcpy.AddMessage(">> Clipping  {0}".format(Raster))
            arcpy.Clip_management(in_raster = Raster,
                                  rectangle = "",
                                  out_raster = os.path.join(outWorkspace,Raster),
                                  in_template_dataset = ClipArea,
                                  nodata_value = "",
                                  clipping_geometry = "ClippingGeometry",
                                  maintain_clipping_extent = "NO_MAINTAIN_EXTENT")
            arcpy.AddMessage("{0} has been clipped.".format(os.path.join(outWorkspace,Raster)))



        return



