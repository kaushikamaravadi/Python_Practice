"""Factors of a number"""
number = int(input("entger any integer"))

for i in range(1 , number + 1):
    if number % i == 0:
        l = []
        l.append(i)
        print()

