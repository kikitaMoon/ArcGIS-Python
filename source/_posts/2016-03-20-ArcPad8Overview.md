title: ArcPad 8 简介

categories:
  - 木工开物

date: 2012-02-07 13:59:00
tags: [ArcPad]

---


ArcPad主要是针对外业数据采集人员的一款产品，它相对独立，但不是完全孤立的，可以与GPS、测距仪、数码相机进行一体化作业。2009年4月推出的ArcPad8以其强大的功能为GIS外业人员提供了巨大的便利。

ArcPad包中包含了Arcpad和ArcPad Application Builder，前者主要用于外业数据采集，后者主要用于定制功能。由此大家可能还联想到ArcGIS Mobile，它是集成与ArcGIS Server高级企业版中的，主要用于通过开发来定制移动GIS功能，提供解决方案。ArcPad与ArcGIS Mobile二者可以用ArcGIS Desktop和AE来类比。

ArcPad在移动设备上支持Windows Mobile 5.0以上的系统，PC上支持Vista、XP，目前我用的Windows7，也没发现什么问题。注意：ArcPad8是不再支持Windows CE .NET的。


ArcPad的工作流程大致有三种：


1、**快速工程**：这是一种立即可用的数据采集方案，没有正式的数据结构和现有数据背景，通常需求是临时提的。直接在移动设备上打开ArcPad，选择快速工程，自动生成点线面图层，是shapefiles。通过采集和编辑之后，将这些数据文件copy到ArcGIS Desktop中，利用ArcGIS来管理数据即可。


2、**本地数据工作流程**：原来已经有数据，需要到ArcGIS Desktop中将数据导出，这用到一个工具条ArcPad Data Manager。然后利用手持设备外业采集，在ArcPad中进行编辑，最后将数据再导入即可。这种工作流程通常是用于小型的工作组。


3、**ArcGIS Server 企业级工作流程**：首先是在ArcCatalog或者ArcGIS Server Manager中发布服务，在ArcPad中浏览服务，进行数据的编辑。在ArcPad8中，增加了同步数据的功能，用户可以将在野外实时采集的数据同步到ArcGIS Server的GDB中。大大提高了工作效率。这种工作流程对SDE数据库有要求，就是数据要先注册版本，并且表中要含有字段“GlobalID”。


