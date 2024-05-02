#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:32:16 2024

@author: justinesilverstein
"""

import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
import matplotlib.pyplot as plt

series = {'CPMNACSCAB1GQDE':'GDPGermany',
          'LRUNTTTTDEQ156S':'EMPGermany',
          'CPMNACSCAB1GQPL':'GDPPoland',
          'LRUNTTTTPLQ156S':'EMPPoland'}
df = web.DataReader(series.keys(), 'fred', start='1995-01-01', end='2019-10-01')

df = df.rename(series, axis=1)

# 1)
# This data is from lecture 18.  Explore it using plots and summary
# statistics. What is wrong with the employment data from Poland? 
# Then, apply an HP filter from the statsmodels library, and filter 
# all four series.  Plot the cycles, trends, and original values to
# see what is happening when you filter.

df=df.reset_index()
df.describe()
df.columns

x = df['DATE']
y1 = df['EMPPoland']
y2 = df['EMPGermany']
fig,ax = plt.subplots()
ax.plot(x,y1, label='Poland')
ax.plot(x,y2, label= 'Germany')
ax.legend(loc='best')
ax.tick_params(axis='both', labelsize=12)
plt.show()

x = df['DATE']
y1 = df['GDPPoland']
y2 = df['GDPGermany']
fig,ax = plt.subplots()
ax.plot(x,y1, label='Poland')
ax.plot(x,y2, label= 'Germany')
ax.legend(loc='best')
ax.tick_params(axis='both', labelsize=12)
plt.show()

#There's missing data for EMPPoland

df['EMPPoland'].isna().sum()
df['EMPPoland'] = df['EMPPoland'].interpolate(method='linear')

g_cycle, g_trend = sm.tsa.filters.hpfilter(df['GDPGermany'], lamb=1600)
p_cycle, p_trend = sm.tsa.filters.hpfilter(df['GDPPoland'], lamb=1600)



# 2)
# The code from the lecture includes a function that implements the
# Hamilton filter, though we did not go over the code in detail.
# Copy that function over and try to understand most of what it is
# doing (you may have to test it in pieces) and then apply it to
# this data. Modify your plots from question 1 to compare the results
# of the Hamilton and HP filters to the unfiltered values.

def hamilton_filter(data, h=8, p=4):
    new_cols = [data]
    for s in range(h, h+p):
        name = f'{data.name}.{s}'
        d = data.shift(s)
        d.name = name
        new_cols.append(d)
    new_cols = pd.concat(new_cols, axis=1)
    
    model = sm.GLM(endog=new_cols.iloc[:,0],
                   exog=sm.add_constant(new_cols.iloc[:,1:]),
                   missing='drop')
    res = model.fit()
    
    trend = res.fittedvalues
    cycle = pd.Series(res.resid_pearson,
                      index=trend.index,
                      name=f'{data.name}.cycle')
    trend.name = f'{data.name}.trend'
    final_data = pd.concat([new_cols, trend, cycle], axis=1)
    
    return final_data.iloc[:,-2:]

g_hamilton = hamilton_filter(df['GDPGermany'], h=8, p=4)
p_hamilton = hamilton_filter(df['GDPPoland'], h=8, p=4)    

fig, axs = plt.subplots(3,2,sharex=True, figsize=(12,8))
x=df['DATE']
axs[0,0].plot(x, df['GDPGermany'], 'k--')
axs[1,0].plot(x, g_trend, 'r-', label='HP Filter')
axs[1,0].plot(x, g_hamilton['GDPGermany.trend'], 'b-', label='Hamilton')
axs[2,0].plot(x, g_cycle, 'r-')
axs[2,0].plot(x, g_hamilton['GDPGermany.cycle'], 'b-')

axs[0,1].plot(x, df['GDPPoland'], 'k--')
axs[1,1].plot(x, p_trend, 'r-')
axs[1,1].plot(x, p_hamilton['GDPPoland.trend'], 'b-')
axs[2,1].plot(x, p_cycle, 'r-')
axs[2,1].plot(x, p_hamilton['GDPPoland.cycle'], 'b-')

axs[0,1].yaxis.tick_right()
axs[1,1].yaxis.tick_right()
axs[2,1].yaxis.tick_right()

axs[0,0].set_title("German GDP")
axs[0,1].set_title("Polish GDP")
axs[0,0].set_ylabel('Level')
axs[1,0].set_ylabel('Trend')
axs[2,0].set_ylabel('Cycle')

fig.legend(loc='lower center')
plt.show()