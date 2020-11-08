# tell name of person on banknote by input from the user
import sys
banknote = int(input('What is the value of the banknote? '))
franklin = 100
grant = 50
jackson = 25
hamilton = 10
lincoln = 5
washington = 1
person = ''
if banknote == franklin:
    person = 'Benjamin Franklin'
elif banknote == grant:
    person = 'Ulysses S Grant'
elif banknote == jackson:
    person = 'Andrew Jackson'
elif banknote == hamilton:
    person = 'Alexander Hamilton'
elif banknote == lincoln:
    person = 'Abraham Lincoln'
elif banknote == washington:
    person = 'George Washington'
else:
    print(f'Sorry, there is no such banknote in the U.S with the value of {banknote}.')
    sys.exit()
print(f'The person on the ${banknote} bill is {person}')