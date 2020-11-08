#Prime Factors

'''
The prime factorization of an integer, n, can be determined using the following steps:

Initialize factor to two
While factor is less than or equal to n do
    If n is evenly divisible by factor then
        Conclude that factor is a factor of n
        Divide n by factor using integer division
    Else
        Increase factor by one
'''

#Read an int from user. Cannot be less than two otherwise make an error.
#Otherwise, it should print the prime factorization of the number.

n = int(input("Number (cannot be less than 2): "))
if n < 2:
    print("Sorry, but int must be 2 or greater.")
else:
    factors = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor #so that we can eliminate that prime number and move on to the next one until it can no longer be divided by a prime number
        else:
            factor += 1
    for i in range(len(factors)):
        print(factors[i])