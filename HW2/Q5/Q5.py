"""
Gabrielle Sedlar
HW2 Q5
January 26, 2025

Task: Building from q4, we want to take the same actions. However now we want to present a 
menu to the user that looks like the below: 
    1) Enter user 
    2) Exit 
When a user enters 1 – add our user like you did previously 
When a user enters 2 – exit like we did previously and print the current set of users to a 
file called q5.out 

"""

#intiiates blank list and variable for menu option
names = []
choice = 0

#until the user enters 2, they will continue to add names to the names list
while (choice != 2):
    print('\n1) Enter user')
    print('2) Exit')
    choice = int(input('Choose your action from the list above: '))
    if (choice==1):
        current = input('\nPlease enter the next name: ')
        names.append(current)
        
    
#adds names to file by a for loop
file = open('q5.out','w')
for name in names:
    file.write(name + '\n')
file.close()