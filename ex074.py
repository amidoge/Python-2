#Multiplication Table
for i in range(11):
    if i != 0:
        for n in range(11):
            if n != 0:
                print(f"{n * i:3d}", end=" ")
                n += 1
    print("\n")
    i += 1

