#conversion table from celsius to farenheit (making part b better)

print(f"""
====================================
CELSIUS TEMP:  |   FARENHEIT TEMP :
====================================
""")

for c in range(10, 101, 10):
    f = c * 33.8
    n = c // 10
    print(f"{n:2d}.{c:5}{f:25.0f}")