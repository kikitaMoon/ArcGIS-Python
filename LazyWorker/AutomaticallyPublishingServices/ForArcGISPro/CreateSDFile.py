import arcpy
from arcpy import env

import os
import os.path
# from multiprocessing import Pool

sdFolder = r'\\192.168.220.162\TestData\MyProject1'
sdName = r'\\192.168.220.162\TestData\MyProject1'
fc = r'\\192.168.220.162\TestData\My_data3DUIM_1.gdb'
projectFile = r'\\192.168.220.162\TestData\MyProject1\MyProject1.aprx'

def multiPatch2ServerDefinition(dsFolder,mpName):
    # Change scene and layer as yours ...
    SceneName = 'MyScene'
    LayerName = '3dlayer'
    # Find the Scene
    aprx = arcpy.mp.ArcGISProject(projectFile)
    m = aprx.listMaps(SceneName)[0]
    print(m.name)
    print(m.mapType)
    # Change data source of the existing layer
    for lyr in m.listLayers(LayerName):
        print(lyr.connectionProperties)
        conProp = lyr.connectionProperties
        print(conProp['connection_info']['database'])
        conProp['connection_info']['database'] = dsFolder
        print(conProp['dataset'])
        conProp['dataset'] = mpName
        lyr.connectionProperties = conProp
    aprx.save()   
    print('add layer to Project : ' + mpName)

    sddraftFile = os.path.join(sdFolder, mpName.__str__() + '_ArcPy162' + '.sddraft')
    sdFile = os.path.join(sdFolder, mpName.__str__() + '_ArcPy162' + '.sd')

    #### Publish Feature Service
    arcpy.mp.CreateWebLayerSDDraft(m, sddraftFile, mpName, 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS')
    print('make SDDraft file : ' + sddraftFile)
    result = arcpy.StageService_server(sddraftFile, sdFile)
    print('make SD file : ' + sdFile)

    # #### GP Service
    # arcpy.CreateGPSDDraft(result, os.path.join(sdFolder, "GPoutput2.sddraft"), "myGPservice22")
    # print("GP Draft Done!")
    # arcpy.StageService_server(os.path.join(sdFolder, "GPoutput2.sddraft"), os.path.join(sdFolder, "GPoutput22.sd") )
    # print("GP SD Done!")
    # # Fialed
    # # arcpy.UploadServiceDefinition_server(os.path.join(sdFolder, "GPoutput22.sd"), 'My Hosted Services')
    # # print('aaa')


if __name__ == '__main__':
    env.workspace = fc
    # multiPatch2ServerDefinition(fc, 'Building1Shells')
    multiPatch2ServerDefinition(fc, 'NewBuilding2')
