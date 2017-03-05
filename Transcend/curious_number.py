"""Curious Number"""

import math

solution = []
for num in range(10, 3000000):
    duplicate = str(num)
    check = 0
    for n in duplicate:
        check = check + math.factorial(int(n))
    if check == num:
        solution.append(num)
print(sum(solution))
