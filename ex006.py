TIP_PERCENTAGE = 0.18
TAX_PERCENTAGE = 0.07
meal = input('How much did your meal cost?')
meal = float(meal)
tip = TIP_PERCENTAGE * meal
tax = TAX_PERCENTAGE * meal
total = meal + tip  + tax
print(f'''
Total Cost of Food ($):
Subtotal: ${meal:6.2f}
Tip:      ${tip:6.2f}  
Tax:      ${tax:6.2f}
TOTAL:    ${total:6.2f}
''') #the 6 in the format is so that it occupies 6 spaces so that way it is aligned
#you can continue to do exercises 7, 8 , 9 , 10, 13, 14, 21, 22, 24, 25, 26 , 27, 33 