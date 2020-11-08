#Binary to Decimal
'''
Program:
Converts Binary (base 2) to decimal (base 10).
Reads a binary number as a string.
Compute the equivalent decimal number.

We do this by processing each digit in the binary number.

Display the equivalent decimal number with an appropriate message
'''
#NOTE: Decimal means whole number (base 10)
binary = input("Binary: ")
#making a list for the binary digits in base 10
binary_digits = []
for i in range(len(binary)): #when each digit is counted then I want to add a base 10 binary_digit so I can count how many there actually are.
    binary_digits.append(2 ** i)

total = 0 #this is for the total
for i in range(len(binary_digits)): #this is going to make us check if it is a zero and then add to a total. Starts from end of bianry number
    if binary[-i - 1] == '0':
        pass
    elif binary[-i - 1] == '1':
        total += binary_digits[i] #since the first digit of the list is the last digit of the string, we must have an -i - 1 which is -1 and an i which would be 1 and so on.

print(f'Converted Number: {total}')
