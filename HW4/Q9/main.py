"""
Gabrielle Sedlar
HW4 Q9
February 10, 2025

Task:  Utilizing the poke,encounters,location_area and locations datasets, write the 
following program. The four of these data sets share a series of id's used to associate 
data between each other. Using these id's, print out the top 5 locations with the most 
pokemon. Print out the dataframe that shows these top 5 locations sorted from highest to 
least. 

"""
import pandas as pd

encDF = pd.read_csv('../Data/encounters.csv')
locDF = pd.read_csv('../Data/locations.csv')
areaDF = pd.read_csv('../Data/location_areas.csv')

#merge 3 datasets together
la = locDF.merge(areaDF,how='left',left_on='id',right_on='location_id',suffixes = ('_loc','_area'))
lae = la.merge(encDF,how='left',left_on='id_area',right_on='location_area_id')

#group based on location names, then count how many pokemon are in each location
DF = lae.groupby('identifier_loc')['pokemon_id'].nunique() #.nunique() counts the number of unique pokemon_id values in each group

file = open('q9.out','w')
file.write(str(DF.sort_values(ascending=False).head(5))) #adds top 5 locations w/ most pokemon to the file
file.close()


