#conversion table from celsius to farenheit

celsius_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
farenheit_list = []

for i in range(10):
    farenheit_list.append(celsius_list[i] * 33.8)

print(f"""
====================================
CELSIUS TEMP:  |   FARENHEIT TEMP :
====================================
""")


for i in range(10):
    x = i + 1
    print(f"{x:2d}.{celsius_list[i]:5}{farenheit_list[i]:25.0f}")