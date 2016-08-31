title: 3D数据互操作之认识Collada
categories:
  - 木工开物
date: 2013-03-04 09:22:20
tags: [3D,Geodata]
---

Collada的名称来自于COLLAborative Design Activity（协同设计活动），是用于存储 3D 模型的开放式标准 XML 格式，最早是由 Sony Computer Entertainment（SCEA）发起。

以下介绍来自网络：

*COLLADA™ 是面向交互式 3D 应用程序的基于 XML 的数字资产交换方案，使 3D 创作应用程序可以自由地交换数字资产而不损失信息 - 使多种DCC和3D处理软件包可以组合成强大的工具链管道。独特的交互模式提供了广泛全面的视觉编译。COLLADA FX支持使用 OpenGL ES 着色语言创作和封装着色器，以使一流的 3D 创作工具可以有效协作创建 OpenGL / OpenGL ES 应用程序和资产。
 COLLADA是一个开放的标准，最初用于3D软件数据交换，由SCEA发起，现在则被许多著名厂家支持如Autodesk、XSI等。COLLADA不仅仅可以用于建模工具之间交换数据之用，也可以作为场景描述语言用于小规模的实时渲染。因为COLLADA DOM拥有丰富的内容用于表现场景中的各种元素，从多边形几何体到摄像机无所不包。我们可以通过COLLADA DOM库来进行场景文件的读取与处理操作。COLLADA DOM的编程方式类似COM。*

总之，我们可以将Collada理解成一个开放的3D数据资源的交换方案。COLLADA 文件的扩展名是 .dae，此类文件中还可能引用一些附加的图像文件，这些文件被用作 3D 对象上覆盖的纹理。
了解更多资源，点击：http://collada.org/mediawiki/index.php/COLLADA

<br>

ArGIS Desktop 中如何转化呢？

从ArcGIS 10.0之后，ArcToolbox中就增加了 Multipath to Collada，可以将ArcGIS的多面体矢量格式转换为3D的解决方案。从而也便利了与 SkecthUp，3DS Max 等第三方软件的交互。

将多面体要素导出到 COLLADA 会创建若干文件 - 一个包含 3D 对象的 XML 表示的 .dae 文件以及一个或多个包含纹理的图像文件（例如 .jpg 或 .png 文件）。

每一个multipatch会对应的生成一个Collada文件，他们之间的关联是通过指定字段维护的，如果没有特殊指定，就使用ObjectID。

![](http://img.my.csdn.net/uploads/201303/04/1362360437_3503.png)

