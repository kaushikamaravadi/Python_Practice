"""Find the sum of the digits in the number 100!
"""
def facto(num):
    n = 1
    for i in range(2, num+1):
        n = n * i
        #print(n)
        addition = sum([int(i) for i in str(n)])
    return "sum of ", n , "is ", addition
print(facto(100))