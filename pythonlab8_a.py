#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:31:55 2024

@author: justinesilverstein
"""
#Justine Silverstein

import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas_datareader import wb 
import requests
import matplotlib.pyplot as plt

# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 31st 2021.

#Hint: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage

#Hint: https://www.alphavantage.co/support/#api-key

#  Then use Pandas DataReader's interface for Alpha Vantage, not the
#  API that they describe on their site (DataReader does all that for
#  you!)

apikey = '3SZKJ9GXLOB0OUHT'
start = datetime.datetime(year=2019, month=1, day=1)
end = datetime.datetime(year=2023, month=5, day=1)
series = 'TSLA'
endpoints = 'av-monthly'

df = web.DataReader(series, endpoints, start=start, end=end, api_key=apikey)
df.head()

# 2. Create a new column that holds the rolling 3 month average.
df['close_3ma'] = df['close'].rolling(3).mean()


# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.
df.index = pd.to_datetime(df.index)
df_qtr = df.resample('Q').mean()


# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.

fig, ax = plt.subplots(figsize=(16,9))
x = pd.to_datetime(df.index)
ax.plot(x, df['close'], 'r-', label= 'mean closing')
ax.plot(x, df['close_3ma'], 'b--', label='mean closing, 3 no MA')

ax.legend()
ax.set_title('Tesla Montly Average Closing Stock Price')
ax.set_xlabel('')
ax.set_ylabel('Price (S)')
plt.show()











