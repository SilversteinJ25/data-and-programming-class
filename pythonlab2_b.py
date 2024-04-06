#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:37:54 2024

@author: justinesilverstein
"""

#Justine Silverstein
#Unless otherwise noted, try solving these using class content and without searching online

#Citation: For how to flatten lists from Stack Overflow: 
#https://stackoverflow.com/questions/20112776/how-do-i-flatten-a-list-of-lists-nested-lists ,
#I went to the TA seession with Kayeceee

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i == 5:
        i += 1
        continue
    elif i >= 5:
        print('big')
    else:
        print('what happened?')
    print('Finished!')
    i += 1

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4

demo_list = ['1', '2', '3', '4']
for i in range(5):
        print(demo_list[:i])
               

#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list


both = [item/2 for sublist in start_list for item in sublist if item%2 == 0]
print(both)


result = []
start_list = [[2, 3, 4], [6, 8, 9]]
for sublist in start_list:
    for items in sublist:
        if items % 2 == 0:
            result = result + [items/2]
print(result)
            

#4
#import datetime
#start_dict = {'noah': '2/23/1999',
           #   'sarah':'9/1/2001',
           #   'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end

from datetime import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
Noah_date = datetime.datetime(1999, 2, 23)
Sarah_date = datetime.datetime(2001, 9, 1)
Zach_date = datetime.datetime(2005, 8, 8)


dates = [] 
names = []
new_dict = {}
for key,val in start_dict.items():
    dates.append(datetime.strptime(val, '%m/%d/%Y'))
    names.append(key.capitalize())
    new_dict.update({key.capitalize() : datetime.strptime(val, '%m/%d/%Y')})
    print(dates)
    print(names)

print(new_dict)
















