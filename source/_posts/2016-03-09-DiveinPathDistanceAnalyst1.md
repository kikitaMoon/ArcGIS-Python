title: 深入路径距离分析（一）
categories:
- 木工开物
date: 2014-09-15 09:10:07
tags: [Geoprocessing]
---
写这篇之前，整理过空间分析中的距离分析工具箱，今天继续深入的说说路径距离分析。

开始路径距离分析之前，先回忆下最基本的欧式距离分析和成本距离分析。欧氏距离分析遵循的就是我们小学都知道的“两点之间直线最短”的原则，两点之间的最短路径就是两点之间的线段的距离。但是实际情况并不是很完美，有时我们无法完全沿直线前往某个位置，例如遇到河流、陡坡、悬崖等障碍。这时，我们就应该考虑使用成本距离工具获得更现实的结果。

如下图，举个简单的例子说明成本距离分析和欧式距离分析。按照欧式距离在问号位置求得的应该是绿色的路径，表示最近源，但是考虑到成本，黄色的曲线确是成本最低的最优路径。并且“曲线救国”比盲目直行，成本更低。

![](http://img.blog.csdn.net/20140913104319765?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


回顾就到这里，继续看更加复杂的路径距离分析：

路径距离工具与成本距离相似，两者都用于确定从源到栅格上各像元位置的最小累积行进成本。但是，路径距离不仅可计算成本表面的累积成本，而且可以考虑到从一个位置到另一个位置的总移动成本的水平和垂直因子补偿。这些工具生成的累积成本表面可用于扩散建模、流向运动和最低成本路径分析。路径距离工具既考虑水平和垂直成本要素，又考虑真实表面距离。


举个简单的例子，了解路径距离分析，假设我们开车从位置A到位置B，路况复杂，还有点起风，这时风向和风速就成了水平影响因子，道路的起伏程度就行了垂直因子。如下图，说明这个问题：

水平影响因子：

![](http://img.blog.csdn.net/20140913120432031?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

垂直影响因子：

![](http://img.blog.csdn.net/20140913120618050?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2lraXRhTW9vbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

理解了路径距离分析工具的用途，在下一篇文章中，我们一起来看看水平系数和垂直系数对路径距离的影响。

