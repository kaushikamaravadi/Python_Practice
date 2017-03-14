"""Fibo using Generator"""

import itertools

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibo(generator, n):
    for i in range(n):
        yield next(generator)

print(list(fibo(fibonacci(), 10)))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

print(list(itertools.islice(fib(), 10)))
