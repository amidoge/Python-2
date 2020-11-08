#Is it a valid triangle?

'''
A triangle is valid if sum of its two sides is greater
than the third side. If three sides are a, b, and c, then
three conditions should be met.
'''
def valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False 

if __name__ == '__main__':
    print(valid_triangle(1,4,5))