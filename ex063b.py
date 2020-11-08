#conversion table from celsius to farenheit (without lists)

print(f"""
====================================
CELSIUS TEMP:  |   FARENHEIT TEMP :
====================================
""")


for i in range(11):
    n = i + 1
    c = 10 * i 
    f = c * 33.8
    print(f"{n:2d}.{c:5}{f:25.0f}")