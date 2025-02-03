"""
Gabrielle Sedlar
HW3 Q10
February 2, 2025

Task:  Utilizing the regions.csv and locations.csv datasets, accept input from the user 
for a specific region name. You should then return the number of locations that exist in 
that region. If the region name does not exist in our dataset, then return the message 
"This region does not exist".  

"""

import pandas as pd

#use pandas to convert csv files into dataframes
locDF = pd.read_csv('../Data/locations.csv')
regDF = pd.read_csv('../Data/regions.csv')


region = input('Please enter a region name: ')
count = 0 #initializes 0 locations in that region

#check if the region exists, and if so, gets the reg_id value (id in region.csv)
if regDF.identifier.isin([region]).any() == False:
    print('This region does not exist.')

else:
    reg_id = regDF.loc[regDF['identifier'] == region, 'id'].iloc[0] 

    for i, r in locDF.iterrows():  #searches through the rows in locations.csv
        if r['region_id'] == reg_id: #if the location has the correct reg id, add one to the count
            count += 1
    
    #print final message
    print(str(count) + ' locations are in that region')