#Next Prime
from ex092b import prime_or_not
'''
Create a function called nextPrime which finds and returns
the first prime number larger than some integer, n. The
value of n will be passed to the function as it's only
parameter. Include a main program that reads an integer
from the user and displays the first prime number larger
than the entered value. Import and use your solution
to Exercise 92 while completing this exercise.
'''
def nextPrime(n):
    next_num = 1 #this is going to increase if the number after n is not a prime number
    while prime_or_not(n + next_num) == False: #this will keep going if the next number is not a prime number
        next_num += 1 #i want to increase the next num which will make it go from n + 1 to n + 2 and so on
    return n + next_num #if the loop ends it means that it has found the prime number. So i want to return it
    
if __name__ == '__main__':
    user_input = int(input("Number: "))
    value = nextPrime(user_input)
    print(value)