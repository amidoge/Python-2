groups = 0
number = 0
while True:
    value = int(input('What is the number? '))
    number += value
    if value == 0:
        break
    groups += 1
try:
    average = number / groups
    print(f"The average of the following numbers is {average:.2f}")
except:
    print("Sorry the first number cannot be 0")