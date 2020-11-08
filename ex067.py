#Admission Price

'''
Guests of age 2 and below = NO CHARGE
Children between 3-12 = 14.00
Seniors age 65 and above = 18.00
Other Guests = 23.00

1. Read the ages of all guests
2. Blank Line indicates no more guests
3. Print the total admission cost for the group of guests
NOTE: The cost needs to be in 2 decimal places
'''
#INPUT
cost = 0
while True:
    guest_age = input("Age of Guest: ")
    if guest_age == ' ':
        break
    if int(guest_age) <= 2:
        cost += 0
    elif int(guest_age) >= 3 and int(guest_age) <= 12:
        cost += 14.00
    elif int(guest_age) >= 63:
        cost += 18.00
    else:
        cost += 23.00

#OUTPUT
print(f'The total cost of the admission is ${cost:.2f}!')