#Approximate Pi

'''
Objective: Program that displays 15 approximations of pi
Steps:
-The first should make use of oly the first term from the infinite series
-Each one after should include one more term than before
'''

divider1 = 2
divider2 = 3
divider3 = 4

pi = 3
for i in range(15):
    round_count = i + 1
    formula_round = 4 / (divider1 * divider2 * divider3)
    if i % 2 == 1:
        pi += formula_round
    elif i % 2 == 0:
        pi -= formula_round
    
    print(f"Round #{round_count:2d}: {pi}\n")
    divider1 += 2
    divider2 += 2
    divider3 += 2
    