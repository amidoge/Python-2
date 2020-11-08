#convert units of pressure
#convert kilopascals to pounds per square inch, millimeters of mercury, and atmospheres
kpa = float(input('How much kilopascals do you want us to calculate? '))
psi = kpa / 6.89475729
mmhg = kpa / 0.1333223684
atm = kpa / 101.325
print(f'''
For {kpa} kilopascals, there are... 
\n{psi:.5f} pounds per square inches,\n 
{mmhg:.5f} millimeters of mercury,\n
and {atm:.5f} atmospheres.\n'''
)