"""Divide by 2 Algorithm"""
n = int(input("enter any integer"))
k = []
while (n > 0):
    p = n % 2
    #print(p)
    k.append(p)
    n = n // 2
print(k[::-1])



