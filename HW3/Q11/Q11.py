"""
Gabrielle Sedlar
HW3 Q11
February 3, 2025

Task:  Utilizing the locations.csv dataset, return a list of locations that are not associated 
with a region.  

"""


import pandas as pd

#use pandas to convert csv files into dataframes
locDF = pd.read_csv('../Data/locations.csv')


locations = [] #empty list of locations with no region

for i, r in locDF.iterrows(): #for each row in data
    if not r['region_id'] >= 1: #if the value isn't over 1 (null value)
        locations.append(r['identifier']) #add location to list
    
print(locations) #print list
    

