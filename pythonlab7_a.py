#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:22:01 2024

@author: justinesilverstein
"""

#Justine S

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression 

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
df = pd.read_csv(url_to_csv)


# 1) Explore the data & produce some basic summary stats  

df.describe()
df.columns

df['price'].mean()


# 2) Run a regression of price (y) on carat (x), including an 
#    intercept term.  Report the estimates of the intercept & slope 
#    coefficients using each of the following methods:
#        a) NumPy
#        b) statsmodels (smf) 
#        c) statsmodels (sm)
#        d) scikit-learn (LinearRegression)  
#           Hint:  scikit-learn only works with array-like objects.    
#    Confirm that all four methods produce the same estimates.

#a)

x = df['carat']
y = df['price']
m, b = np.polyfit(x, y, deg=1)

result_np = np.poly1d((m,b))
print(result_np)

#With numpy, the intercept term is -2256 and slope is 7756.

#b) 
model = smf.ols('price~carat', data=df)
results_smf = model.fit()
print(results_smf.summary())

#With smf, the intercept is -2256.3686 and the slope is 7756.4256


#c)
y = df['price']
df['const'] = np.ones(len(x))
x= df[['const','carat']]

model = sm.OLS(endog=y, exog=x)
result=model.fit()
result.summary()

#The coef estimate is 7756.4256, the intercept is -2256.3606

#d)
y = df['price']
x = df[['carat']]
y.shape
x.shape

model = LinearRegression(fit_intercept=True)
results_sk1 = model.fit(x,y)
print(results_sk1.intercept_)
print(results_sk1.coef_)

#The intercept  is -2256.36 and the coef is 7756.43


# 3) Run a regression of price (y) on carat, the natual logarithm of depth  
#    (log(depth)), and a quadratic polynomial of table (i.e., include table & 
#    table**2 as regressors).  Estimate the model parameters using any Python
#    method you choose, and display the estimates.  

model = smf.ols('price~carat + C(cut) + C(color) +C(clarity)+ np.log(depth) + table + np.power(table, 2)', data=df)
results = model.fit()
print(results.summary())

#The coef estimate is 617.2723 and the intercept is -1071.9974


# 4) Run a regression of price (y) on carat and cut.  Estimate the model 
#    parameters using any Python method you choose, and display the estimates.  

model = smf.ols('price~carat + C(cut)', data=df)
results = model.fit()
print(results.summary())

#The intercept is -3875.47 and the slope is 1120.33



# 5) Run a regression of price (y) on whatever predictors (and functions of 
#    those predictors you want).  Try to find the specification with the best
#    fit (as measured by the largest R-squared).  Note that this type of data
#    mining is econometric blasphemy, but is the foundation of machine
#    learning.  Fit the model using any Python method you choose, and display 
#    only the R-squared from each model.  We'll see who can come up with the 
#    best fit by the end of lab. 

model = smf.ols('price~carat + C(cut) + C(color) +C(clarity)+ np.log(depth)', data=df)

results = model.fit()
print(results.rsquared)

#I got an rsquared of 0.916




 