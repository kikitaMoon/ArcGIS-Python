title: shapefile与字符集编码设置
categories:
- 木工开物
date: 2014-02-13 13:38:36
tags: [Geodata]
---
在 ArcGIS Desktop&nbsp;(ArcMap, ArcCatalog, and ArcToolbox)中，有编码页转换功能（CODE PAGE CONVERSION），可以读写多种字符编码的 shapefile 和 dBASE 表。 在系统注册表中，编码页转换功能（CODE PAGE CONVERSION）命名为 'dbfDefault'，可以修改这个值。 

在&nbsp;ArcGIS 10.2.1 之前，可以直接按照 'dbfDefault' 设置方法 到注册表中修改。 

在&nbsp;ArcGIS Desktop 10.2.1 以及以后的版本，shapefile (.DBF) 的编码页的默认设置为&nbsp;UTF-8 (UNICODE) 。

<br>

----------

更新内容（2014.8.1）

ArcGIS Desktop 10.2.1 和 10.2.2 版本下需要修改编码行为，先打补丁，然后再按照 **'dbfDefault' 设置方法** 到注册表中修改。</span></span>**</span>

**10.2.1**：  [http://support.esri.com/en/downloads/patches-servicepacks/view/productid/160/metaid/2090](http://support.esri.com/en/downloads/patches-servicepacks/view/productid/160/metaid/2090) 

**10.2.2**：  [http://support.esri.com/en/downloads/patches-servicepacks/view/productid/67/metaid/2089](http://support.esri.com/en/downloads/patches-servicepacks/view/productid/67/metaid/2089)

----------


<br>


# 'dbfDefault' 的作用



使用 ArcGIS for Desktop 打开 dBase 表文件时，程序先去读头文件中的 &nbsp;Language Driver ID (LDID) 或者是同名 *.CPG文件。前面二者都是用来在读文件之前，决定用什么编码类型来正确读出文件。如果有必要， ArcGIS for Desktop 会进行编码转换来显示字符串。


如果文件缺失&nbsp;LDID 或者 &nbsp;.CPG 文件，编码就会被假定为 Windows (ANSI/Multi-byte)。也是因为这个原因，</span><span style="font-size:12px">如果文件是 OEM 编码的，并且没有写入 LDID 或者 .CPG，字符就会出现乱码。 也就说 ArcGIS 把 OEM 文件当成 ANSI 文件来处理了。


多数情况下， shapefiles 和 dBASE 文件都会存储编码页信息。 但是有些程序的 OEM 文件没有包含编码页信息，例如 Microsoft Access 2000 and Excel 2000，所以这些文件读取时，就会乱码。为了避免这个问题，用户可以给没有编码页信息的文件设置
**dbfDefault**。



**写**


在注册表中设置 'dbfDefault' ，可以决定导出的 shapefile 和 dBASE 的编码类型。例如，把 'dbfDefault' 设置为 OEM ，那么用 ArcMap, ArcCatalog, ArcToolbox 生成出来的 shapefile 和 dBASE 文件就是以 OEM编码的，设置成 ANSI ，那 shapefile 和 dBASE 文件就是 ANSI 编码的。 



**读**

读 shapefile 和 dBASE 文件的逻辑与写是相同的，如果缺失编码信息，ArcGIS 读取文件的编码类型由 **dbfDefault**决定。


<br>

# 不适用'dbfDefault' 的情况

'dbfDefault' 这项设置仅对 ArcGIS Desktop 生效，对于一些很老版本的ArcGIS 产品不适用；仅对 shapefile 生效，Personal GDB等不生效。


<br>

**无视 'dbfDefault' 设置的包括：**

*In ArcInfo Workstation:*

- ARCSHAPE with &amp;CODEPAGE OEM creates a shapefile in OEM&nbsp;

- ARCSHAPE with &amp;CODEPAGE ANSI creates a shapefile in ANSI&nbsp;

- INFODBASE with &amp;CODEPAGE OEM creates a dBASE file in OEM&nbsp;

- INFODBASE with &amp;CODEPAGE ANSI creates a dBASE file in ANSI&nbsp;

*In ArcView 3.x,&nbsp;*

- Shapefile and dBASE files are saved in the ANSI code page.&nbsp;

*In ArcGIS for Desktop (regardless of the dbfDefault setting),&nbsp;*

- Personal geodatabases are saved in Unicode&nbsp;

- Personal geodatabase tables are saved in Unicode&nbsp;

- Coverages are saved in the ISO code page&nbsp;

- INFO files are saved in the ISO code page&nbsp;

- Interchange files are saved in the ANSI code page&nbsp;

- Text files are saved in the ANSI code page</span></span>


<br>


#  'dbfDefault' 设置方法

1. 开始 -- 运行，输入”Regedit“，打开&nbsp;**注册表**。

2. 如是用的是 10.x 版本 ArcGIS Desktop，定位到 ‘**My Computer\HKEY_CURRENT_USER\Software\ESRI\Desktop 10.x**. 如果是9.3.1之前的版本，定位到 'My Computer\HKEY_CURRENT_USER\Software\ESRI'。 

3. 创建项 **`Common`**， 接着在其下创建 **`CodePage`** 项， 添加 **`字符串`** ，名称： **`dbfDefault`** ，健值： **`oem`</span>（或者`936`）**。

![](http://img.blog.csdn.net/20140213131243500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)</span>

<br>

如下为支持的编码值：


**OEM** Code Page Values:

OEM, 437, 708, 720, 737, 775, 850, 852, 855, 857, 860, 861, 862, 863, 864, 865, 866, 869, 932, 936, 950

**ANSI** Code Page Values:

ANSI, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, Big5, SJIS&nbsp;</span></span>


**ISO** Code Page Values:

ISO, 88591, 88592, 88593, 88594, 88595, 88596, 88597, 88598, 88599, 885910, 885913, 885915, EUC

**Unicode** Values:

UTF-8

<br>

现在，Shapefiles 可以以 UTF-8 存储，但是，只有在 ArcGIS Desktop 中才能被识别。

相关技术文章：

[http://support.esri.com/en/knowledgebase/techarticles/detail/21106](http://support.esri.com/en/knowledgebase/techarticles/detail/21106)