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
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    #fig = plt.figure(figsize=(8,6))
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7- i) * flip)

fig = plt.figure(figsize=(21,12),facecolor = 'white')
gs = GridSpec(3, 3)

ax1 = plt.subplot(gs[0, :])
sinplot()
ax2 = plt.subplot(gs[1, :2])
sinplot()
ax3 = plt.subplot(gs[1:, 2])
sinplot()
ax4 = plt.subplot(gs[2, 0])
sinplot()
ax5 = plt.subplot(gs[2, 1])
sinplot()


