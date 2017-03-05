"""Pandigital Number"""

import time

start = time.time()
n = int(input("enter the upper limit"))
def pandigit(n):


    largest = 0

    for i in range(1, n):
        mul = ""
        # noinspection PyRedeclaration
        first = 1
        while len(mul) < 9:
            mul = mul + str(i * first)
            first = first + 1

        if len(mul) == 9 and len(set(mul)) == 9 and ('0' not in mul):
            if int(mul) > largest:
                largest = int(mul)

    return (largest)

print(pandigit(n))
end = time.time()
print(end - start)

