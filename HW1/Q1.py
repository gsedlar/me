"""
Gabrielle Sedlar
HW2 Q1
January 26, 2025

Task:  Create a python file that asks a user for their name. Your application should output the 
phrase “Hello, “ and whatever name the user provides to the application. In addition to outputting 
this response to the console, you should also write it to a file called q1.out 

"""
#asks user for name
name = input('Please enter your name: ')

#switches name to title case
capitalName = name.title()

#saves output to a new file
file = open('q1.out','w')
file.write('Hello, ' + capitalName)
file.close()

#prints output
print('Hello, ' + capitalName)

