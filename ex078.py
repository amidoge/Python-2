result = ''
q = int(input('Decimal: '))
while q != 0:
    r = q % 2
    r = str(r)
    result = r + result #add it to the string
    q = q // 2

print(f"Converted Binary: {result}")