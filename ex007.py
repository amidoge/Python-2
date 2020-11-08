print('\nThis program is going to give you the sum of 1 to the number you want or n\n\nAll you need to do is put in an integer greater than 1, and you would get your sum.')
n = input('\nWhat does n equal?\n')
n = int(n)
if n < 0:
    print('Sorry, but n needs to be a positive integer.')
else:
    sum = n * (n + 1) / 2
    print(f'The sum from 1 to {n} is {sum}')