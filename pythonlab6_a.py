#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:43:14 2024

@author: justinesilverstein
"""

#JSilverstein25

import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
    
    
#   March 2001 - November 2001
#   December 2007 - June 2009
#   February 2020 - April 2020


# Next continue to clean up the figure, adding a title, axis labels, shading the area
# that designates recessions, and any other changes that come to mind. If you manually
# copy-pasted the code for each recession line, try instead to put them in containers
# and use a for-loop.

path=r'/Users/justinesilverstein/Desktop/data-and-programming-class'
df = pd.read_csv(os.path.join(path,'UNRATE.csv'), parse_dates=['DATE'])

recessions=[(datetime.datetime(2001,3,1),datetime.datetime(2001,11,30)),(datetime.datetime(2007,12,31),datetime.datetime(2009,6,30)),(datetime.datetime(2020,2,29),datetime.datetime(2020,4,30))]

df.plot(x='DATE', y='UNRATE')

fig, ax= plt.subplots(figsize=(12,6))
ax = df.plot(x='DATE', y='UNRATE', legend=False, ax=ax)

for start,end in recessions:
    ax.axvspan(start, end, alpha=0.3, color='red')


ax.set_title('US Unemployment Rate', fontsize= 18)
ax.set_xlabel('')
ax.set_ylabel('UnEmployment Rate', fontsize=12)
ax.tick_params(axis='both', labelsize=14)
plt.show()



















