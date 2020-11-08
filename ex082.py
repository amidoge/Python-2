#Taxi Fare
#constants:
BASE = 4.00
PER_METERS = 140
MONEY_PER_METERS = .25
'''
base is 4 dollars
for every another 140 meters traveled is 25 cents
'''

#function that takes distance traveled and returns total fare
def taxi_fare(km):
    extra_pay = (km * 1000 // PER_METERS) * MONEY_PER_METERS #integer division and multiplying it by 25 cents
    total_pay = BASE + extra_pay
    print(total_pay)
    return total_pay
if __name__ == '__main__':
    def main():
        distance_traveled = int(input("Distance Traveled (km): "))
        taxi_fare(distance_traveled)

    main() #calling function

