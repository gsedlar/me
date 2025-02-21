"""
Gabrielle Sedlar
HW5 Q3
February 18, 2025

Task:  Using the appropriate datasets, draw a graph showing the number of pokemon within a 
region. The Y Axis should show the number of Pokemon within that region and the X axis 
should show the name (ex: Kanto). The name of the region should be capitalized appropriately. 
Ensure that appropriate labels are given to both the x and y axis and an appropriate title is 
applied to the graph as a whole. The labels should be formatted in a way that makes it easy for 
the user to know what the graph is visualizing. 

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


reg = pd.read_csv('../data/regions.csv')
loc = pd.read_csv('../data/locations.csv')
locar = pd.read_csv('../data/location_areas.csv')
enc = pd.read_csv('../data/encounters.csv')


#merging all dataframes into one large one
merged1 = locar.merge(enc,how='left',left_on='id',right_on='location_area_id',suffixes=('_locar','_enc'))
merged2 = reg.merge(loc,how='left',left_on='id',right_on='region_id',suffixes=('_reg','_loc'))
merged = merged1.merge(merged2,how='left',left_on='location_id',right_on='id_loc')


#get the count of how many pokemon in each region
count = merged.groupby('identifier_reg')['identifier_reg'].count().reset_index(name='count')
count['identifier_reg'] = count['identifier_reg'].str.title() #switch regions to title case

#make/design barplot for results
b = sns.barplot(data=count,x='identifier_reg',y='count',palette='bright')
plt.xlabel('Region', fontsize=16)
plt.ylabel('Number of Pokemon',fontsize=16)
plt.title('Number of Pokemon within each Region',fontsize=20,fontweight='bold')
plt.tick_params(axis='both',which='major',labelsize=10,)

plt.show()