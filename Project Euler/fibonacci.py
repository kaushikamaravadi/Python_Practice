"""What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
def fibo():
    a = 0
    b = 1
    while True:
        yield b
        a,b = b,a+b

f = fibo()
print([next(f) for i in range(10)])

f = enumerate(fibo())
x = 0
while len(str(x)) < 1000:
    i,x = next(f)

print(i+1,len(str(x)),x)