title: 深入路径距离分析（三）
categories:
- 木工开物
date: 2014-09-15 12:56:17
tags: [Geoprocessing]
---
路径分析不仅可以考虑到水平方向的影响因子，而且可以考虑到垂直方向的影响因子，例如前面开车的例子中，水平方向的影响因子是风向，垂直方向的影响因子就是路面的起伏状况。

**垂直系数**

垂直系数越大，移动的难度也就越大。确定从一个像元行进到另一个像元时遇到的垂直系数（VF）与确定水平系数（HF）相似。这里需要引入一个概念，垂直相对移动角度（VRMA），垂直相对移动角度（VRMA）是“起始”像元与“目标”像元形成的斜率的角度，斜率=垂直增量/水平增量。VRMA 以度为单位进行指定。VRMA 的值范围为 -90 到 +90 度。

路径距离分析工具中，提供了几种算法，**BINARY、LINEAR、SYM_LINEAR、INVERSE_LINEAR、SYM_INVERSE_LINEAR、COS、SEC、COS_SEC、SEC_COS、TABLE**：

![](http://img.blog.csdn.net/20140913235422125)

<br>

**（1）Binary——二元垂直系数**

当 VRMA 大于切削角下限且小于切削角上限时，在两个像元之间移动的 VF 设置为与零系数相关联的值。如果 VRMA 大于切削角上限或者小于<span style="font-family: 'Microsoft YaHei';font-size:14px;">切削角下限</span>，则 VF 设置为无穷大。工具默认的切削角为正负30度。

![](http://img.blog.csdn.net/20140914003649682)

![](http://img.blog.csdn.net/20140914003509703)

<br>

**（2）Linear——线性垂直系数**

VF 由 VRMA-VF 坐标系中的一条直线确定。这条线在 y 轴上与零系数相关联的值处进行截取。线的斜率可以使用 SLOPE 属性进行指定。如果未确定斜率，则默认值为 1/90（指定为 0.01111）。默认的切削角下限为 -90 度，而默认的切削角上限为 90 度。

![](http://img.blog.csdn.net/20140914004337732)

![](http://img.blog.csdn.net/20140914004212218)

<br>

**（3）Inverse Linear——逆线性垂直系数**

这个与线性垂直系数类似，VF 由 VRMA-VF 坐标系中的一条直线的逆向值确定。这条线在 y 轴（表示 VF 系数）上与零系数相关联的值处进行截取。线的斜率可以确定（如果使用 SLOPE 修饰属性指定）。如果未确定斜率，则默认值为 -1/45（指定为 0.02222）。默认的切削角下限为 -45 度，而默认的切削角上限为 45 度。



**注意：这个算法的图表，在ArcGIS的帮助中绘制错误了，画成了二次曲线的样子，如下是改正后正确图表。**_

![](http://img.blog.csdn.net/20140914010130562)


<span style="font-family:Microsoft YaHei;font-size:14px;color:#3366ff;"><span style="font-family: 'Microsoft YaHei';font-size:14px;">_


![](http://img.blog.csdn.net/20140914005439828)

<br>

**（4）Symmetric Linear——对称线性垂直系数**

SYM_LINEAR 由两个与 VRMA 相关的线性函数组成，这两个函数关于 VF (y) 轴对称。两条线都在与零系数相关联的 VF 值处截取 y 轴。使用 SLOPE 垂直系数修饰属性相对于正 VRMA 定义线的斜率，然后将针对负 VRMA 生成一个镜像。默认斜率为 1/90（指定为 0.01111）。默认的切削角下限为 -90，而默认的切削角上限为 90。



![](http://img.blog.csdn.net/20140914010301296)

![](http://img.blog.csdn.net/20140914010524406)


<br>

**（5）Symmetric Inverse Linear——对称线性垂直系数**

顾名思义，SYM_INVERSE_LINEAR 与 SYM_LINEAR 垂直系数关键字正相反。它由两个与 VRMA 相关的线性函数组成，这两个函数关于 VF (y) 轴相对称。两条线都在 VF 值为 1 处截取 y 轴。使用 SLOPE 垂直系数修饰属性相对于与正 VRMA 定义线的斜率，然后将针对负 VRMA 生成一个镜像。默认斜率为 -1/45（指定为 .02222）。默认的切削角下限为 -45，而默认的切削角上限为 45。


**注意：这个算法的图表，在ArcGIS的帮助中也绘制错误了，也画成了二次曲线的样子，如下是改正后正确图表。**</span>



![](http://img.blog.csdn.net/20140914011146888)


![](http://img.blog.csdn.net/20140914010919265)

<br>

**（6）Cos——余弦垂直系数**

VF 由 VRMA 的余弦函数确定。默认的切削角下限为 -90 度，而默认的切削角上限为 90 度。默认的 COSPOWER 为 1.0。

![](http://img.blog.csdn.net/20140914011138140)

![](http://img.blog.csdn.net/20140914011357725)

<br>

**（7）Sec——正割垂直系数**

VF 由 VRMA 的正割函数确定。默认的切削角下限为 -90 度，而默认的切削角上限为 90 度。默认的 SECPOWER 为 1.0。

![](http://img.blog.csdn.net/20140914011836435)

![](http://img.blog.csdn.net/20140914011900038)

<br>

**（8）Cos-Sec——余弦正割垂直系数**

当 VRMA 度数为负值时，VF 由 VRMA 的余弦函数确定。如 VRMA 度数为正值，VF 则由 VRMA 的正割函数确定。默认的切削角下限为 -90 度，而默认的切削角上限为 90 度。默认的 COSPOWER 和 SECPOWER 均为 1.0。


![](http://img.blog.csdn.net/20140914011816734)

![](http://img.blog.csdn.net/20140914011929031)

<br>

**（9）Sec-Cos——正割余弦垂直系数**

当 VRMA 度数为负值时，VF 由 VRMA 的正割函数确定。如 VRMA 度数为正值，VF 则由 VRMA 的余弦函数确定。默认的切削角下限为 -90 度，而默认的切削角上限为 90 度。默认的 COSPOWER 和 SECPOWER 均为 1.0。



![](http://img.blog.csdn.net/20140914012144843)


![](http://img.blog.csdn.net/20140914012440290)

<br>

**（10）Table——自定义表格垂直系数**

与 HRMA 图一样，VRMA 图中的字符可由修饰属性进行进一步的控制，从而细化垂直系数。这个就不再赘述了。


好了，到这里路径距离分析就说完了，也就是说，当需要计算最短路径的时候，需要考虑和前进方向有关的水平阻力因子和垂直阻力因子的时候，可以使用 ArcGIS 的路径距离分析工具，可以使用工具中的既定算法模型，通过配置参数达到目的，或者自定义表格自定义细化水平或垂直系数。