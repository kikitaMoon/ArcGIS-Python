title: CityEngine Web Viewer IIS 部署
categories:
- 木工开物
date: 2013-09-11 14:43:49
tags: [CityEngine,3D]
---

中文原文链接：

http://blog.csdn.net/arcgis_all/article/details/8363728

esri原文链接：

http://www.arcgis.com/home/item.html?id=38fede3935a440e49cf316dcae6aae47

<br>

重点提出来，方便配置：

（1）先找到 webviewer 文件夹，在CE工作空间下ce.lib 文件夹下；

（2）将 webviewer 文件夹丢到 wwwroot 文件夹下；

（3）计算机管理中，webviewer目录中，双击打开右边的窗口中选中MIME类型，添加类型，如下图：

<br>

- 参数项：

 - 文件扩展名： .3ws 
 - MIME类型：application/octet-stream



![](http://img.blog.csdn.net/20130911144024750?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)    


访问地址：http://localhost/webviewer/ceviewer_offline.html
