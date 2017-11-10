__author__ = 'kikita'

# FileName: EasyFeathering.py

import os
import arcpy

'''
#arcpy.env.workspace = "D:\IncidentSupport2015\something\Data.gdb"

# Get the value of the input parameters
InputFeature = arcpy.GetParameterAsText(0)
OutputFeature = "OutFeathering"
SingleRingWidth = 10000
'''

# Get the input values from tool UI
InputFeature = arcpy.GetParameterAsText(0)
SingleRingWidth = arcpy.GetParameterAsText(1)
OutputFeature = arcpy.GetParameterAsText(2)


# Some Predefined Parameters
distances = []
level = 9
bufferUnit = "meters"
NewField = "Percent"


# My Easy Feathering function
for i in range(level):
    distances.append(int(SingleRingWidth)*(i+1))
    i = i+1
arcpy.AddMessage("Step1 Distance list Complete!")


arcpy.MultipleRingBuffer_analysis(InputFeature, OutputFeature, distances, bufferUnit, "", "ALL","OUTSIDE_ONLY")
arcpy.AddMessage("Step2 Success to execute Multi Ring Buffer.")

arcpy.AddField_management(OutputFeature,NewField,"double")
arcpy.AddMessage("Step3 Success to add Transparency Percent Field.")

arcpy.CalculateField_management(OutputFeature, NewField, "!OBJECTID! *10", "PYTHON", "")

OutputFeatureCount = int(arcpy.GetCount_management(OutputFeature).getOutput(0))

if OutputFeatureCount == 0:
    arcpy.AddWarning("{0} has no features.".format(OutputFeature))
else:
    arcpy.AddMessage("Step4 Success to Calculate Transparency Percent Field.")



# Layer files are located in same folder as the .py file
PythonFilePath = os.path.dirname(__file__)

params = arcpy.GetParameterInfo()
params[2].symbology = os.path.join(PythonFilePath, "FeatheringEffectTemplate.lyr")

arcpy.AddMessage("Finding Feathering Effect Template Layer ..." +"/r/n"+ os.path.join(PythonFilePath, "FeatheringEffectTemplate.lyr"))
arcpy.AddMessage("Success!")



