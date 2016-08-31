title: 将ArcMap中的符号样式导出的供ArcPad使用
categories:
  - 木工开物
date: 2013-01-15 16:40:35
tags: [ArcPad]
---

1. 在安装有ArcGIS Desktop的机器上，安装ArcPad。这里采用了各个产品的最新版本，分别是ArcGIS Desktop 10.1 和 ArcPad 10.0.4。

![](http://img.my.csdn.net/uploads/201301/15/1358238637_3345.png)

2. 激活ArcMap中的对应扩展：

![](http://img.my.csdn.net/uploads/201301/15/1358238370_4517.png)

3. 打开ArcPad 工具条，将当前地图的样式导出。

![](http://img.my.csdn.net/uploads/201301/15/1358238700_3584.gif)

默认是保存在安装目录下的Style文件夹。将将要生成的aps最好放置到这个位置， **\Users\Public\Documents\ArcPad\Styles** 。

为什么么呢？后面会说到~

无论保存在哪，最后会提示保存成功。

![](http://img.my.csdn.net/uploads/201301/15/1358238921_8524.gif)

4. 使用ArcPad样式文件。

ArcPad读取并使用这些样式，对路径是有要求的，只要下述路径才能直接使用。因此其他路径是需要重新拷贝的。

- **PC Windows：\Users\Public\Documents\ArcPad\Styles**

- **移动设备 WM： \Program Files\ArcPad\Styles**

最后，在ArcPad的图层属性中就可以看到ArcMap导出的自定义的Style文件。

![](http://img.my.csdn.net/uploads/201301/15/1358239383_4059.png)

哦啦，就到这里~



