"""What is the largest prime factor of the number 600851475143"""
number = int(input("entger any integer"))
factors = []
largest = []
for i in range(1 , number + 1):
    if number % i == 0:
        factors.append(i)
        #print(i)

print(factors)
maximum = max(factors)
print(maximum)
for fact in factors:
    for i in range(2, fact):
        if (fact % i) == 0:
            break
    else:
        largest.append(fact)

print(max(largest))

