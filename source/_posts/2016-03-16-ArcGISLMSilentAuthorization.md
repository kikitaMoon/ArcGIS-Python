title: ArcGIS License Manager 静默授权命令摘录
categories:
  - 木工开物
date: 2013-08-06 17:31:21
tags: [License]
---


在命令行中，将目录更改为许可管理器安装位置。Windows 上的默认位置是 `C:\Program Files (x86)\ArcGIS\License10.1\bin`。

在命令的末尾添加 `-verbose`，可以在命令窗口中显示进度和错误消息。

<br>


**以静默方式授权：**


`softwareauthorizationls.exe -s -lif -ver10.1 "c:\temp\<*.prvs>" `

当离线授权时，此命令还可以与 ***.resps** 文件结合使用。当授权单机版 Desktop 或 Engine 许可时，可使用 *.prvc 和 *.respc。


为离线授权创建一个 **.txt** 授权文件：

`softwareauthorizationls.exe -s -lif -ver 10.1 "C:\Temp\<.prvs>" -out "C:\Temp\authorize.txt" `


<br>


**以静默方式取消授权：**



要从机器中取消所有许可的授权，请运行 `softwareauthorizationls.exe -s -return all`。

要从机器中取消特定许可的授权，您需要输入要取消授权的具体授权码。运行 `softwareauthorizationls.exe -s -return EFLxxxxxxxxx,EFLxxxxxxxxx`。


<br>


**以静默方式升级许可：**

要在机器中升级所有许可，请运行 `softwareauthorization.exe -s -upgrade all`。

要在机器中升级特定许可，您需要输入具体的授权码。运行 `softwareauthorization.exe -s -upgrade EFLxxxxxxxxx,EFLxxxxxxxxx`。