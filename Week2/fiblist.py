"""Fibonacci sequence under 1000"""
def fib_list(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
fib = fib_list(1000)
print(fib)