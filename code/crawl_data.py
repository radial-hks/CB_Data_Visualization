
#%%
import requests
import re
import pandas as pd
from lxml import etree


class spiders():
    def __init__(self):
        # 使用默认地址为富投网行情全表
        self.url = r"http://www.richvest.com/index.php?m=cb&a=cb_all"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        

    def get_html(self):
        ''' 模拟请求数据 '''
        try:
            res = requests.get(self.url,headers=self.headers)
            res.raise_for_status()
            res.encoding = res.apparent_encoding
            return res.text
        except :
            return "GET HTML A (出现错误)"

    def parse_html(self):
        '''  使用lxml解析HTML '''
        demo = self.get_html()
        # try:
        if  "GET HTML(出现错误)" != demo:
            html =  etree.HTML(demo)
            data_pool =  []
            for i in html.xpath('//tbody/tr'):
                print(i.xpath("./td[@class = 'cb_name_id']/text()")[0],)
                
                # 第二组必须存在(添加到下列列表中)
                try :
                    x = i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[0]
                    y =  i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[1]
                except :
                    x = i.xpath("./td[@class = 'cb_mov2_id']/text()")[0]
                    y =  i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[0]
                """ 先判断时候有子孙节点 """
                data = [
                    i.xpath("./td[@class = 'cb_num_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_name_id']/text()")[0],
                    i.xpath("./td[@class = 'bond_code_id bond_code']/text()")[0],
                    i.xpath("./td[@class = 'bond_date_id']/text()")[0],
                    i.xpath("./td[@class = 'stock_name_id stock_name']/text()")[0],
                    i.xpath("./td[@class = 'bond_code_id stock_code']/text()")[0],
                    i.xpath("./td[@class = 'bond_code_id industry']/text()")[0],
                    i.xpath("./td[@class = 'cb_price2_id']/text()")[0],
                    # 注意添加条件判断
                    x,y,
                    i.xpath("./td[@class = 'stock_price_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_mov_id']/font/text()")[0],
                    i.xpath("./td[@class = 'cb_trade_amount_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_trade_amount_id']/text()")[1],
                    i.xpath("./td[@class = 'cb_strike_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_elasticity_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_stockOverCB_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_premium_id']/text()")[0],
                    i.xpath("./td[@class = 'cb_t_id ']/text()")[0],
                    i.xpath("./td[@class = 'cb_t_id bond_t bond_t1']/text()"),
                    i.xpath("./td[@class = 'cb_t_id red_t']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id cb_to_share']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id cb_to_share_shares']/text()")[0],
                    i.xpath("./td[@class = 'stock_price_id remain_amount']/text()")[0],
                    i.xpath("./td[@class = 'cb_BT_id BT_yield']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id AT_yield']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id wa_yield']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id BT_red']/text()")[0],
                    i.xpath("./td[@class = 'cb_AT_id AT_red']/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id npv_red']/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id npv_value']/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id option_value']/a/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id']/a/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id']/a/text()")[1],
                    i.xpath("./td[@class = 'cb_value_id']/text()")[1],
                    i.xpath("./td[@class = 'cb_value_id vola_implied']/text()")[0],
                    i.xpath("./td[@class = 'cb_value_id vola_est']/text()")[0],
                    i.xpath("./td[@class = 'cb_elasticity_id elasticity']/text()")[0],
                    i.xpath("./td[@class = 'cb_elasticity_id elasticity_adj_up']/text()")[0],
                    i.xpath("./td[@class = 'cb_elasticity_id elasticity_adj_down']/text()")[0],
                    i.xpath("./td[@class = 'bond_rating_id rating']/text()")[0],
                    i.xpath("./td[@class = 'bond_rating_id discount_rate']/text()")[0],
                    i.xpath("./td[@class = 'cb_elasticity_id']/text()")[1],
                    i.xpath("./td[@class = 'cb_name_id']/text()")[1],
                    ]
                data_pool.append(data)
            return  data_pool
        else :
            return  "GET HTML B (失败)"
        # except :
        #     return "PARSE HTMl (出现错误)"
    
    def data_clean(self,pool_data):
        ''' 简单的数据清洗及存储 '''
        head = [
        "序号","转债名称","转债代码","股票日期","股票名称","股票代码","所属行业","转债价格","涨跌",
        "盘中套","股价","涨跌","转债成交额","转债换手率","转股价格","P/B","股价/转股价","转股溢价率",
        "距离转股日","剩余年限","回售年限","余额/市值","余额/股本","转债余额","税前收益率","税后收益率",
        "加权收益率","税前回售收益","税后回售收益","回售价值","纯债价值","期权价值","内在价值","价值溢价",
        "历史波动","隐含波动","预测波动","弹性","涨修正弹","跌修正弹","信用","折现率","热门度","转债名称"]
        data =  pd.DataFrame(pool_data)
        # data.columns = head
        return  data

#%%

spider = spiders()
spider.parse_html()

#%%
