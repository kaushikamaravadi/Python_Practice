"""Find given number is prime or not"""
raw = int(input("enter the limit"))

if raw > 1:
    for i in range(2, raw):
        if (raw % i ) ==0:
            print("it is not a prime")
            print(raw, "is divisible by", i )
            break

        else:
            print("its a prime")

else:
    print("its not a prime anyway")




