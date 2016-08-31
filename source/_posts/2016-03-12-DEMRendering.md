title: DEM渲染洼地淹没图
categories:
- 木工开物
date: 2014-01-23 11:13:31
tags: [3D]
---

首先要准备基础数据，一张DEM栅格图。

![](http://img.blog.csdn.net/20140123105822359?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)





然后将掩膜水位以下的数据提取出来以备后用。这里我提取了高程1000以下的像元。

![](http://img.blog.csdn.net/20140123110128421?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)







对这个图层设置分类渲染，并设置半透明：

![](http://img.blog.csdn.net/20140123110412593?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



效果：

![](http://img.blog.csdn.net/20140123110500531?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)







生成DEM山影图，使用空间分析工具箱中的 Hillshade

![](http://img.blog.csdn.net/20140123110603953?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)







叠在一起就很漂亮了，可以表示，某个高度下水淹没的情况。





![](http://img.blog.csdn.net/20140123110810046?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)







3D效果：

![](http://img.blog.csdn.net/20140123111252968?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)





