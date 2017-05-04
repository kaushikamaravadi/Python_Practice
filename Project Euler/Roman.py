roman = (('M', 1000),
         ('CM', 900),
         ('D',  500),
         ('CD', 400),
         ('C',  100),
         ('XC', 90),
         ('L',  50),
         ('XL', 40),
         ('X',  10),
         ('IX', 9),
         ('V',  5),
         ('IV', 4),
         ('I',  1))

def toRoman(n):
    result = ""
    for num, integer in roman:
        #print(num, integer)
        while n >= integer:
            result = result + num
           # print(result)
            n = n - integer
            print(n, integer)
    return result
print(toRoman(777))

