import arcpy
import pythonaddins

class ZoomtoSelectedFeatures(object):
    """Implementation for PythonProject_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    # Implementation of OnClick method of Button's class
    def onClick(self):

        # Get the current map document and the first data frame.
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd)[0]

        # Call the zoomToSelectedFeatures() method of the data frame class
        df.zoomToSelectedFeatures()