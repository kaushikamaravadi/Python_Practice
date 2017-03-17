"""Fibonacci Using generator"""



import time

start = time.time()
def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for x in fibo(10):
    print(x)
end = time.time()
print(end - start)

