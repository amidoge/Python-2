#Parity Bits
#using the count() function to count instead of itering through it
even = False
'''
A parity bit is a way to detect errors in a 
data through a unreliable connection.


If the parity bit is odd or even, meaning 
if there are an odd number of 1's or even 
number of 1's, then it will either be 0
or 1. The input is an 8 bit number meaning
that it is a total of eight 0's and 1's.
'''

print('''
11111111111111111111111111111
    PARITY BIT DETECTOR
00000000000000000000000000000
''')

eight_bit_num = input("Enter an 8 bit number: ") #not going to be int because I need to iter through it

count = eight_bit_num.count('1')
if count % 2 == 0:
    even = True

if even:
    print("Parity Bit: 1")
else:
    print("Parity Bit: 0")
