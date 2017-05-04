""" Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
number = int(input("enter the limit"))
def fib_list(number):
    a, b = 1, 2
    sum = 0
    while a < number:
        a, b = b, a+b
        if a % 2 == 0:
            sum = sum + a
    print(sum)


(fib_list(number))
