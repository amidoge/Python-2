LITRES_PER_HUNDRED_KM = 235.214583
try:
    miles_per_gallon = input('How many miles per gallon were you driving?')
    miles_per_gallon = float(miles_per_gallon)
    litres_per_hundred_km = LITRES_PER_HUNDRED_KM * miles_per_gallon
    print(f'In Canada, {miles_per_gallon:.0f} miles per gallon is equivalent to {litres_per_hundred_km} litres per hundred kilometers.')
except ValueError:
    print('Please type in an answer!')