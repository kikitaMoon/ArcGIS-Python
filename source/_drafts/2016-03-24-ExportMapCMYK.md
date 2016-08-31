将地图导出成PDF、AI格式的色彩空间问题整理


# 背景知识

我们在使用 ArcGIS 制图的时候，桌面端产品通常默认采用的是 **RGB** 色彩空间（Red/Green/Blue Color Space），也就是我们常说红绿蓝三原色光，这也是目前最常用的一种色彩系统。

除了RGB之外还有其他的 [**色彩空间**](https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%96%93)，例如，常用于印刷的四色 [**CMYK**（Cyan/Magenta/Yellow/blacK）](https://zh.wikipedia.org/wiki/%E5%8D%B0%E5%88%B7%E5%9B%9B%E5%88%86%E8%89%B2%E6%A8%A1%E5%BC%8F)，用色相、饱和度、明度表示的 [**HSV**（Hue/Saturation/Value）](https://zh.wikipedia.org/wiki/HSL%E5%92%8CHSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)，还有传说更接近人类视觉的 [**Lab**（Lightness,a,b）](https://zh.wikipedia.org/wiki/Lab%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)等等。 如果感兴趣，还是老样子，点进每个关键字的 wiki 链接探探细节。


现在提到 ArcGIS 桌面产品，除了 ArcMap，就不自觉地会捎上新成员 ArcGIS Pro，看看它们对色彩空间的支持情况：

**ArcMap**, 三种 RGB，CMYK，HSV:

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ArcMapColor.png)

**ArcGIS Pro**，更多，增加了 HSL，Lab，GrayScale:

![](http://7xs3vz.com1.z0.glb.clouddn.com/MGKW_ArcGISProColor.png)


<br>

<br>


# 

ArcMap 能够为**矢量**符号定义CMKY色彩，




Procedure

Define the colors in CMYK and export the map to a CMYK document.

Open the properties for the symbol to change to CMYK. In some ArcMap dialog boxes, the application may present a quick selection color palette. In these cases, click the 'More Colors' button to access the full color selector. -show me- 

 If the color selector displays the RGB sliders, the color was previously defined as an RGB color. -show me-
Change the color to CMYK and access the CMYK color sliders by clicking on the triangle button and selecting 'CMYK sliders'. -show me-
Use the CMYK sliders or text boxes to define CMYK values.
Click OK to close the dialog box and store the CMYK colors in the symbol. 

 Since the color selector was in CMYK mode when OK was clicked, the color is now tagged as CMYK. When this symbol is exported to a vector graphics format with the exporter's Destination Colorspace set to 'CMYK', the CMYK numbers will be preserved in the output file.

Navigate to File > Export map.
Click the 'Save as type' drop-down list and select one of the following export formats: PDF, EPS, Illustrator, or SVG.
View the export options panel and select the Format tab. For the Destination Colorspace option, select CMYK. -show me-
Set other options as needed, and click Save to export the map. 

The output file is marked as a CMYK mode file. When viewed in other graphics applications like Adobe Illustrator, the CMYK values for vector symbols match the values defined in ArcMap. 


 CMYK output is supported with the following limitations: 

• ArcMap raster layers always render internally as RGB colors. This means that even when a raster is defined with the color selector in CMYK mode, it does not internally get marked as CMYK color, and the raster layers stores only the RGB equivalent. On export to a CMYK graphics file, the stored RGB information is converted from RGB back to CMYK, but the CMYK values do not match the user defined CMYK values selected during set up of the raster layer properties. 

• Vector layers with transparency render as raster. Thus, any transparent vector layer using CMYK colors are not preserved CMYK numbers during output to a CMYK export file. 

• Picture Marker symbols sourced from a vector EMF file always use the colors defined in the EMF. Since the EMF file format does not support CMYK colors, it is not possible to define EMF Picture Marker symbols as CMYK. Instead, use a Simple Marker Symbol or a Character Marker Symbol, and follow the procedure documented above to define the symbol colors in CMYK.