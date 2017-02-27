"""Consecutive Armstrong Numbers for any range"""
min = int(input("Please Enter the Minimum Value: "))
max = int(input("Please Enter the Maximum Value: "))
consecutive = []
for n in range(min, max + 1):

    s = 0
    ti = 0

    t = n
    while t > 0:
        ti = ti + 1
        t = t // 10

    t = n
    while t > 0:
        d = t % 10
        s = s + (d ** ti)
        #print(s)
        t //= 10

    if n == s:
        consecutive.append(s)
        lol = s + 1
        lo = s + 1
        si = 0
        times = 0
        while lol > 0:
            times = times + 1
            lol= lol // 10

        lol = s + 1
        while lol > 0:
            di = lol % 10
            si = si + (di ** times)
            # print(s)
            lol //= 10
            if lo == si:
                print("yes,", n, lo)

print(consecutive)
