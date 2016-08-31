title: 如何检测显卡类型和OpenGL版本?
categories:
  - 木工开物
date: 2013-03-04 09:17:58
tags: [Deployment]
---

# **摘要**

OpenGL是一个行业标准的3D图像API。运行 CityEngine 需要 OpenGL 2.x 或更高版本。OpenGL 驱动通常与显卡驱动和支持的软件（例如：DirectX）一同安装。

<br>

# **过程**

## 1.检测显卡类型（Windows）：

1） 打开 “**运行**” 窗口。

2）输入&nbsp;**`dxdiag`**&nbsp;进入 DirectX诊断工具，即列出显卡信息。

![](http://img.my.csdn.net/uploads/201303/04/1362360176_7429.jpg)


## 2.检测 OpenGL版本（Windows，Mac，移动设备）

需要安装个第三方小软件。。名字叫：OpenGL Extension Viewer.

下载并安装 OpenGL Extension Viewer 

**Mac、移动设备**：在 OpenGL Extension Viewer 网页中，对应的选择从 Mac App Store、iTunes Store、Android Market下载即可。

![](http://img.my.csdn.net/uploads/201303/04/1362360184_9650.png)

<br>

OpenGL Extension Viewer是个免费的应用程序，由 Realtech VR 开发。此工具可以显示当前安装的 OpenGL 版本，并且可以检测和升级显卡驱动。

![](http://img.my.csdn.net/uploads/201303/04/1362360193_7094.jpg)



<br>

本文内容来源于 ArcGIS Resource Center 技术文件，编号：[39476](http://support.esri.com/en/knowledgebase/techarticles/detail/39476)

