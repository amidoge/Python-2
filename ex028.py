# find out the wind chill index
air_temparature = float(input('What is the air temparature (°C)?'))
wind_speed = float(input('What is the speed of the wind (km/h)? '))

wci = 13.12 + 0.6215 * air_temparature - 11.37 * wind_speed ** 0.16 + 0.3965 * air_temparature * wind_speed ** 0.16
wci = round(wci)
print(f'The wind chill is {wci}°C ')