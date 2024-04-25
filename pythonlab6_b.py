# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Justine S

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species')
plt.show()

#Recreate this plot in Matplotlib, without using Seaborn!
#Then try adding some of your own customizations to the 
#plot using MatPlotLib methods

fig, ax= plt.subplots()
ax.plot(df['sepal_length'],df['petal_length'],linestyle='',marker='.',markersize=5)

flowers=df.groupby(['species'])
flowers.describe()

for species,groups in flowers:
    plt.scatter(x=groups['sepal_length'],
                y=groups['petal_length'])



fig, ax = plt.subplots(figsize=(11,9))
iris=df.groupby('species')
colors = {'setosa':'blue', 'versicolor':'green','virginica':'purple'}

for key,group in iris:
    group.plot(x='sepal_length', 
               y='petal_length',
               ax=ax,
               kind='scatter',
               color=colors[key],
               label=key.capitalize(),
               fontsize=10)
leg=ax.legend()
leg.set_title('species')
plt.show()






















