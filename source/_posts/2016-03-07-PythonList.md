title: Python列表常用操作
categories:
  - 木工开物
date: 2015-07-07 17:49:58
tags: [Python]
---
Python的列表非常好用，一些常用的操作写在这里。


<br>

在Python中创建一个列表时，解释器会在内存中创建一个类似数组（但不是数组）的数据结构来存储数据。列表中的编号从 0 开始，然后是1，依此类推。


![](http://img.blog.csdn.net/20150707101532255)


<br>

<br>


**print() 显示列表；**

**len() 得出列表中有多少数据项；**

**append() 在列表末尾追加一个数据项；**

**extend() 在列表末尾增加一个数据项集合；**

**pop() 在列表末尾删除一个数据项；**

**remove() 在列表中删除一个特定的数据项；**

**insert()  在特定位置前面增加一个数据项；**

**count()  统计某个数据项在列表中出现的次数；**

**reverse() 反向列表中数据项。**


<br>


```python
>>> Fruit = ["Apple","Pear","Grape","Peach","Bananer"]
>>> print(len(Fruit))
5
>>> print(Fruit[0])
Apple
>>> print(Fruit[4])
Bananer

>>> Fruit.append("tomato")
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Peach', 'Bananer', 'tomato']

>>> Fruit.extend(["lemon","coconut"])
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Peach', 'Bananer', 'tomato', 'lemon', 'coconut']

>>> Fruit.pop()
'coconut'
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Peach', 'Bananer', 'tomato', 'lemon']

>>> Fruit.remove("Peach")
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Bananer', 'tomato', 'lemon']
>>> Fruit.remove(Fruit[0])
>>> print(Fruit)
['Pear', 'Grape', 'Bananer', 'tomato', 'lemon']

>>> Fruit.insert(0,"Apple")
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Bananer', 'tomato', 'lemon']
>>> Fruit.insert(6,"coconut")
>>> print(Fruit)
['Apple', 'Pear', 'Grape', 'Bananer', 'tomato', 'lemon', 'coconut']

>>> Fruit.count("Apple")
1





```

<br>

用迭代显示列表中的数据项，以下的代码段中 **for** 和 **while** 完成的工作是一样的：

```Python
>>> for item in Fruit:
	print(item)

```

```python
>>> while count < len(Fruit):
	  print(Fruit[count]) 
	  count = count + 1
```
```	
# 输出结果
Apple
1
Pear
2
Bananer
3
```

<br>

如果字符串中需要包含双引号，不要忘记转义 ，**\"**。

```python
>>> Fruit.append("\"Tomato\"")
>>> print(Fruit)
['Apple', 1, 'Pear', 2, 'Bananer', 3, '"Tomato"']

```


<br>

**isinstance()** 函数可以用来判断特定标识符是否包含某个特定类型的数据。

```python
>>> isinstance(Fruit,list)
True

>>> isinstance(count,list)
False
```

<br>

<br>

Python中列表可以嵌套，并且可以支持任意多层的嵌套，例如：

```python
>>> print(Fruit)
['Apple', 1, 'Pear', 2, 'Bananer', 3]

>>> Fruit.append(["A","B","C"])
>>> print(Fruit)
['Apple', 1, 'Pear', 2, 'Bananer', 3, '"Tomato"', ['A', 'B', 'C']]

>>> Fruit[-1].append(["aa","bb","cc"])
>>> print(Fruit)
['Apple', 1, 'Pear', 2, 'Bananer', 3, '"Tomato"', ['A', 'B', 'C', ['aa', 'bb', 'cc']]]
```

```python
>>> for i in Fruit:
	print(i)
	
Apple
1
Pear
2
Bananer
3
"Tomato"
['A', 'B', 'C', ['aa', 'bb', 'cc']]
```



试试输出三层嵌套的列表中的各个数据项：


```python
>>> for i in Fruit:
	if isinstance(i,list):
		for j in i:
			if isinstance(j,list):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)

		
Apple
1
Pear
2
Bananer
3
"Tomato"
A
B
C
aa
bb
cc
```


<br>

<br>

上面的循环嵌入的有点多，如果是N层嵌套的列表重复代码会很多，来点优化试试：

```python
>>> def my_print(mylist):
	for i in mylist:
		if isinstance(i,list):
			my_print(i)
		else:
			print(i)
		
>>> my_print(Fruit)

Apple
1
Pear
2
Bananer
3
"Tomato"
A
B
C
aa
bb
cc
```


定义个递归函数实现，看起来好多了。


<br>

<br>

列表操作符部分，+表示列表组合，*表示列表重复：

```python
>>> mylist = [1,2,3] + [4,5,6]
>>> print mylist
[1, 2, 3, 4, 5, 6]

>>> mylist = mylist*4
>>> print(mylist)
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

```

<br>

今天就写到这里吧。

