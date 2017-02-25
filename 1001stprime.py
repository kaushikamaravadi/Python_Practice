import math
def iprime(n):
    if n < 2:
        return ("nothing")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nprime(n):
    npr = 0
    prime = 1

    while npr < n:
        prime = prime + 1
        if iprime(prime):
            npr += 1
    return prime

print(nprime(10001))
