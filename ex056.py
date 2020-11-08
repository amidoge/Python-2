#cell phone bill
#50 minutes air time
#50 text messages for 15 dollars a month
#additional minute of air time costs 0.25 dollars
#additional text messages costs 0.15 dollars each
#0.44 dollars to support 911 call centers
#entire bill including 911 is subject to 5% tax
air_time = int(input('How much air time has been used this month (minutes)?'))
text_messages = int(input('How many text messages have been sent this month?'))
base = 15.00
additional_air_time_charge = (air_time - 50) * 0.25
additional_text_messages_charge = (text_messages - 50) * 0.15
nine_one_one = 0.44
sales_tax = (base + additional_air_time_charge + additional_text_messages_charge + nine_one_one) / 100 * 5
total_cost = base + additional_air_time_charge + additional_text_messages_charge + nine_one_one + sales_tax
print(f'''
==================CELL PHONE BILL===================
BASE = ${base:44.2f}
ADDITIONAL AIR TIME = ${additional_air_time_charge:29.2f}
ADDITIONAL TEXT MESSAGES = ${additional_text_messages_charge:24.2f}
911 CHARGE = ${nine_one_one:38.2f}
SALES TAX = ${sales_tax:.2f}
==================TOTAL COST========================
TOTAL COST = ${total_cost:.2f}
''')

print(f'================================BILL==========================')
print(f'{"BASE":26s} :  {"$":>16s} {base:14.2f}')
print(f'{"ADDITIONAL AIR TIME":26s} :  {"$":>16s} {additional_air_time_charge:14.2f}')
print(f'{"ADDITIONAL TEXT MESSAGES":26s} :  {"$":>16s} {additional_text_messages_charge:14.2f}')
print(f'{"911 CHARGE":26s} :  {"$":>16s} {nine_one_one:14.2f}')
print(f'{"SALES TAX":26s} :  {"$":>16s} {sales_tax:14.2f}')
print(f'===========================TOTAL COST=========================')
print(f'{"TOTAL COST":26s} :  {"$":>16s} {total_cost:14.2f}')