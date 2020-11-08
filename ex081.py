#Computing a Hypotenuse
from math import sqrt

#function
def hypotenuse(side1, side2):
    #formula to find c
    c = sqrt(side1 ** 2 + side2 ** 2)
    return c 


if __name__ == '__main__':

    #main function
    def main():
        a = int(input("Length of short side:"))
        b = int(input("Length of short side:"))
        c = hypotenuse(a, b) #calculating the hypotenuse using earlier function
        print(f"{c:.2f}")

    main() #caling function

