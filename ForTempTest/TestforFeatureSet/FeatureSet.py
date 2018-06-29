import arcpy

#
inPath = arcpy.GetParameterAsText(0)
outPath = arcpy.GetParameterAsText(1)

outSet = arcpy.FeatureSet(inPath)
arcpy.AddMessage(str(type(outSet)))
arcpy.SetParameter(1 ,outSet)
outSet.save(outPath)