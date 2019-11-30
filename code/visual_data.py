import crawl_data
import os
import setting
import pandas as pd
from bokeh.plotting import figure 
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.palettes import Viridis256
from bokeh.models.annotations import Span



""" 数据收集及存储 """

# 初始化类
spider = crawl_data.Spiders()

# 获取数据并解析 
data = spider.parse_html()
# 数据简单清洗及存储
data_clean = spider.clean_data(data)
spider.storage_data(data_clean)


""" 数据读取及预处理 """
# 读取最新数据
path = setting.DATA_PATH
file = os.listdir(path)[-1]
data = pd.read_csv(path + str(file)) 
# 截取数据
# 选取需要展示的数据字段
old_columns = [
    '转债名称',
    '转债代码',
    '股票名称',
    '股票代码',
    '所属行业',
    '转债价格',
    '股价',
    '转股价格',
    '转股价值',
    '转股溢价率',
    '价值溢价', 
    '信用',   
]

new_columns = [
    'bond_name',
    'bond_code',
    'stock_name',
    'stock_code',
    'industry',
    'bond_price',
    'stock_price',
    'to_stock_price',
    'to_stock_value',
    'to_stock_premium_rate',
    'value_premium', 
    'credit',   
]
# 重命名
df =  data[old_columns]
df.columns = new_columns


""" 数据展示 """
# 传入DataFrame数据
source = ColumnDataSource(df)

# 图形配置文件
options = dict(plot_width=600, plot_height=400,
               tools="pan,wheel_zoom,box_zoom,box_select,lasso_select")
TOOLTIPS = [
    ("index", "@index"),
    ("转债名称", "@bond_name"),
    ("转债代码", "@bond_code"),
    ("转债价格","@bond_price"),
    ("行业","@industry"),
]


# 信用色彩
color_mapper = LinearColorMapper(palette=Viridis256, low=df["credit"].min(), high=df["credit"].max())
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, location=(0,0), title='Weight')

# 转债价格与股价
p1 = figure(title="转债价格-股价",tooltips=TOOLTIPS,**options)
p1.circle("bond_price", "stock_price", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p1.add_layout(color_bar, 'right')

# 添加参线:https://nbviewer.jupyter.org/github/gafeng/bokeh-notebooks/blob/master/tutorial/03%20-%20Adding%20Annotations.ipynb
upper = Span(location=100, dimension='height', line_color='green', line_width=1)
p1.add_layout(upper)

# 转债价格与转股价格
p2 = figure(title="转债价格-转股价格",tooltips=TOOLTIPS,**options)
p2.circle("bond_price", "to_stock_price", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p2.add_layout(color_bar, 'right')

# 转股价值与转股溢价率
p3 = figure(title="转股价值-转股溢价率",tooltips=TOOLTIPS,**options)
p3.circle("to_stock_value", "to_stock_premium_rate", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p3.add_layout(color_bar, 'right')
# 转股价值与价值溢价
p4 = figure(title="转股价值-价值溢价",tooltips=TOOLTIPS,**options)
p4.circle("to_stock_value", "value_premium", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p4.add_layout(color_bar, 'right')

p = gridplot([[p1,p2], [p3,p4]], toolbar_location="right")
# p.add_layout(color_bar, 'right')
show(p)