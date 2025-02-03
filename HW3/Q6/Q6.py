"""
Gabrielle Sedlar
HW3 Q6
February 1, 2025

Task:  Using poke.csv, write an application that consumes this data and then gives me a 
summary of the data. Specifically, produce an application that will read this data in and 
return the following output: 
    The pokemon dataset consts of X columns and Y rows. It has the following 
    column names [list of column names here]. 

"""

import pandas as pd

#converts csv file to a dataframe
df = pd.read_csv('../Data/poke.csv') 


#prints the desired output with the number of columns and rows
print('The pokemon dataset consists of ' + str(df.shape[1]) + ' columns and ' + str(df.shape[0]) +
      ' rows. It has the following column names: ' + str(df.columns.tolist()))

#prints names of columns, tolist() gets rid of the Index([],dtype='object') text in df.columns


