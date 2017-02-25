"""Find the largest palindrome made from the product of two 3-digit numbers"""
g = []
for i in range(100,999):
    for j in range(100,999):
        k = i * j
        kiki = str(k)[::-1]
        if str(k) == str(kiki):
            g.append(k)
print(max(g),"this is the largest palindrome")
