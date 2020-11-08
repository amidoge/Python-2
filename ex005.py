SMALL_DEPOSIT = 0.10
BIG_DEPOSIT = 0.25
small = input('How many small containers do you have?')
big = input('How many big containers do you have?')
big_total = int(big) * BIG_DEPOSIT
small_total = int(small) * SMALL_DEPOSIT
total = small_total + big_total
if len(str(total)) == 3:
    print(f'You get ${total:.2f} back') #the :.2f is going to round to put it to 2 decimal places
elif len(str(total)) == 4:
    print(f'You get ${total} back')
else:
    print('There is an error with your input')
