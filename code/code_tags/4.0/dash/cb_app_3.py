import pandas as pd
import numpy as np
import precess_data
import crawl_data
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly_express as px
import plotly.graph_objects as go
# 回调函数
from dash.dependencies import Input, Output  


""" 数据爬取类实例化  """
# 基金数据
spider = crawl_data.Spiders()
fund_data = spider.get_zs_data()

# 可转债数据
cb_data = precess_data.Precess()
df = cb_data.get_data()

""" 数据展示 """ 
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

# 网页模板
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>可转债数据可视化 - radial</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# 生成数据表格
def generate_table(data):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in ["名称","代码","现价","净估值","溢价率(%)"]])
        ),
        html.Tbody([
            html.Tr([
                html.Td(i) for i in data
            ])
        ])
    ])

app.layout = html.Div(children=[
    html.H1(id="intro",children="可转债数据可视化"),
    html.Div(
        # 对应选项及动作
        id = "zero",
        children=[
            dcc.ConfirmDialogProvider(
                children=html.Button('点击更新数据',),
                id='danger-danger-provider',
                message="点击更新为最新数据",
        ),
        html.Div(id='output-provider'),
        html.P(id="text",children=["免责声明： 1、以上数据由富投网采集整理，富投网力求数据的客观公正性，但不对数据本身的准确性及完整性做出保证。\n 2、富投网的数据不构成任何决策依据，本网站对访问者参考本网站数据所引发的任何直接或间接损失概不负责"]),
        ]),
        
    html.Div(
            id = "one",
            children=[
                html.H3("转债价格-转股溢价率"),
                # 税前回售收益率
                dcc.Graph(
                    id = 'to_stock_premium_rate',
                )
            ]),
    html.Div(
            id = "two",
            children=[
                html.H3("转债价格-到期收益率"),
                # 税前回售收益率
                dcc.Graph(
                    id = 'income_before_taxes_rate',
                )
            ]),
    html.Div(
            id = "three",
            children=[
                html.H3("回售年限-税前回售收益率"),
                # 税前回售收益率
                dcc.Graph(
                    id = 'income_tosell_before_taxes',
                )
            ]),
    html.Div(
            id = "four",
            children=[
                html.H3("基金债券数据"),
                # 基金数据
                html.Div(id="fund_data",children=[generate_table(fund_data)]) 
            ]),
])


# 新加默认选择器


# 根据对应的的标题返回数据提示模板
def get_hover_template(title):
    """ 
    图表的标题名称 --> 返回对应的模板文件
    - 图片的xy字段名称
    - return 返回为 hovertemplate
    - 注意: To hide the secondary box completely, use an empty tag `<extra></extra>`.
    - 参考链接: https://community.plotly.com/t/remove-trace-0-next-to-hover/33731
    """
    string = ""
    if title == "转债价格-转股溢价率(%)":
        string  = "%{text}转债: <br>转债价格(元) : %{x} <br> 转股溢价率(%) : %{y} <extra></extra> "
    elif title == "转债价格-到期收益率(%)":
        string  = "%{text}转债: <br>转债价格(元) : %{x} <br> 到期收益率(%) : %{y}  <extra></extra> "
    else: 
        string  = "%{text}转债: <br>回售年限(天) : %{x} <br> 税前回售收益率(%) : %{y}  <extra></extra> "
    return string 

# 绘制对应的图形
# TODO: 图片尺寸 + 默认选择器 + 添加特定的颜色标识 + 坐标轴设置
def get_figure(data,x,y,title,selectedpoints):
    # 生成图形对象
    fig = go.Figure(
        go.Scatter(
            x = df[x],
            y = df[y],
            text=df["bond_name"],
            hovertemplate = get_hover_template(title), 
            # 'textposition': 'top',
            selectedpoints=selectedpoints,
            # 设置对应的主键数据
            customdata= df.index,
            # 'type': 'scatter',
            mode = "markers",
            ))
    # 新增对应的配置
    fig.update_traces(marker=dict(size=12,
                                color = df["credit"],
                                colorscale = 'Viridis',
                                showscale=True,
                                line=dict(width=1.5,color='DarkSlateGrey')),
                    selector=dict(mode='markers'), 
                    #  未选中的点的配色
                    unselected = {'marker': {'opacity': 0.2 }})
    
    fig.update_layout(
        # 数据信息显示的位置
        hoverlabel_align = 'right',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.5)',
        autosize = True,
        # margin= {'l': 20, 'r': 0, 'b': 20, 't': 5},
        margin= {"autoexpand":True},
        ),
    
    # 显示及控件配置
    # fig.show(config={
    #                 'modeBarButtonsToRemove': ['toggleSpikelines','hoverCompareCartesian']
    #             })
    return fig



@app.callback(
    [Output('to_stock_premium_rate', 'figure'),
    Output('income_before_taxes_rate', 'figure'),
    Output('income_tosell_before_taxes', 'figure')],
    [Input('to_stock_premium_rate', 'selectedData'),
    Input('income_before_taxes_rate', 'selectedData'),
    Input('income_tosell_before_taxes', 'selectedData')]
)
def callback(selection1, selection2, selection3):
    # 获取原始数据INDEX
    selectedpoints = df.index
    for selected_data in [selection1, selection2, selection3]:
        # 筛选数据及其内部值存在
        if selected_data and selected_data['points']:
            selectedpoints = np.intersect1d(selectedpoints,
                [p['customdata'] for p in selected_data['points']])

    return [get_figure(df, "bond_price", "to_stock_premium_rate", "转债价格-转股溢价率(%)",selectedpoints),
            get_figure(df, "bond_price", "income_before_taxes_rate", "转债价格-到期收益率(%)",selectedpoints),
            get_figure(df, "back_to_sell_years", "income_tosell_before_taxes", "回售年限(天)-税前回售收益率(%)",selectedpoints)]


# 点击按钮更新数据
@app.callback(Output('output-provider', 'children'),
            [Input('danger-danger-provider', 'submit_n_clicks')])
def update_output(submit_n_clicks):
    global df,fund_data
    if not submit_n_clicks:
        return ''
    else:
        # 重新爬取数据(债券基金)
        fund_data = spider.get_zs_data()
        # 重新进行数据爬取(可转债数据)
        cb_data.reboot()
        df = cb_data.get_data()
    return """
        It was dangerous but we did it!
        Submitted {} times,victory.
    """.format(submit_n_clicks)



if __name__ == '__main__':
    app.run_server(port=5000,host="0.0.0.0")
    # app.run_server(debug=True)
