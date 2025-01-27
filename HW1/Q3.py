"""
Gabrielle Sedlar
HW2 Q3
January 26, 2025

Task: Building on exercise 2, create a python file that prompts a user for their age. Based upon 
the input do the following based on the value: 
    a. Below 20: print fail to q3.out 
    b. 20 or above and 30 or below: print pass to q3.out 
    c. Above 30: print fail to q3.out 

"""
#ask user for age
age = int(input('Please enter your age: '))

#open file
file = open('q3.out','w')

#if the age is 20 or above and 30 or below, print pass to the file. if below 20 or above 30, print fail to the file
if (age >= 20 and age <= 30):
    file.write('pass')
else:
    file.write('fail')

#close file
file.close()    