title: 空间分析之邻域分析

categories:
  - 木工开物

date: 2012-08-23 16:49:00
tags: [Geoprocessing,Spatial Analyst]

---


ArcGIS 的空间分析扩展中，提供了这样一组邻域分析工具：

![](http://my.csdn.net/uploads/201208/20/1345445275_4135.png)

<br>

# **1. 块统计（Block Statistics）**

分块统计，按照指定邻域类型计算区域统计值，输出区域为指定邻域类型的外接矩形。

以下为邻域的形式：

* Nbr**Annulus**({innerRadius}, {outerRadius}, {CELL | MAP})
* Nbr**Circle**({radius}, {CELL | MAP}
* Nbr**Rectangle**({width}, {height}, {CELL | MAP})
* Nbr**Wedge**({radius}, {start_angle}, {end_angle}, {CELL | MAP})
* Nbr**Irregular**(kernel_file)
* Nbr**Weight**(kernel_file)

Irregular与Weight邻域类型需要指定核文件（ .txt 文件）。

可以进行统计的计算类型：

* **MEAN**/平均值；
* **MAJORITY**/众数（出现次数最多的值）；
* **MAXIMUM**/最大值；
* **MEDIAN**/中值；
* **MINIMUM**/最小值；
* **MINORITY**/少数（出现次数最少的值）；
* **RANGE**/范围（最大值和最小值之差）。
* **STD**/标准差。
* **SUM**/总和。
* **VARIETY**/变异度（唯一值的数量）。

例如，输入为圆形邻域，输出为外接矩形的像元范围：

![](http://my.csdn.net/uploads/201208/22/1345608085_7238.gif)![](http://my.csdn.net/uploads/201208/22/1345608090_2034.gif)![](http://my.csdn.net/uploads/201208/22/1345616739_2158.gif)


# **2. 滤波器（Filter）**

对栅格执行平滑（低通）滤波器或边缘增强（高通）滤波器。

滤波器工具既可用于消除不必要的数据，也可用于增强数据中不明显的要素的显示。

低通滤波（平滑边界）：

![](http://my.csdn.net/uploads/201208/22/1345619338_2779.png)   ![](http://my.csdn.net/uploads/201208/22/1345619348_1594.png)

高通滤波（边缘增强）：

![](http://my.csdn.net/uploads/201208/22/1345620385_8334.png)   ![](http://my.csdn.net/uploads/201208/22/1345620399_3640.png)

# **3. 焦点流（Focal Flow）**

焦点流工具使用直接的 3 x 3 邻域来确定一个像元的八个相邻点中哪一个流向此像元。

焦点流也可以是液体由高到低流动的方向，也可以是定义的任何移动（比如污染物向污染浓度较低的地方流入）。

![](http://my.csdn.net/uploads/201208/22/1345628029_1229.gif)

举个例子，各个方向流向像元中心像元的值总和是最终值。

![](http://my.csdn.net/uploads/201208/23/1345689573_4554.gif)


# **4. 焦点统计（Focal Statistics）**

为每个输入像元位置计算其周围指定邻域内的值的统计数据。

统计类型与邻域形状与块统计是相同的，区别在于，块统计的输出是整个邻域的外接矩形范围，而焦点统计的输出，是邻域内的焦点栅格。如下图：

![](http://my.csdn.net/uploads/201208/23/1345692857_9912.png)![](http://my.csdn.net/uploads/201208/23/1345692904_9259.png)![](http://my.csdn.net/uploads/201208/23/1345692848_4441.png)

![](http://my.csdn.net/uploads/201208/23/1345692864_5106.png)


# **5. 线统计**

工具用于为每个输出栅格像元周围的圆形邻域内所有线的指定字段值计算统计量。

可用的统计量类型有：均值、众数、最大值、中位数、最小值、少数、范围、标准差以及变异度。只有众数、少数和中位数统计量是根据线长度进行加权的。

![](http://my.csdn.net/uploads/201208/23/1345706357_1591.gif)

![](http://my.csdn.net/uploads/201208/23/1345706657_9521.gif)

还没有想到此工具的应用场景，以后有了再来追加。


# **6. 点统计**


该工具类似于焦点统计工具，不同之处在于它直接对点要素而非栅格进行操作。直接对要素进行操作的其中一个优点在于，即使点距离过近，在转换成栅格时点也不会丢失。


