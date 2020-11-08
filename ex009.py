INTEREST = 0.04
money = input('How much money do you have?')
money = float(money)
interest = INTEREST * money
one_yr = interest + money
interest = INTEREST * one_yr
two_yr = interest + one_yr
interest = INTEREST * two_yr
three_yr = interest +  two_yr
print(f'\nIn one year you will have ${one_yr:.2f} dollars in your savings account.\n')
print(f'\nIn two years you will have ${two_yr:.2f} dollars in your savings account.\n')
print(f'\nIn three years you will have ${three_yr:.2f} dollars in your savings account.\n')