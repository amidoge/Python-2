#Median of Three Values

def median_finder(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    if a != minimum and a != maximum:
        median = a
    if b != minimum and b != maximum:
        median = b
    else:
        median = c
    return median #return median

if __name__ == '__main__':
    def main():
        a = input("Num: ")
        b = input("Num: ")
        c = input("Num: ")
        median = median_finder(a, b, c)
        print(median)
    main()

