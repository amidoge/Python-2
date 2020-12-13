#Random License Plate

from random import randint
'''
Older license plates consist of three letters followed by
three numbers. When all of the license plates following
that pattern had been used, the format was changed to
four numbers followed by three letters.

Write a function that generates a random license plate.
Your function should have approximately equal odds of
generating a sequence of characters for an old license
plate or a new license plate. Write a main program that
calls your function and displays the randomly generated
license plate.
'''

def random_license_plate():
    #older = 1
    #newer = 2
    older = False
    newer = False

    license_type = randint(1, 2) #choose a number between 1 and 2
    if license_type == 1:
        older = True
    else:
        newer = True
    license_plate = [] #making a list for the license plate letters and numbers
    if older: #if it has randomly selected older
        print('Older License Plate: ', end=' ')
        #generate 3 uppercase letters
        for i in range(3):
            random_ascii_char = randint(65, 90) #capital A to Z in ASCII
            random_char = chr(random_ascii_char) #the chr function is going to convert it into a character
            license_plate.append(random_char) #put the random capital letter into the list for the license plate
        #generate 3 numbers
        #I am basically going to do the same thing, except with different ASCII range
        for i in range(3):
            random_ascii_num = randint(48, 57) #0 to 9 in ASCII
            random_num = chr(random_ascii_num) #the chr function is going to convert the ascii char into an actual string char
            license_plate.append(random_num) #then I am going to add the random numbers into the license plate list
    elif newer: #if it has randomly selected newer
        print('Newer License Plate: ', end=' ')
        #generate 4 numbers
        for i in range(4):
            random_ascii_num = randint(48, 57) #0 to 9 in ASCII
            random_num = chr(random_ascii_num) #the chr function is going to convert the ascii char into an actual string char
            license_plate.append(random_num) #I am going to add the random number to the license plate list which is going to be printed out later in the code
        #generate 3 uppercase letters
        #I am basically doing the same thing except with chars
        for i in range(3):
            random_ascii_char = randint(65, 90) #A to Z in ascii
            random_char = chr(random_ascii_char) #this is going to convert the ascii char into an actual char
            license_plate.append(random_char) #I am going to add the random character generated into the end result license plate 
    #after either the newer or older license plate generating methods I want to return the end result
    return ''.join(license_plate)

if __name__ == '__main__':
    print(random_license_plate())
