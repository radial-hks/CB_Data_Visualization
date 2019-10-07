import requests
import pandas as pd
import numpy as np
from lxml import etree
import setting


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
        try:
            if  "GET HTML(出现错误)" != demo:
                html =  etree.HTML(demo)
                data_pool =  []
                for i in html.xpath('//tbody/tr'):
                    x,y,z = 0,0,0
                    # 跟换一种思路来讲就是  -->  如果 td 之下存在子孙节点,直接使用子孙节点;否则使用自身节点 
                    #  x 
                    if  len(i.xpath("./td[9]/font/text()")) == 0:
                        x = i.xpath("./td[9]/text()")[0]
                    else :
                        x = i.xpath("./td[9]/font/text()")[0]
                    # y 
                    if  len(i.xpath("./td[10]/font/text()")) == 0:
                        y = i.xpath("./td[10]/text()")[0]
                    else :
                        y = i.xpath("./td[10]/font/text()")[0]
                    #  z
                    if len(i.xpath("./td[12]/font/text()")) == 0:
                        z = i.xpath("./td[12]/text()")[0]
                    else:
                        z = i.xpath("./td[12]/font/text()")[0] 
                    
                    """ 先判断时候有子孙节点 """
                    
                    data = [
                        i.xpath("./td[1]//text()")[0],
                        i.xpath("./td[2]//text()")[0],
                        i.xpath("./td[3]//text()")[0],
                        i.xpath("./td[4]//text()")[0],
                        i.xpath("./td[5]//text()")[0],
                        i.xpath("./td[6]//text()")[0],
                        i.xpath("./td[7]//text()")[0],
                        #  9.10.12 需要及时调整及判断
                        i.xpath("./td[8]//text()")[0],
                        # i.xpath("./td[9]//text()")[0],
                        # i.xpath("./td[10]//text()")[0],
                        x,y,
                        i.xpath("./td[11]//text()")[0],
                        z,
                        # i.xpath("./td[12]//text()")[0],
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
                        i.xpath("./td[45]//text()")[0]]
                    
                    data_pool.append(data)
                return  data_pool
            else :
                return  "GET HTML B (失败)"
        except :
            return "PARSE HTMl (出现错误)"
    
    def afford_help(self,cell):
        """ 
        辅助datalean 进行数据清洗  
        -  替换 回售中、转股中、无权等废标量数据 
        -  删除年
        -  删除 % > <
        """
        if "回售中" in cell or "转股中" in cell or "无权" in cell:
            return  str(0)
        elif "年" in cell or "天" in cell :
            return  cell.replace("年",'').replace("天",'')
        else:
            return  cell.replace("%","").replace(" ","").replace(">","").replace("<","")

    def clean_data(self,data_):
        ''' 
        
        简单的数据清洗 
        
        
        '''
        head = ["序号","转债名称","转债代码","股票日期","股票名称","股票代码","所属行业","转债价格","涨跌_1",
        "盘中套","股价","涨跌_2","转债成交额","转债换手率","转股价格","P/B","股价/转股价","转股价格","转股溢价率",
        "距离转股日","剩余年限","回售年限","余额/市值","余额/股本","转债余额","税前收益率","税后收益率",
        "加权收益率","税前回售收益","税后回售收益","回售价值","纯债价值","期权价值","内在价值","价值溢价",
        "历史波动","隐含波动","预测波动","弹性","涨修正弹","跌修正弹","信用","折现率","热门度","转债名称_"]

        data  = pd.DataFrame(np.array(data_),columns = head)
        #  删除序号
        data.drop(["序号","转债名称_"],axis = 1,inplace = True)

        #  开始数据清洗
        for i in data.columns:
            # 删除多余参数
            data[i] = data[i].apply(self.afford_help)
            # 数据类型转换(排除 需记你一步处理的列 )
            if i not in ["转债名称","股票日期","股票名称","所属行业","距离转股日","信用"]:
                data[i].astype(np.float)
            #  转换为数据格式
            if i == "股票日期":
                data[i] = pd.to_datetime(data["股票日期"])           
            # 数据标量化
            if i ==  "距离转股日":
                med =  data[i].str.split("月")
                for x in med.index:
                    if  len(med[x]) == 2:
                        med[x] = float(med[x][0])*30 + float(med[x][1])
                    else :
                        med[x] = float(med[x][0])
                data[i] = med
            # 数据表量化 （AAA+ --> 375）
            if i ==  "信用":
                med =  data[i].str.split("")
                for x in med.index:
                    num = len(med[x])
                    if  '+' in med[x]:
                        med[x] = (num -2) * 100 + 75
                    elif '-' in med[x]:
                        med[x] = (num -2) * 100 + 25
                    else:
                        med[x] = (num -2) * 100
                data[i] = med
        return data

    def storage_data(self,data,path = setting.PATH):
        """
        数据预览及存储
        - 默认存储
        """
        name = str(pd.datetime.now())
        try:
            data.to_csv(path+name+".csv",index = False)
            return  "T"
        except :
            return "F"


# 初始化类
spider = spiders()

# 获取数据并解析 
data = spider.parse_html()
# 数据简单清洗h及存储
data_clean = spider.clean_data(data)
spider.storage_data(data_clean)