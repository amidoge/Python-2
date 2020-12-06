#Random Password

from random import randint
'''
Make a function that generates a random password. The
password should have a random length of 7 and 10
characters. Each character should be randomly selected
from positions 33 to 126 in the ASCII table. Your function
will not take any parameters. It will return the randomly
generated password as its only result. Display the 
randomly generated password in your file's main program.
Your main program should only run when your solution has
not been imported into another file.
'''

def random_password():
    #making a list where I put all my generated characters in
    random_chars = []
    #selecting random length between 7 and 10
    length = randint(7, 10)
    #making characters that go in a loop that goes for the length
    for i in range(length):
        #generating random char between 33 and 126 in ASCII table
        random_char = randint(33, 126)
        char = chr(random_char) #this function makes the ASCII int turn into a char
        random_chars.append(char)
    return ''.join(random_chars)
    
if __name__ == '__main__':
    a = random_password()
    print(a)