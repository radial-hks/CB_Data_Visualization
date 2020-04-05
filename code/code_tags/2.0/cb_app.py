import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import crawl_data
import os
import setting
import plotly_express as px
import plotly.graph_objs as go
# 回调函数
from dash.dependencies import Input, Output  

""" 数据收集及存储 """

# 初始化类
# spider = crawl_data.Spiders()
# spider.crawl_storage()

""" 数据读取及预处理 """
# 读取最新数据
path = setting.DATA_PATH
file = os.listdir(path)[-1]
data = pd.read_csv(path + str(file)) 

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
df.loc[:,'转债名称'] = df['转债名称'].apply(lambda x:x[:2])
df.loc[:,'转股溢价率'] = df['转股溢价率'].apply(percent_)
df.loc[:,"税前收益率"] = df["税前收益率"].apply(percent_)
df.loc[:,"回售年限"] = df["回售年限"].apply(to_days)
df.loc[:,"税前回售收益"] = df["税前回售收益"].apply(percent_)
df.loc[:,'信用'] = df['信用'].apply(credit)

# 更换columns
df.columns = new_columns

gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")

""" 数据展示 """

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

text_notes = '''
### Dash和Markdown
投资需谨慎哦
如果这是你对Markdown的第一次介绍，请查看他们的[60 Second Markdown Tutorial](http://commonmark.org/help/)！
'''

app.layout = html.Div(children=[
    # 二级标题
    html.H1(children='可转债数据可视化'),
    # 临时添加散点图
    dcc.Graph(
        figure={
            'data': [
                dict(
                    x=df["bond_price"] ,
                    y=df["to_stock_premium_rate"],
                    text=df["bond_name"],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                ) 
            ],
            'layout': dict(
                # title = 'Dash数据可视化',
                margin = {'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend = dict(x = 0, y = 1),
                width = 800,
                height = 800,
            )
        }
    ),
    # 柱状图
    dcc.Graph(
        figure = go.Figure(
            data=[go.Bar(y=[2, 1, 3])],
            layout_title_text="A Figure Displayed with the 'png' Renderer")
    ),
    # 散点图
    dcc.Graph(
        figure = px.scatter(
                    # X字段
                    df,
                    x = "bond_price",
                    y = "to_stock_premium_rate",
                    size = [5 for i in df["to_stock_premium_rate"]],
                    color= "credit",
                    hover_name = "bond_name",
                    width = 800,
                    height = 800,
                    color_continuous_scale=px.colors.sequential.Burg,
                    template='seaborn',
                    title =  "可转债散点图",),
    ),
    # markdown
    dcc.Markdown(children=text_notes),
])

if __name__ == '__main__':
    app.run_server(debug=True)