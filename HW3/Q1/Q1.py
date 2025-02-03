"""
Gabrielle Sedlar
HW3 Q1
January 31, 2025

Task:  Create a list of users and their test scores. Using this list, convert it to a DataFrame so 
we can begin utilizing pandas to work with the data. Your list should have at least ten 
entries. This application should run and then exit by printing out just the names from your 
DataFrame. 

"""
import pandas as pd

#dictionary scores contains names and scores as lists
scores = { 
    'Name':['John','Adam','Teresa','Beth','Mary','Penny','Jacob','Mark','Goose','Maverick'],
    'Score':[20,78,95,13,25,32,49,92,84,84]
    }

#convert dictionary to DataFrame
df = pd.DataFrame(scores)
#prints just the names from the DataFrame
print(df['Name'])
