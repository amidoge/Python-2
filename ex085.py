#Int to Ordinal

def converter(num):
    ordinal_nums = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    return ordinal_nums[num - 1]

if __name__ == '__main__':
    num = int(input("Number: "))
    ordinal = converter(num)
    print(ordinal) 
