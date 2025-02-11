"""
Gabrielle Sedlar
HW4 Q10
February 10, 2025

Task:  Using the same datasets, return the names of the pokemon who appear in the most and 
fewest locations.This data should be returned as a dataframe and written to a file called 
q10.out.

"""
import pandas as pd

pokeDF = pd.read_csv('../Data/pokemon.csv')
encDF = pd.read_csv('../Data/encounters.csv')
locDF = pd.read_csv('../Data/locations.csv')
areaDF = pd.read_csv('../Data/location_areas.csv')


#merge 3 datasets together
la = locDF.merge(areaDF,how='left',left_on='id',right_on='location_id',suffixes = ('_loc','_area'))
lae = la.merge(encDF,how='left',left_on='id_area',right_on='location_area_id')
laep = lae.merge(pokeDF,how='left',left_on='pokemon_id',right_on='id',suffixes = ('_lae','_poke'))

#group based on pokemon id, then count how many rows (locations) each pokemon appears in and give highest and lowest counts
mostLoc = laep.groupby('identifier')['identifier'].count().sort_values(ascending=False).head(1)
leastLoc = laep.groupby('identifier')['identifier'].count().sort_values(ascending=False).tail(1)


file = open('q10.out','w')
file.write(str(mostLoc) + '\n')
file.write(str(leastLoc) + '\n')
file.close()
