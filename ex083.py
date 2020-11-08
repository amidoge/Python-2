#SHIPPING CALCULATOR

BASE = 10.95
PER_SUB = 2.95

'''
Online Retailer Provides:
$10.95 as a base for first item
$2.95 per items after that.
'''

def calc(items):
    total = 0
    total += BASE
    total += (items - 1) * PER_SUB
    return total

if __name__ == '__main__':
    def main():
        items = int(input("Number of items? "))
        total = calc(items)
        print(f'{total:.2f}')
    main()
