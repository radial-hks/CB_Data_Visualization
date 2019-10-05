def parse_html(self):
        '''  使用lxml解析HTML '''
        demo = self.get_html()
        # try:
        if  "GET HTML(出现错误)" != demo:
            html =  etree.HTML(demo)
            data_pool =  []
            for i in html.xpath('//tbody/tr'):
                
                # 第二组必须存在(添加到下列列表中)
                try :
                    x = i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[0]
                    y =  i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[1]
                except :
                    x = i.xpath("./td[@class = 'cb_mov2_id']/text()")[0]
                    y =  i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[0]



                # 跟换一种思路来讲就是  -->  如果 td 之下存在子孙节点,直接使用子孙节点;否则使用自身节点 
                if len(i.xpath("./td[@class = 'cb_mov2_id']/child::*")):
                    x = i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[0]
                    y =  i.xpath("./td[@class = 'cb_mov2_id']/font/text()")[1]
                else :
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


def parse_html(self):
        '''  使用lxml解析HTML '''
        demo = self.get_html()
        # try:
        if  "GET HTML(出现错误)" != demo:
            html =  etree.HTML(demo)
            data_pool =  []
            for i in html.xpath('//tbody/tr'):
                """ 先判断时候有子孙节点 """
                data = [
                    i.xpath("./td[1]//text()")[0],
                    i.xpath("./td[2]//text()")[0],
                    i.xpath("./td[3]//text()")[0],
                    i.xpath("./td[4]//text()")[0],
                    i.xpath("./td[5]//text()")[0],
                    i.xpath("./td[6]//text()")[0],
                    i.xpath("./td[7]//text()")[0],
                    i.xpath("./td[8]//text()")[0],
                    i.xpath("./td[9]//text()")[0],
                    i.xpath("./td[10]//text()")[0],
                    i.xpath("./td[11]//text()")[0],
                    i.xpath("./td[12]//text()")[0],
                    i.xpath("./td[13]//text()")[0],
                    i.xpath("./td[14]//text()")[0],
                    i.xpath("./td[15]//text()")[0],
                    i.xpath("./td[16]//text()")[0],
                    i.xpath("./td[17]//text()")[0],
                    i.xpath("./td[18]//text()")[0],
                    i.xpath("./td[19]//text()")[0],
                    i.xpath("./td[20]//text()")[0],
                    i.xpath("./td[21]//text()")[0],
                    i.xpath("./td[22]//text()")[0],
                    i.xpath("./td[23]//text()")[0],
                    i.xpath("./td[24]//text()")[0],
                    i.xpath("./td[25]//text()")[0],
                    i.xpath("./td[26]//text()")[0],
                    i.xpath("./td[27]//text()")[0],
                    i.xpath("./td[28]//text()")[0],
                    i.xpath("./td[29]//text()")[0],
                    i.xpath("./td[30]//text()")[0],
                    i.xpath("./td[31]//text()")[0],
                    i.xpath("./td[32]//text()")[0],
                    i.xpath("./td[33]//text()")[0],
                    i.xpath("./td[34]//text()")[0],
                    i.xpath("./td[35]//text()")[0],
                    i.xpath("./td[34]//text()")[0],
                    i.xpath("./td[37]//text()")[0],
                    i.xpath("./td[38]//text()")[0],
                    i.xpath("./td[39]//text()")[0],
                    i.xpath("./td[40]//text()")[0],
                    i.xpath("./td[41]//text()")[0],
                    i.xpath("./td[42]//text()")[0],
                    i.xpath("./td[43]//text()")[0],
                    i.xpath("./td[44]//text()")[0],
                    i.xpath("./td[45]//text()")[0], 
                ]
                data_pool.append(data)
            return  data_pool
        else :
            return  "GET HTML B (失败)"
        # except :
        #     return "PARSE HTMl (出现错误)"