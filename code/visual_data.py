#%%
import pandas as pd 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

# from setting import *

#%% 
# 导入数据
data =  pd.read_csv(r"./"+"2019-10-07 14:35:24.324998.csv")

# 

#%%
fig = plt.figure(figsize=(21,12),facecolor = 'white')
gs = GridSpec(3, 3)

ax1 = plt.subplot(gs[0, :])
ax = sns.scatterplot(x="转债价格", y="股价",
                    hue="转股溢价率", size="信用",
                    sizes=(10, 200),
                    data=data_sc)

ax2 = plt.subplot(gs[1, :2])
ax = sns.scatterplot(x="转债价格", y="股价",
                     hue="转股溢价率", size="信用",
                     palette=cmap, sizes=(10, 200),
                     data=data_sc)
ax3 = plt.subplot(gs[1:, 2])
ax = sns.scatterplot(x="转债价格", y="股价",
                     hue="转股溢价率", size="信用",
                     sizes=(10, 200),
                     data=data_sc)
ax4 = plt.subplot(gs[2, 0])
ax = sns.scatterplot(x="转债价格", y="股价",
                     hue="转股溢价率", size="信用",
                     sizes=(10, 200),
                     data=data_sc)
ax5 = plt.subplot(gs[2, 1])
ax = sns.scatterplot(x="转债价格", y="股价",
                     hue="转股溢价率", size="信用",
                     sizes=(10, 200),
                     data=data_sc)


#%%
import seaborn as sns
sns.set()

# Load the example iris dataset
planets = sns.load_dataset("planets")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)

ax = sns.scatterplot(x="distance", y="orbital_period",
                     hue="year", size="mass",
                     palette=cmap, sizes=(10, 200),
                     data=planets)



#%%

import seaborn as sns
sns.set()
data =  pd.read_csv(r"./"+"2019-10-07 14:35:24.324998.csv")


data_sc = data[["转债价格","股价","转股溢价率","信用"]]


cmap = sns.cubehelix_palette(start=2.8,rot=-.2, as_cmap=True)

ax = sns.scatterplot(x="转债价格", y="股价",
                     hue="转股溢价率", size="信用",
                     palette=cmap, sizes=(10, 200),
                     data=data_sc,legend=False)



#%%
