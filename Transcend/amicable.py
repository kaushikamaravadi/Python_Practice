"""Amicable Numbers"""

def amicable_numbers(x, y):
    sumx = 0
    sumy = 0
    for i in range(1, x):
        if x % i == 0:
            sumx += i

    for k in range(1, y):
        if y % k == 0:
            sumy += k

    return sumx == y and sumy == x

n1 = int(input('Enter any number'))
n2 = int(input('Enter any number'))

if amicable_numbers(n1, n2):
    print('amicable')

else:
    print('not amicable')
