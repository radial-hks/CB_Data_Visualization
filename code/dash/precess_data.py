import pandas as pd
import setting
import crawl_data


""" 数据爬取类实例化  """
spider = crawl_data.Spiders()

""" 预设的处理函数及数据"""
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
# 数据处理模块
class  Precess():
    def __init__(self):
        self.path = setting.DATA_PATH
        # 返回解析网页数据 (暂时没有容错机制)
        self.data = spider.parse_html()
        # 直接执行没毛病
        self.precess_data()

    def precess_data(self):
        """接续制定字段数据及预处理"""
        self.data = self.data[old_columns]
        # 数据转化
        self.data.loc[:,'转债名称'] = self.data['转债名称'].apply(lambda x:x[:2])
        self.data.loc[:,'转股溢价率'] = self.data['转股溢价率'].apply(percent_)
        self.data.loc[:,"税前收益率"] = self.data["税前收益率"].apply(percent_)
        self.data.loc[:,"回售年限"] = self.data["回售年限"].apply(to_days)
        self.data.loc[:,"税前回售收益"] = self.data["税前回售收益"].apply(percent_)
        #  信用登记保留原始字符串标记
        self.data.loc[:,'信用'] = self.data['信用'].apply(credit)
        # 更换columns
        self.data.columns = new_columns

    def get_data(self):
        """ 获取解析数据 """
        return  self.data

    def reboot(self):
        """ 获取进行数据爬取 """
        # 返回解析网页数据 (暂时没有容错机制)
        self.data = spider.parse_html()
        # 直接执行没毛病
        self.precess_data()
        # print("爬取成功！！！")

