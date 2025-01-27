"""
Gabrielle Sedlar
HW2 Q2
January 26, 2025

Task:  Create a python file that asks a user for their age. Your application should print the user 
input to a file called q2.out. It should then add 5 to the age that is provided and then 
also write that to a file called q2.out. Both lines should be present in the file after it is 
run. 

"""
#ask user for age
age = int(input('Please enter your age: '))

#add age to file
file = open('q2.out','w')
file.write(str(age) + '\n')

#add 5 to age
newAge = age + 5

#add new age to file and close file
file.write(str(newAge))
file.close()