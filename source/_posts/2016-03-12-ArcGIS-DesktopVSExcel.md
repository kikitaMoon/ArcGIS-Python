title: ArcGIS Desktop 与 Excel
categories:
- 木工开物
date: 2014-02-11 11:35:40
tags: [Geodata]
---
微软 OFFICE 产品中，Excel是很强大，并且平民化的表格制作工具。ArcGIS 用户会经常需要在两种软件中做交互，今天就来说一说&nbsp;ArcGIS Desktop 与 Excel。

# ArcGIS Desktop 中访问 Excel 数据


Excel 表可直接在 ArcGIS 中打开，使用方法与其他表格数据源类似。例如，可以向 ArcMap 中添加这种表、在 ArcCatalog 中预览这种表，并可将这种表作为地理处理工具的输入数据。


通过 ArcGIS 进行访问Excel表时，每个工作表在 ArcGIS 中都是一个单独的表，名称末尾带有美元符号 $ 标识，但是这个$并不是表名的一部分。如果工作表的表名中包含空格，那表名称周围会括有单引号。



![](http://img.blog.csdn.net/20140211102406546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


# 对于ArcGIS Desktop 对 office 版本的支持情况


ArcGIS 支持 ：

- Excel 2003 以及更早版本的 .xls 文件；
- Excel 2007 的 .xlsx 文件。

为什么要分开说呢？

*.xls 文件可以直接在ArcGIS中以只读的形式打开，例如直接在ArcMap中添加数据、在ArcMap中添加XY数据显示为点、在ArcCatalog中进行查看等等。

而 *.xlsx 文件打开时，需要有一个数据驱动。如果我们遇到这个错误：“ **Failed to connect to ddatabase. An underlying database error occured. 没有注册类**”，那就是缺少驱动的结果。

一般如果我们安装了 MS Office 2010 或者 2013，或者根本就没有安装 Office，这个错误必然会遇到了。

![](http://img.blog.csdn.net/20140211111357921?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


<br>

需要安装 &nbsp;2007 Office System 驱动程序（AccessDatabaseEngine.exe），下载英文版点[这里](http://www.microsoft.com/en-us/download/details.aspx?displaylang=en&amp;id=23734)，中文版点[这里](http://www.microsoft.com/zh-cn/download/details.aspx?id=23734)，这个包的官方说明如下：



这个程序安装之后，上述错误即可解决。


# ArcGIS访问Excel表时，字段类型的确定


ArcGIS 访问 Excel 时，字段名称从工作表各列的首行中获取。

在 Excel 中指定的字段类型对 ArcGIS 中显示的字段类型不起任何决定作用。ArcGIS 中的字段类型是由该字段的头八行值扫描决定的。

如果在单个字段中扫描到混合数据类型，则该字段将以字符串字段的形式返回，并且其中的值将被转换为字符串。

在 ArcGIS 中，数值字段将被转换为双精度数据类型。




# 其他问题


1. 如果不想安装前面的驱动，最快的办法使得ArcGIS能够访问2007以后版本的表格文档，那就另存为97-2003版本的 *.xls了。

2. 想把要素类的属性表导出来以供Excel使用，那就将属性表导出为 *.dbf 格式，然后打开方式使用 Excel 即可。

3. 使用工具 Export to Excel 也可以将表导出为 Excel 表。