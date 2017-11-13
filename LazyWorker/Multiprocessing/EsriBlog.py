__author__ = 'kikit'

import os
import re
import multiprocessing
import arcpy

def update_shapefiles(shapefile):
    '''Worker function'''

    # Define the projection to wgs84 -- factory code is 4326.
    # arcpy.management.DefineProjection(shapefile, 4326)

    # Add a field named CITY of type TEXT.
    arcpy.management.AddField(shapefile, 'CITY', 'TEXT')

    # Calculate field 'CITY' stripping '_base' from
    # the shapefile name.
    city_name = shapefile.split('_base')[0]
    city_name = re.sub('_', ' ', city_name)
    arcpy.management.CalculateField(shapefile, 'CITY',
                    '"{0}"'.format(city_name.upper()), 'PYTHON')

# End update_shapefiles
def main():
    ''' Create a pool class and run the jobs.'''
    # The number of jobs is equal to the number of shapefiles
    workspace = r'D:\IncidentSupport2015\AllforTest\ArGISTutorTest\AT_Digitizing'
    arcpy.env.workspace = workspace
    fcs = arcpy.ListFeatureClasses('*')
    fc_list = [os.path.join(workspace, fc) for fc in fcs]
    pool = multiprocessing.Pool()
    pool.map(update_shapefiles, fc_list)

    # Synchronize the main process with the job processes to
    # ensure proper cleanup.
    pool.close()
    pool.join()
    # End main

if __name__ == '__main__':
    main()