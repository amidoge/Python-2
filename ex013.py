PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
TOONIE = 200
change = input('How many cents do I need to pay you back?')
change = int(change)

toonie_amount = change // TOONIE #this will not give me a float
extra = change % TOONIE
loonie_amount = extra // LOONIE
extra = extra % LOONIE
quarter_amount = extra // QUARTER
extra = extra % QUARTER 
dime_amount = extra // DIME
extra = extra % DIME
nickel_amount = extra // NICKEL
extra = extra % NICKEL
penny_amount = extra // PENNY
extra = extra % PENNY
print(f'''
To get {change} cents:
You would need...
{toonie_amount} toonies,
{loonie_amount} loonies,
{quarter_amount} quarters,
{dime_amount} dimes,
{nickel_amount} nickels,
and {penny_amount} pennies''')