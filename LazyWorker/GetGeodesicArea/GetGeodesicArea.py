# -*- coding: utf-8 -*-
__author__ = 'kikita'


import arcpy

inFC = arcpy.GetParameterAsText(0)
geodesicAreaField = arcpy.GetParameterAsText(1)
# units = arcpy.GetParameterAsText(2)


# inFC = 'D:\IncidentSupport2015\AllforTest\ArGISTutorTest\AT_America\America.gdb\USA_states1'
# geodesicAreaField = 'GeodesicArea'
units = 'SQUAREMETERS'


arcpy.AddField_management(inFC, geodesicAreaField, 'DOUBLE')

with arcpy.da.UpdateCursor(inFC, ['SHAPE@', geodesicAreaField]) as cursor:
    for fc in cursor:
        fc[1] = fc[0].getArea('GEODESIC', units)
        cursor.updateRow(fc)

