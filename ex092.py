#Is a number prime?

'''
-Greater than 1
-Only divisible by one and itself
-Return True if prime, False if not
-Only runs in the main file
'''

def prime_or_not(number):
    #loop that runs until half the number
    if number > 1:
        if number == 2:
            return True
        else:
            for i in range(number):
                if i == 0 or i == 1: #Since there would be a ZeroDivisionError and any number can divide with 1
                    continue
                elif number % i == 0: #if it can (integer) divide without any remainders
                    return False
                else:
                    return True #if there were no clean divisions then that means that it has to be prime because nothing was able to divide with it
    return False

if __name__ == '__main__':
    num = int(input("Number: "))
    function = prime_or_not(num)
    print(function)