"""
Gabrielle Sedlar
HW4 Q2
February 8, 2025

Task:  Building on problem 1: once again find all null rows from the locations dataset. Once 
found, update them with a region value of 999. Once complete, write this dataframe to a 
file called q2-a.out. You should then update the regions dataset to include a region 
with the id of 999 and an identifier of Carlow. Also write this new regions dataset to a file 
as q2-b.out. 

"""
import pandas as pd

#bringing in dataframes, opening files for output
locDF = pd.read_csv('../Data/locations.csv')
regDF = pd.read_csv('../Data/regions.csv')
fileA = open('q2-a.out','w')
fileB = open('q3-b.out','w')

#find and fill all null values of 999
locDF = locDF.fillna(999)

#write new dataframe to file called q2-a.out
fileA.write(str(locDF[locDF.region_id== 999]))

fileA.close() #done with the file, closing it

data = dict.fromkeys(regDF.columns) #getting dictionary with column names

#assigning values to each column for the new entry
data['id'] = 999
data['identifier'] = 'Carlow'

#adding new values to a combined DataFrame
newDF = pd.DataFrame([data])
comboDF = pd.concat([regDF,newDF])

#writing the output and closing the file
fileB.write(str(comboDF))
fileB.close()

