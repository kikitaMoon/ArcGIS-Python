title: CityEngine与ArcGIS对栅格数据的要求情况
categories:
  - 木工开物
date: 2013-05-13 10:47:28
tags: [CityEngine,Raster]
---

在论坛上看到一篇很好的讲述如题主题的文章，很有价值，可以为CityEngine选择合适的栅格数据或者纹理，提供一些帮助，原文如下：

----------------------------------------------------------------------------------------------------------

**textures / raster files : concepts in CityEngine / ArcGIS**

Hi,

Quite a few new customers and people evaluating CityEngine who are working in the field of GIS ask about how CityEngine handles 'raster files' or 'basemaps' and what the best practices are concerning file resolutions.

Since CityEngine works ( from a technology-POV ) very similar as many other pure 3d applications (CityEngine is a 3d Modelling Application), I wanted to point out a few differences between CityEngine and ArcGIS :

**ArcGIS-users call bitmap files 'raster files' due to their grid-based nature. People usually working with 3d applications call them 'textures'. It's the same thing.**

ArcGIS has technologies embedded which 'dynamically' load only the part of a dataset which is currently visible on screen. Thus, with this technology HUGE raster datasets (> 1GB) can easily be displayed.
CityEngine does NOT have such a streaming service, thus raster files / textures should be prepared with some basic knowledge how they shall be used in a CityEngine project.



Important things to know :

1] Arc GIS' basemaps can not directly be loaded in CityEngine as a layer. The user must export the specific 'area of interest' (extent) as a texture to be used within CityEngine.
2] To be able to work with textures, all the textures must reside within the opened project, usually in the 'assets' folder general textures, respectively the 'maps' folder for map-/basemap - textures (or a subdirectory).
3] CityEngine is a 3d application which uses a technology called 'OpenGL' to display the 3d models (and the scene). Displaying 3d graphics this way uses the computer's graphics card . For this, all textures are fully loaded in thatgraphics card's memory. [Please note that the computer has 'main memory', which is usually called RAM. A graphics card has it's own RAM, often called 'Video RAM'. ]
4] Since the amount of memory on graphics cards is usually quite small (~ 256 MegaBytes - 1.5 GigaBytes), one can imagine that the resources should be handled carefully !
5] Please note that when importing raster files from ArcGIS (e.g. GeoTIF), the file's projection MUST MATCH the CityEngine scene's Scene Coordinate System. CityEngine can not (yet) reproject raster files when importing into the scene (as opposed to Shapes and Graph Segments !).

Since the amount of memory used per texture is directly linked to it's resolution (e.g. 500x500 pixels) plus the bit-depth of the file, we recommend to work with as efficient files as possible :

- use graphics card drivers which are UP TO DATE !
- use 8 bit textures whenever possible (except the terrain's 'heightmap' which usually just is 32 bit)
- use texture resolutions <= 1024 x 1024 px (does not need a square ratio)
- terrains may be higher in resolution, I'd say <= 2048 x 2048 px.
- higher resolution textures may be downsampled automatically by CityEngine ( for viewport display only ! ).
- if a texture has too large a resolution (e.g. 13'000 x 13'000 px), it will not be displayed at all.

----------------------------------------------------------------------------------------------


原文链接：

http://forums.arcgis.com/threads/54072-textures-raster-files-concepts-in-CityEngine-ArcGIS

