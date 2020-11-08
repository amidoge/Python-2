BREAD = 3.49
day_old_breads = int(input('How many day old breads would you like to purchase?'))
discount = (BREAD / 100) * 60
regular_price = BREAD * day_old_breads
total = regular_price - discount

print(f'''
Total Cost of Purchase ($):
Regular Price:  ${regular_price:5.2f},
Discount:       ${discount:5.2f},
______________________________________
Total Price:    ${total:5.2f}

''')