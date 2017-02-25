"""the sum of all the primes below two million."""
import time
start_time = time.clock()
def get_primes(n):

    numbers = set(range(n, 1, -1))
    #print(numbers)
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
        #print(primes)
    return (primes)

print(sum(get_primes(2000000)))
run_time = time.clock() - start_time
print("Run time = ", run_time)
