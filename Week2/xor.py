a = 10
b = 20

c = (a ^ b)
b = b ^ c
a = a ^ c

print(b,a)
#without using a variable