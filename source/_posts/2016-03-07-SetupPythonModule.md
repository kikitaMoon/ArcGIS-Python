title: 发布和安装python自定义模块
categories:
  - 木工开物
date: 2015-07-09 13:00:00
tags: [Python]
---
这一篇说下如何发布和安装python自定义模块，版本：Python 2.7 。

<br>

# 1.创建setup.py

现在如果已经写好一个python文件，为了尽量简明，创建一个新的文件夹，把自己py文件放进去。接着在这个文件夹中创建一个名为 setup.py 的文件，用来表示模块的元数据，文件的内容类似下面这个样子。除了手工创建，有很多python编辑器也可以更简便的来创建这个文件，例如 pycharm。

```python
from distutils.core import setup

setup(
    name='nesterprint',
    version='1.0.0',
    packages=[''],
    url='http://blog.csdn.net/kikitaMoon',
    license='',
    author='kikita',
    author_email='kikitamoopn@gmail.com',
    description='My Test'
)

```

<br>


# 2. 打包发布

使用Window自带的命令窗口，转到上一步创建的文件夹目录，输入命令，**python setup.py sdist**：

![](http://img.blog.csdn.net/20150709110253363)

通过上面的状态信息知道，产生了下面的结果：

![](http://img.blog.csdn.net/20150709110634336)


<br>


# 3. 安装

在命令窗口输入命令： **python setup.py install**

![](http://img.blog.csdn.net/20150709111352788)


安装命令也会产生额外的目录，build/lib 。

![](http://img.blog.csdn.net/20150709111855388)

<br>


# 4. 导入模块

import nesterprint ，导入这个自定模块，开始使用其中的myprint函数吧。



![](http://img.blog.csdn.net/20150709112732680)

>PS:这一篇重在发布安装模块的流程，模块内部脚本没提及，在前一篇的最后Demo中有写，可以参考，但是这真的不是重点。


<br>


# 5. 升级模块

如果我们想升级模块，可以不？ 可以！

更新了nesterprint.py 中的一些代码，改进了功能后，来升级下模块。到 setup.py 文件中修改下版本信息，我就叫他2.0.0 。

![](http://img.blog.csdn.net/20150709113804070)


用 2， 3 两步一样的方法发布安装就好了。

![](http://img.blog.csdn.net/20150709114154886)

<br>

<br>

试验一下：

nesterprint 的功能已经升级到 2.0 版本了。

![](http://img.blog.csdn.net/20150709114539197)

> what's new？ 增加了根据列表的深度自动缩进的功能。 


