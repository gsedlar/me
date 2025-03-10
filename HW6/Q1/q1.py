"""
Gabrielle Sedlar
March 3, 2025
HW6 Q1

Task: Utilizing the datasets that we've been working with, draw a graph showing the number of 
each type of pokemon exist (i.e. electric, fire, etc.). The graph should show the number 
and should show the string representation of that type (i.e. fire, electric) and not just an 
integer representation. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

p = pd.read_csv('../data/pokemon_types.csv')
t = pd.read_csv('../data/types.csv')

#merge and group data to get each type with the number of pokemon of that type
pt = p.merge(t,how='left',left_on='type_id',right_on='id')
pt = pt.groupby('identifier')['identifier'].count().reset_index(name='count')


#make and edit plot
b = sns.barplot(data=pt,x='identifier',y='count',palette='bright')
plt.xlabel('Type', fontsize=16)
plt.ylabel('Number of Pokemon',fontsize=16)
plt.title('Number of Each Type of Pokemon',fontsize=20,fontweight='bold')
plt.tick_params(axis='both',which='major',labelsize=10, rotation=90)


