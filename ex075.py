#Greatest Common Divisor

n = int(input("First Number: "))
m = int(input("Second Number: "))

'''
The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m. There are several algorithms that can be
used to solve this problem, including:

Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
    Decrease the value of d by 1
Report d as the greatest common divisor of n and m
'''
d = min(n, m)
while m % d != 0 or n % d != 0:
    #print(d) #Just checking what is going on
    d -= 1
print(f"{d} is the greatest common divisor of {n} and {m}!")

