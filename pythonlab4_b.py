#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:31:25 2024

@author: justinesilverstein
"""

#NAMES

import pandas as pd
import numpy

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.

path=r'/Users/justinesilverstein/Desktop/data-and-programming-class/iris.csv'
flowers=pd.read_csv(path)

#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.

# There are three kinds of flowers, called setosa, versicolor, and virginica. 

setosa = flowers.iloc[0:50]
versicolor = flowers.iloc[51:101]
virginica = flowers.iloc[101:]


#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.


#3. How many of observations for each species of iris is in the data?


#4. Using one line of code, divide each value by the mean for that measure,
#   and assign the result to four new columns.  How is this different from 
#   a zscore?  How would you make this a zscore instead?  What's the problem
#   with doing this without accounting for the values in the species column?


#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.


#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.