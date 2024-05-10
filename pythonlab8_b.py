#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:33:35 2024

@author: justinesilverstein
"""

#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#Yes, but we need to check the robots.txt which we can do by entering the basic #url with /robots.txt at the end. We need to the read the text shown by entering #the robots.txt to see where we are allowed and not allowed.


#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = r'/users/justinesilverstein/Desktop/data-and-programming-class/' 

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find_all('table')
print(len(table))
print('Madonna' in table[0].text)

tables = table[0]
rows = tables.find_all('tr')
cells = [r.find_all(lambda c: c.name in ['td', 'th']) for r in rows]
#text = [[t.text for t in c] for c in cells]
text = [[t.text.strip().replace('|n','') for t in c] for c in cells]
print(text[1])

text_rows = [','.join(t) for t in text]
text_body = '\n'.join(text_rows)

with open(path, 'w') as ofile:
    ofile.write(text_body)









