title: 将度-分-秒值转换为十进制度
categories:
  - 木工开物
date: 2013-07-22 10:21:29
tags: [Geodata]
---


在ArcMap中，在表中新建一个字段，用于存储新的十进制度值，使用字段计算器和 VB 脚本实现。

如下示例，其中，假设 Latitude 是表中存储 DMS 纬度值字段的名称，经纬度数据中的度分秒三个数据是以空格分隔。

```
Dim Degrees
Dim Minutes
Dim Seconds
Dim DMS
Dim DD

DMS = Split([Latitude])
Degrees = CDbl(DMS(0))
Minutes = CDbl(DMS(1))
Seconds = CDbl(DMS(2))
If Degrees < 0 Then
   DD = -(Seconds/3600) - (Minutes/60) + Degrees
Else
   DD = (Seconds/3600) + (Minutes/60) + Degrees
End If
```

PS：使用到的VBScript 函数：

（1）**Split**：

    Split(expression[,delimiter[,count[,compare]]])

（2）**CDbl**：

CDbl 函数可把表达式转换为双精度（Double）类型。


结果示例：


![](http://img.blog.csdn.net/20130722102111140?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)