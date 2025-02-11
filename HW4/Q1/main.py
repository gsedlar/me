"""
Gabrielle Sedlar
HW4 Q1
February 8, 2025

Task:  Using the locations dataset, return all null rows and write the dataframe to a file 
called q1.out 

"""
#########################NOT SOLVED


import pandas as pd

locDF = pd.read_csv('../Data/locations.csv')
file = open('q1.out','w')

#save all rows wih no region id to a new dataframe
newDF = locDF[locDF['region_id'].isnull()]

#add rows to the dataframe and close the file
file.write(str(newDF))

file.close()
