title: ArcGIS中的地理坐标系转换方法参数（一）
categories:
- 木工开物
date: 2014-01-17 18:00:00
tags: [Coordinate System]
---

地理坐标系变换是数据处理过程中常遇到的问题，今天就说下这方面的问题。

<em><span style="color:#009900">如果遇到这种情景：两份数据有不同的坐标系，想叠加在一起显示，作图或显示精度要求不高。</span></em>

<em><span style="color:#009900">这种情况使用 ArcMap 的动态投影即可，ArcMap 的内部动投影机制会解决地理坐标系变换的问题。数据在显示的过程中，会实时的被转换，但不改变数据本身。</span></em>

如果我们需要进行地理坐标系转换，我们知道 ArcGIS Desktop 中提供了 Project 工具。

此工具界面上有个至关重要的参数：<strong>Geographic Transformation。</strong>我们发现它的后面赫然写着。依照使用其他工具的经验，这种打了 Optional 标志的参数，不就是可填可不填的意思吗？

但是，它真的让你随便的可填可不填吗？ Naive！ 图样图森破！ 这个参数的填写与否，完全是受前面两个参数决定的，主要三种情景吧。

<br>

<strong><span style="color:#990000">情景1：</span></strong>


不涉及到地理坐标系变换的坐标变换，这个参数完全不需要，而不是 optional 哦。


例如：从 GCS_Xian_1980 进行投影变换，转换为 Xian_1980_3_Degree_GK_CM_120E 投影坐标系。


整过转换中，仅使用了高斯克吕格投影变换，没有涉及到地理坐标变换。


<img src="http://img.blog.csdn.net/20140117171332968?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" width="420" height="451" alt="" /><br />



<br />



<br />



<span style="color:#990000"><strong>情景2：</strong></span>


涉及到地理坐标系变换的坐标变换，并且ArcGIS 已知二者之间的变换方法，这个参数是必须的，在已知列表中做选择或者自定义。（自定义见：情景3）


例如：从&nbsp;GCS_Beijing_1954，转换为&nbsp;GCS_WGS_1984坐标系。


转换过程中涉及到地理坐标系变换，也就是进行了椭球体变换。


ArcGIS 中提供了6种已知转换方法，可以根据适用范围选择之。其中如何选择，此文不做介绍，请查看我的另一篇博客：<a target="_blank" href="http://blog.csdn.net/kikitamoon/article/details/12914477">http://blog.csdn.net/kikitamoon/article/details/12914477</a>


<img src="http://img.blog.csdn.net/20140117171927109?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="420" height="451" alt="" />


<br />



<br />



<span style="color:#990000"><strong>情景3：</strong></span>


涉及到地理坐标系变换的坐标变换，并且ArcGIS 未知二者之间的变换方法，也就是ArcGIS没有提供转换方法，但是这个参数是必须的，需要自定义，这个参数前会亮绿灯，告诉用户，必须要填写。另外，上面情景2中，ArcGIS给出的方法，如果都不是自己需要的，也需要自定义。<br />



例如：从&nbsp;GCS_Beijing_1954，转换为&nbsp;GCS_Xian_1980坐标系。


<img src="http://img.blog.csdn.net/20140117173532843?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="420" height="450" alt="" /><br />



<br />



需要使用工具 Creat Custom Geographic transformation，创建一种转换方法，辅助 Project 工具。


这个工具的帮助如下，就不赘述了。


<a target="_blank" href="http://resources.arcgis.com/zh-cn/help/main/10.2/index.html#//001700000076000000">http://resources.arcgis.com/zh-cn/help/main/10.2/index.html#//001700000076000000</a><br />



<br />



<br />



<strong><span style="color:#990000">补充：</span></strong>


讲到这里全部的情形都涵盖了。有的同学会问，为什么会这样呢？ArcGIS为啥就不能都知道转换方法呢？为啥偏要我们自定义呢？好麻烦的耶%￥#@……


有些坐标系转换的参数是不公开的，属于涉密的内容，所以ArcGIS是没有权利知道变换方法的。例如与 Xian 80 有关的变换。原文：<span style="color:rgb(77,77,77); font-family:'Comic Sans','Comic Sans MS',cursive,Courier,sans-serif; font-size:14.399999618530273px; line-height:20.149999618530273px">Some geographic coordinate systems do not have any publicly known transformations because that information is considered to have strategic importance to a government or company.&nbsp;</span>


<br />



好了，至此，大致就知道这个参数什么时候不需要，什么时候需要，如果没有如何得到，这几个问题。
