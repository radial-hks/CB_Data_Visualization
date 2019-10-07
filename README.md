# CB_Data_Visualization

[富投网](http://www.richvest.com/index.php?m=cb&amp;a=cb_all) 

**可转债数据收集及可视化小工具,大佬带带我。(满足时时交互体验)**

![行情全表](https://i.loli.net/2019/10/05/Gw2O61mvfnlpryW.png)

**免责声明： 1、以上数据由富投网采集整理，富投网力求数据的客观公正性，但不对数据本身的准确性及完整性做出保证。 2、富投网的数据不构成任何决策依据，本网站对访问者参考本网站数据所引发的任何直接或间接损失概不负责**

## 一、数据收集

*说实话,真的很想吐槽这个表格的前端,什么破命名规则。*

但是使用`requests`与`lxml`将表格的数据提取出来了,虽然历经坎坷,但是...

[requests : 数据请求 ](https://github.com/psf/requests)  

[lxml : HTMl文档解析 ](https://github.com/lxml/lxml)


![数据收集](https://i.loli.net/2019/10/05/gXAO6lnK3QcIaxb.png)


## 二、数据预处理

*数据简单的整理、清洗及存储*



[Pandas : 超级无敌好用的数据处理库 ](https://pandas.pydata.org/pandas-docs/stable/genindex.html)

![本地化存储预览](https://i.loli.net/2019/10/06/dxusvfkUliX9RtV.png)



## 三、数据可视化

*此阶段将会是最挑战及趣味性的阶段,可视化,来啦*



[Matplotlib : 绘制图形（入门）](https://matplotlib.org/gallery/index.html)

![](https://matplotlib.org/_images/sphx_glr_csd_demo_001.png)

[Seaborn : 绘制更加漂亮的图形 ](http://seaborn.pydata.org/)

![](http://seaborn.pydata.org/_images/introduction_29_0.png)

[Bokeh : 绘制可交互的图形 ](https://bokeh.pydata.org/en/latest/)


![](https://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/images/bokeh-header.png)


### 问题及解决方法

#### 1、在图形中绘制大小不同的子图？？（之前是使用`ax1 = fig.add_subplot(2,1,1)`绘制出来的都是整整齐齐的）

* 直达[`gridspec`](https://matplotlib.org/tutorials/intermediate/gridspec1.html)出现,子图的布局被安排的明明白白。
* [代码展示](https://matplotlib.org/tutorials/intermediate/gridspec1.html):
```python

fig1 = plt.figure(constrained_layout=True)
spec1 = gridspec.Gridspec1(ncols=2, nrows=2, figure=fig)
f2_ax1 = fig.add_subplot(spec1[0, 0])
f2_ax2 = fig1.add_subplot(spec1[0, 1])
f2_ax3 = fig1.add_subplot(spec1[1, 0])
f2_ax4 = fig1.add_subplot(spec1[1, 1])

""" 以上代码效果与下列效果相同 """

fig2 = plt.figure(figsize=(10,6),facecolor = 'white')

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

""" 但是可以这样操作 """
fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)
f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax1.set_title('gs[0, :]')
f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('gs[-1, 0]')
f3_ax5 = fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')
```
绘制结果:

![](https://matplotlib.org/_images/sphx_glr_gridspec_002.png)

![](https://matplotlib.org/_images/sphx_glr_gridspec_003.png)

到此我的第一个困难解决了~~~~

#### 2、散点图绘制详解

