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
    if number < 2: #if the number is smaller than 2 then it cannot be a prime num
        return False
    if number == 2: #if the number is 2 then it is a prime number
        return True
        
    for i in range(2, round(sqrt(number)) + 1): #in the algorithm, we can just do it from 2 to the square root of the number you 
        if number % i == 0: #if it can (integer) divide without any remainders
            return False
    return True #otherwise if there are no numbers which are able to divide with the number, then it is prime.

if __name__ == '__main__':
    num = int(input("Number: "))
    function = prime_or_not(num)
    print(function)
