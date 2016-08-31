title: 上传代码到PyPI
categories:
  - 木工开物
date: 2015-07-09 14:26:05
tags: [Python]
---
我们可以把自己的代码，尤其是期待分享的得意代码，上传分享到第三方Python模块的“集中营” —— **[PyPI](https://pypi.python.org)**，如果没有账号，可以注册个先。

<br>

# 1  准备发布

像在本地发布安装一样，先新建一个文件夹，然后将自己的py文件放进去，然后再这个文件夹中创建一个 setup.py 的文件，内容如下面的样子：


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


# 2 注册登录

使用命令行窗口，跳转到要发布的py所在的文件夹目录，首先进行注册登录，让命令行上传工具知道我的PyPI账户和密码。输入命令：**python setup.py register**，选择 1，输入账户和密码，并且保存登录信息，下次上传可以跳过这个步骤。

![](http://img.blog.csdn.net/20150709140417573)


<br>


# 3 上传发布

接着在命令行窗口中，输入命令： **python setup.py sdist upload**：

![](http://img.blog.csdn.net/20150709140952485)


看到 OK 即上传成功。到 PyPI 自己的账户下看看吧。


![](http://img.blog.csdn.net/20150709141322318)


Bingo ~


<br>


# 4 更新模块

当我们修改了模块中的代码，并想更新 PyPI 上的模块，那就在上传之前更改下 setup.py 的 version 参数，告诉 PyPI 这是个新的版本。



![](http://img.blog.csdn.net/20150709113804070)


并使用相同的命令来上传新的发布版本。

![](http://img.blog.csdn.net/20150709141931924)


好了，看看 PyPI，两个版本的模块都在，其中旧的版本默认被隐藏。

![](http://img.blog.csdn.net/20150709142246342)


<br>


我们可以下载最新版本直接解压安装使用。

![](http://img.blog.csdn.net/20150709142447368)


