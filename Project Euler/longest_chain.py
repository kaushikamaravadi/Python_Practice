"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
for example: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Which starting number, under one million, produces the longest chain?
"""
import time
x = 0
d = 0
start_time = time.clock()
for i in range(1,1000000 + 1):
    #print(i)

    n = i
    t = 0
    while n > 1:
        if n % 2 == 0:
            #print("yes", n)
            n = n // 2
            t = t + 1

        if n == 1.0:
            #print("n  is  1")
            t = t + 1
            if t > x:
                x = t
                d = i
            break

        if n % 2 != 0:
            #print("no", n)
            n = 3 * n + 1
            t = t + 1

    #print(t,i)
print(x,d)
run_time = time.clock() - start_time
print("Run time = ", run_time)











