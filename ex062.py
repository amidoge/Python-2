#60% off sale
#create a loop that shows a table the before and after prices of the discount

product_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

discounts = []
final_prices = []
number = 0

#LOOP FOR DISCOUNTS
for i in product_prices:
    number = i / 100 * 60
    discounts.append(number)

#LOOP FOR FINAL PRICES
for i in range(5):
    number = product_prices[i] - discounts[i]
    final_prices.append(number)
    
#LOOP FOR PRINTING TABLE
'''
for i in range(5):
    product_num = i + 1
    print(f'Product{product_num} starting price: ${product_prices[i]:.2f}. Discount: ${discounts[i]:.2f}. Final Price: ${final_prices[i]:.2f} \n')
'''
symbol = '$'
print(f'''
===================================
STARTING PRICE:        FINAL PRICE:
===================================
${product_prices[0]:5.2f}{symbol:10s}{final_prices[0]:17.2f},
${product_prices[1]:5.2f}{symbol:10s}{final_prices[1]:17.2f},
${product_prices[2]:5.2f}{symbol:10s}{final_prices[2]:17.2f},
${product_prices[3]:5.2f}{symbol:10s}{final_prices[3]:17.2f},
${product_prices[4]:5.2f}{symbol:10s}{final_prices[4]:17.2f},
''')