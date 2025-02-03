"""
Gabrielle Sedlar
HW3 Q5
February 1, 2025

Task:  Using the documentation at https://pandas.pydata.org/docs/reference/index.html, find 
the parameter for read_csv that would allow me to change the delimiter for a CSV from 
a comma to something else of my own choosing. 

"""

import pandas as pd

df1 = pd.read_csv('file.csv', sep=',')
df2 = pd.read_csv('file.csv', sep=';')
df3 = pd.read_csv('file.csv', sep=':')
# sep is the parameter, and the comma is the default option

# delimeter does the same thing

df4 = pd.read_csv('file.csv', delimeter=',')
df5 = pd.read_csv('file.csv', delimeter=';')
df6 = pd.read_csv('file.csv', delimeter=':')