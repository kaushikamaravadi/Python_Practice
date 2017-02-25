"""Factorial of a number(iteration and recursion)"""
def facto(num):
    n = 1
    for i in range(2, num+1):
        n = n * i
    return n
print(facto(4))


def fact(n):
    if n == 1:
        return (n)
    else:
        return (n * fact(n-1))

print(fact(4))
