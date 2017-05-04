output = input("enter anything")
empty = ""
for char in output:
    if ord(char) >= 65 and ord(char)<= 90:
        capital = ord(char) + 32
        small = chr(capital)
        empty = empty + small
print(empty)
