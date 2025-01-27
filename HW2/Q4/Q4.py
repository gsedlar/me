"""
Gabrielle Sedlar
HW2 Q4
January 26, 2025

Task: Create a python application that asks for a series of names. Until a user enters exit, 
keep collecting the name of students. Once a user asks to exit, print the list of students 
to q4.out 

"""

#intiiates blank list
names = []

#initiates variable for each added name
current = input('Please enter the first name. To stop, type EXIT: ') 

#user adds names until they enter 'EXIT'; each name is added to the names list
while (current != 'EXIT'):
    names.append(current)
    current = input('Please enter the next name. To stop, type EXIT: ')
    
#adds names to file by a for loop
file = open('q4.out','w')
for name in names:
    file.write(name + '\n')
file.close()