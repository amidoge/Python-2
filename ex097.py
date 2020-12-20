#Making a good password
#importing the functions from previous exercises
from ex094 import random_password #importing my old password generator function
from ex096b import password_checker #importing my old password checker function
'''
Using your solutions to Exercises 94 and 96, write a
program that generates a random good password and displays
it. Count and display the number of attempts that were
needed before a good password was generated. Structure
your solution so that it imports the function named main
in the file that you create for this exercise.
'''

if __name__ == '__main__':
    count = 0 #counting how many times it took to generate a new password which finally is verified
    password = random_password() #making the first random password
    result = password_checker(password) #verifying the first random password
    while result == False: #if it is false it is going to keep doing this until it is true
        count += 1 #keep counting until result == True
        password = random_password()
        result = password_checker(password)
    #once result == True...
    count += 1 #I need to add another because there needs to be the extra round for the good password as well
    if count == 1: #this is for grammar purposes only
        print(f'It took {count} try to generate a good password')
    else:    
        print(f'It took {count} tries to generate a good password.')
