#Check a password

'''
Write a function that determines whether or not a 
password is good. We will define a good password to be a
one that is at least 8 characters long and contains at 
least one uppercase letter, at least one lowercase letter,
and at least one number. Your function should return true
if the password passed to it as its only parameter is good.
Otherwise it should return false. Include a main program
that reads a password from the user and reports whether
or not if it is good. Ensure that your main program only
runs when your solution has not been imported to another
file.
'''

def password_checker(password):
    #checking if it is at least eight characters long
    if len(password) < 8:
        return False
    #making sure that there is at least 1 uppercase letter in the password
    #I am going to use the ord() function to convert the char into an ASCII, to make sure that there is at least 1 uppercase letter.
    uppercase_found = False #this is going to be False right now. If an uppercase is found, then it is going to change to True
    for i in range(len(password)):
        if ord(password[i]) >= 65 and ord(password[i]) <= 90: #if it between 65 and 90 in the ASCII table (uppercase letters) then I want to change it to True
            uppercase_found = True
    if uppercase_found == False:
        return False
    #making sure that there is at least 1 lowercase letter in the password
    #I am going to use the ord() function to convert the char into an ASCII, to make sure that there is at least 1 lowercase letter.
    lowercase_found = False #this is going to be False right now. If a lowercase letter is found, then it is going to change to True
    for x in range(len(password)):
        if ord(password[x]) >= 97 and ord(password[x]) <= 122: #if it is between 97 and 122 in the ASCII table (lowercase letters), then I want to change it to True
            lowercase_found = True
    if lowercase_found == False:
        return False
    #the final thing to check is if there is a number in the password.
    #I am going to use the ord() function again because it will help convert the char into an ASCII number, and I can use that to check if it is in between the numbers ASCII range
    number_found = False #this is going to be False right now. If there is a number found, then I am going to change this to True
    for j in range(len(password)):
        if ord(password[j]) >= 48 and ord(password[j]) <= 57: #if the char turns out to be in the number ASCII range, then that means that it is a number. WHich means that I can change it to True.
            number_found = True
    if number_found == False:
        return False
    return True

if __name__ == '__main__':
    user_password = input('Password: ')
    print(password_checker(user_password))
    