#Is a number prime?
from math import sqrt
'''
-Greater than 1
-Only divisible by one and itself
-Return True if prime, False if not
-Only runs in the main file
'''

def prime_or_not(number):
    #loop that runs until half the number
    if number < 2:
        return False
    if number == 2:
        return True
        
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0: #if it can (integer) divide without any remainders
            return False
    return True

if __name__ == '__main__':
    num = int(input("Number: "))
    function = prime_or_not(num)
    print(function)
