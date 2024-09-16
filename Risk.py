# -*- coding: utf-8 -*-
"""
@author: C.Z.J
"""
# risk #
import akshare as ak
import pandas as pd
import numpy as np

# get data of stock 600519 (贵州茅台)
df = ak.stock_zh_index_daily_tx(symbol='sh600519')
df = df.set_index(df['date'])
R = df['close'].pct_change().dropna()


#-------------------------Task 1: variance depicts risk-------------------------#
var1 = np.var(R)
std1 = np.std(R)
var2 = R.var()
std2 = R.std()

print('Task 1: variance depicts risk \n\nusing numpy:', 
      'the variance of 茅台 is {:.4f}, std is {:.4f}'.format(var1, std1),'\nusing pandas:', 
      'the variance of 茅台 is {:.4f}, std is {:.4f}'.format(var2, std2))


#-------------------------Task 2: downside deviation-------------------------#
def downside_deviation(r):
    mean = r.mean()
    r_adjust = r.map(lambda x: min(x-r.mean(), 0))
    risk = np.sqrt((r_adjust**2).mean())
    return risk

risk = downside_deviation(R)
print('Task 2: downside deviation \n\nthe downside deviation of 茅台 is {:.4f}'.format(risk))


#-------------------------Task 3: VaR-------------------------#
print('Task 3: VaR')
# Back/Historic Simulation Approach
var1 = R.quantile(0.05)/100
print('\nVaR using Back Simulation Approach:', var1)

# Covariance Matrix Method
from scipy.stats import norm
var2 = norm.ppf(0.05, R.mean())
print('VaR using Covariance Matrix Method:', var2)



