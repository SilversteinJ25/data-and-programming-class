#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:31:25 2024

@author: justinesilverstein
"""

#Justine Silverstein

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
pd.value_counts(flowers.species)

#For sepal length, the mean is 5.843, the median is 5.8 and the STD is 0.83
#For sepal width, the median is 3, the mean is 3.6, and the STD is 0.44
#For petal length, the median is 4.35, the mean is 3.75, and the STD is 1.76
#For petal width, the median is 1.3, the mean is 1.2, and the STD is 0.76

print(flowers.iloc[:,0:4].median())
print(flowers.iloc[:,0:4].mean())
print(flowers.iloc[:,0:4].std())

setosa = flowers.loc[flowers['species']=='setosa',:]
print(setosa.iloc[:,0:4].mean())

versicolor = flowers.loc[flowers['species']=='versicolor',:]
print(versicolor.iloc[:,0:4].mean())

virginica = flowers.loc[flowers['species']=='virginica',:]
print(virginica.iloc[:,0:4].mean())


#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.

flowers.loc[flowers['sepal_length']==flowers['sepal_length'].max()]
flowers.loc[flowers['sepal_width']==flowers['sepal_width'].max()]
flowers.loc[flowers['petal_length']==flowers['petal_length'].max()]
flowers.loc[flowers['petal_width']==flowers['petal_width'].max()]

#3. How many of observations for each species of iris is in the data?
pd.value_counts(flowers.species)

#There are 50 observations for each species of iris in the data.


#4. Using one line of code, divide each value by the mean for that measure,
#   and assign the result to four new columns.  How is this different from 
#   a zscore?  How would you make this a zscore instead?  What's the problem
#   with doing this without accounting for the values in the species column?


#This is different from a zscore becuase we are not taking into consideration
#the standard deviation. To make this a z score, you need to divide by the
#stadnard deviation and subtract the value from the mean. This issue with 
#not doing this while accounting for the species is how the species have 
#different averages overall. 

for column_name in flowers.columns[0:4]:
    flowers[column_name+'notscore']=flowers[column_name]/flowers[column_name].mean()    


#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.

flowers['petal_area']=flowers['petal_length']*flowers['petal_width']

#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

virginica = flowers.loc[flowers['species']=='virginica',:]
print(virginica.iloc[:,0:1].mean())

# sepal_length mean is 6.588


virginica['length_greater_mean'] = 0
virginica['length_greater_mean'].loc[flowers['sepal_length'] > \
                                     flowers['sepal_length'].mean(),]=1

flowers=flowers[['sepal_length', 'sepal_width', 'petal_length', \
                 'petal_width','sepal_lengthnotscore', 'sepal_widthnotscore',\
                     'petal_lengthnotscore','petal_widthnotscore','species']]









