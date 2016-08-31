title: CityEngine支持多少种栅格数据？
categories:
- 木工开物
date: 2014-01-06 11:11:29
tags: [3D,CityEngine]
---
<span style="font-size:12px">&nbsp; &nbsp; 许多用户会问 CityEinge 到底支持多少种栅格数据作为底图数据？</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">&nbsp; &nbsp; CityEngine目前的帮助文档略显单薄，作为工具书查看是很好的，但是作为知识类资料就不如ArcGIS Desktop的帮助文档完整饱满。</span><span style="font-size:12px">因此像“栅格数据支持列表”这种归纳性的文档当然现在还是没有……</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">&nbsp; &nbsp; 只能从软件界面自身去寻找了，就把这页贴出来，方便大家参考。从以下这个长长的下列表中可以了解CityEngine支持的类型：</span>

<span style="font-size:12px">（png，jpg，tif，jpeg，img，data，ico，xpm，dds，tga，psp，tiff，vbs，sid，mpeg，jsl，xbm，sit，bmp，mpg，dat，com，hqx，cur，dll，bin，emf，exe，gif，xyz，sgi）</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">![](http://img.blog.csdn.net/20140106100109203?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">&nbsp; &nbsp;CityEngine在显示栅格数据时，对数据有一定的要求，不满足要求时可能会出现不显示等情况。</span>

<span style="font-size:12px">&nbsp; &nbsp;CityEngine使用了OpenGL技术用于3D模型/场景的显示，当显示模型的时候，会将所有的texture数据输入到显存（不是内存哦！）显存的大小在机器中通常是不大的（256M~1.5G，或者更大一点吧），因此CE对输入的栅格数据是要求的。</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">&nbsp; &nbsp; 为了获取最佳的效果，如下几点要注意哦~</span>

<span style="font-size:12px">（1）显卡驱动一定要安装至最新版本！</span>

<span style="font-size:12px">（2）Texture图层尽量选择 8-bit 的，terrain 图层中的Heightmap也可以是32-bit的。</span>

<span style="font-size:12px">（3）栅格数据的行列数会影响显示，过多的行列数会导致显示失败，这个具体的数目与硬件也是相关的。通常如果发现不能正常显示时，可以考虑通过ArcGIS Desktop 中的重采样将数据的降低分辨率。</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">附上esri美国论坛上工程师发的一个帖子：</span>

<span style="font-size:12px">[http://forums.arcgis.com/threads/54072-textures-raster-files-concepts-in-CityEngine-ArcGIS](http://forums.arcgis.com/threads/54072-textures-raster-files-concepts-in-CityEngine-ArcGIS)

</span>

<span style="font-size:12px">

</span>

<span style="font-size:12px">以及，添加 Terrain 图层的帮助文档：</span>

[<span style="font-size:12px">http://cehelp.esri.com/help/index.jsp</span>](http://cehelp.esri.com/help/index.jsp)