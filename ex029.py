# calculate a degree in °C and then convert to °F and Kelvin

celsius = float(input('What is the temparature in °C? '))
farenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
print(f'''
{celsius}°C is equivalent to...
{farenheit}°F, and
{kelvin}K ''')