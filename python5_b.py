#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:38:00 2024

@author: justinesilverstein
"""

#SilversteinJ25

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys

list(df)


df.groupby('clarity')





# 2) Display the describe() output JUST for group color=E, clarity=SI2






# 3) Display the max value for price in each group







# 4) Display the min value for price in each group









# 5) Write four different functions:
#    - one that works with map on the values in a column
#    - one that works with apply on the values in a row
#    - one that works with apply on the values in a column
#    - one that works with apply on a groupby object









# 6) Display only the maximum price for each clarity.









# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?









