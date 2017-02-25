"""Prime numbers under specific interval"""
lower = 1622592
upper = 2000000
for num in range(lower,upper + 1):

   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
