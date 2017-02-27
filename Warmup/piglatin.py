"""English to Pig Latin"""
english = input("enter the statement")
pig = "ay"
li = english.split()
piglatin = []
for i in li:
    latin = i[1:]
    k = i[0] + pig
    #print(k)
    final = latin + k
    piglatin.append(final)
print(" ".join(piglatin))
# do not use split