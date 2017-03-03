"""Sum of all Mersenne Numbers in a text file called mersene.txt"""

file = open("/home/kaushik/mersene.txt", "r")
line = file.read()
kiki = (line.replace('\n',''))
print(sum([int(i) for i in str(kiki)]))

