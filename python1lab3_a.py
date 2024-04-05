#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:29:47 2024

@author: justinesilverstein
"""

#Silversteinj25
# Workked with Ella M.
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    value = second_func()
    return value

def second_func(d=40):
    e = 50
    b = 20
    c = 30
    return a + b + c + d + e
result = first_func()
print(result)

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

from datetime import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}

def key_func(key):
    key = key.capitalize()
    return key

def val_func(v):
    v = datetime.strptime(v, '%m/%d/%Y')
    return v
    
answer = {key_func(k):val_func(v) for k, v in start_dict.items()}
print(answer)


#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: (x - x_mean) / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values

from numpy import mean, std

def zscore(x):
    new_score =  (x - mean(x))/std(x) 
    return new_score


test = zscore([0, 1, 2, 3, 4])

print(mean(test))


#source: https://stackoverflow.com/questions/48705448/z-score-calculation-from-mean-and-st-dev

#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior

from numpy import median, absolute
from numpy import mean, std

def zscore(x, modified=None):
    MAD = median(absolute((x-median(x))))
    new_score =  (x - mean(x))/MAD
    return new_score

test = zscore([0, 1, 2, 3, 4, 4, 9])

print(mean(test))

#cite: https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments







