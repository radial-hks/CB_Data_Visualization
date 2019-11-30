# CB_Data_Visualization

[富投网](https://i.loli.net/2019/11/30/WruF6enGmL9oH5t.png)

**可转债数据收集及可视化小工具,大佬带带我。(满足时时交互体验)**

![行情全表](https://i.loli.net/2019/10/05/Gw2O61mvfnlpryW.png)

**免责声明： 1、以上数据由富投网采集整理，富投网力求数据的客观公正性，但不对数据本身的准确性及完整性做出保证。 2、富投网的数据不构成任何决策依据，本网站对访问者参考本网站数据所引发的任何直接或间接损失概不负责**

## 使用方法

```python
# 切换到工作路径后执行代码
python visual_data.py
```
**注意：运行环境准备`requests`,`pandas`及`bokeh`等第三方库**


## 一、数据收集

*说实话,真的很想吐槽这个表格的前端,什么破命名规则。*

但是使用`requests`与`lxml`将表格的数据提取出来了,虽然历经坎坷,但是...

[requests : 数据请求 ](https://github.com/psf/requests)  

[lxml : HTMl文档解析 ](https://github.com/lxml/lxml)

![数据收集](https://i.loli.net/2019/11/30/RtIUnaAYJT1PvWu.png)


## 二、数据预处理

*数据简单的整理、清洗及存储*

[Pandas : 超级无敌好用的数据处理库 ](https://pandas.pydata.org/pandas-docs/stable/genindex.html)


## 三、数据可视化

*此阶段将会是最挑战及趣味性的阶段,可视化,来啦*

[Bokeh : 绘制可交互的图形 ](https://bokeh.pydata.org/en/latest/)

[Bokeh 教程](https://nbviewer.jupyter.org/github/gafeng/bokeh-notebooks/tree/master/tutorial/)

![](https://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/images/bokeh-header.png)

**结果展示**

![结果展示](https://i.loli.net/2019/11/30/RXsPxSdhCirk3D8.png)


## 四、大佬带带我

* 作为新手,对于可转债的理解不足,因此作出来的工具不是很好,请多多指正;
* 入手可转债的新手或多年的老手,希望你们能多提提建议,改善工具；
* 最后，还要说一句:大佬，带带我！！！


**程序的功能将进一步完善,敬请期待**

