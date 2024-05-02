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

('GDPGermany~GDPPoland', data=df)


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









# 2)
# The code from the lecture includes a function that implements the
# Hamilton filter, though we did not go over the code in detail.
# Copy that function over and try to understand most of what it is
# doing (you may have to test it in pieces) and then apply it to
# this data. Modify your plots from question 1 to compare the results
# of the Hamilton and HP filters to the unfiltered values.

















