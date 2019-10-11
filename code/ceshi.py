#%%
import numpy as np 
import pandas as pd 

#%%
# 生成6000条数据 
data = np.random.randint(-100,100,[10000,2])

data_ = pd.DataFrame(data,columns=["实验","求和"])

data_["all"] =  0

data_["all"][data_["实验"]>0] = 1
data_["all"][data_["实验"]<0] = -1

data_["求和"] = np.cumsum(data_["all"])

#print(data_["求和"][999]/10000)

plt.plot(data_.index,data_["求和"])
plt.xlabel('Number of throwing coin')
plt.ylabel('Positive upward probability')
plt.title('Probability of positive head-up as the number of tossed coins increases')
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt
import random

'''
用代码实现抛掷硬币N次后,观察正面向上的概率随着抛掷次数的变化
'''

# 定义做500次试验,每次抛掷10 * n次,即,每次抛掷硬币10, 20,30...
batch = 50
samples = [10 * i for i in range(1, batch + 1)]
result = []
result_mean = []

# 统计每批试验正面向上的概率
for _ in range(batch):
    for i in range(samples[_]):
        result.append(random.randint(0, 1))

    result_mean.append(np.mean(result))
xaxis = list(range(batch))

plt.plot(xaxis, result_mean)
plt.xlabel('Number of throwing coin')
plt.ylabel('Positive upward probability')
plt.title('Probability of positive head-up as the number of tossed coins increases')
plt.show()



