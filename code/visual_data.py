import crawl_data
import os
import setting
import pandas as pd
from bokeh.plotting import figure 
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.transform import factor_cmap
from bokeh.palettes import Viridis256
from bokeh.models.annotations import Span



""" 数据收集及存储 """

# 初始化类
spider = crawl_data.Spiders()
spider.crawl_storage()



""" 数据读取及预处理 """
# 读取最新数据
path = setting.DATA_PATH
file = os.listdir(path)[-1]
data = pd.read_csv(path + str(file)) 
# 截取数据

# 选取需要展示的数据字段
old_columns = [
    '转债名称',
    '转债价格',
    '转股溢价率',
    "税前收益率", 
    "回售年限",
    "税前回售收益",
    '信用'
]

new_columns = [
    'bond_name',
    'bond_price',
    'to_stock_premium_rate',
    'income_before_taxes_rate',
    'back_to_sell_years',
    'income_tosell_before_taxes',
    'credit',  
]

def to_days(x):
    """ 回售年限 """
    x = str(x)
    if "回售中" in x:
        return  float(0)
    elif "无权" in x:
        return float(6)
    else:
        if "天" in x:
            med = x[0:-1]
            if "年" in med:
                med_list = med.split("年")
                year = float(med_list[0])
                day = float(med_list[1])
                return year*365 + day
            else:
                return float(med)
        else:
            try:
                return float(x[:-1])*365
            except:
                return float(0)

def credit(x):
    """ 信用等级 """
    print(x)
    num = len(x)
    if  '+' in x:
        res = (num -1) * 100 + 75
    elif '-' in x:
        res = (num -1) * 100 + 25
    else:
        res = num * 100 + 50
    return res

def percent_(x):
    """ 百分比 """
    x  = str(x)
    if "回售中" in x or "无" in x:
        return 0
    else:
        try:
            return float(x[0:-1])
        except:
            return 0


# 截取数据
df =  data[old_columns]

# 数据转化
df.loc['转股溢价率'] = df['转股溢价率'].apply(percent_)
df.loc["税前收益率"] = df["税前收益率"].apply(percent_)
df.loc["回售年限"] = df["回售年限"].apply(to_days)
df.loc["税前回售收益"] = df["税前回售收益"].apply(percent_)
df.loc['信用'] = df['信用'].apply(credit)

df.columns = new_columns


""" 数据展示 """
# 传入DataFrame数据
source = ColumnDataSource(df)

# 图形配置文件
options = dict(plot_width=600, plot_height=400,x_axis_label="回售年限",y_axis_label= "税前回售收益率",
               tools="pan,wheel_zoom,box_zoom,box_select,reset")
TOOLTIPS = [
    # ("index", "@index"),
    ("转债名称", "@bond_name"),
    ('转股溢价率(%)','@to_stock_premium_rate'),
    ("税前收益率(%)", '@income_before_taxes_rate'),
    ("回售天数(天)",'@back_to_sell_years'),
    ("税前回售收益(%)",'@income_tosell_before_taxes'), 
    ('信用','@credit'),
]

# 信用色彩
color_mapper = LinearColorMapper(palette=Viridis256, low=df["credit"].min(), high=df["credit"].max())
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, location=(0,0), title='Weight')

# 转债价格与股价
p1 = figure(title="转债价格-转股溢价率",tooltips=TOOLTIPS,**options)
p1.circle("bond_price", 'to_stock_premium_rate', color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p1.add_layout(color_bar, 'right')

# 添加参线:https://nbviewer.jupyter.org/github/gafeng/bokeh-notebooks/blob/master/tutorial/03%20-%20Adding%20Annotations.ipynb
upper = Span(location=100, dimension='height', line_color='green', line_width=1)
p1.add_layout(upper)

# 转债价格与转股价格
p2 = figure(title="转债价格-到期收益率",x_range=p1.x_range,y_range=p1.y_range,tooltips=TOOLTIPS,**options)
p2.circle("bond_price", 'income_before_taxes_rate', color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
p2.add_layout(color_bar, 'right')

# 转股价值与转股溢价率
p3 = figure(title="回售年限-税前回售收益率",tooltips=TOOLTIPS,**options)
p3.circle('back_to_sell_years', "income_tosell_before_taxes", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
# p3.add_layout(color_bar, 'right')

# 转股价值与价值溢价
# p4 = figure(title="转股价值-价值溢价",tooltips=TOOLTIPS,**options)
# p4.circle("to_stock_value", "value_premium", color={'field': 'credit', 'transform': color_mapper}, size=10, alpha=0.6,source=source)
# p4.add_layout(color_bar, 'right')

p = gridplot([[p1,p2], [p3,None]], toolbar_location="right")
# p.add_layout(color_bar, 'right')
show(p)