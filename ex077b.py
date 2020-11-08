# let binary (variable) be the number to convert to to decimal number
# iterate through each bit in binary. for each digit, multiply it with the placing
# sum up the result

binary = input("Binary: ")
total = 0
for i in range(len(binary)):
    num = int(binary[-i - 1]) * (2 ** i) #no list!
    total += num

print(f'Converted Decimal: {total}')


