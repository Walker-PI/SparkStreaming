# SparkStreaming

### 目标
使用scraping.py 爬去codeforces上所有题目，利用SparkStreaming 做热门算法统计，结果用柱状图/圆饼图展示。

不是使用Scala语言，而是使用pysprak

### 环境准备
ubuntu18.04 搭建Spark集群
python3.6
jupyter notebook

### 执行步骤
在jupyter中运行HotAlgorithms.ipynb  
然后在Ubuntu18.04  本文件目录下执行终端指令 python3 write_data.py  
动态变化的柱状图/圆饼图就会出现在jupyter中

### 结果展示

#### 柱状图  

![histogram.png](https://i.loli.net/2019/10/13/wQzIWi9RvpXCZE3.png)

#### 圆饼图

![pieChart.png](https://i.loli.net/2019/10/13/C1m2TZJI9fsgGbz.png)

