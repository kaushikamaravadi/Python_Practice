"""In largest mersenne prime number find number of occurrences of
  0’s 1’s 2’s 3’s 4’s 5’s 6’s 7’s 8’s 9’s"""
"""Using Counter"""
from collections import Counter

file = open("/home/kaushik/mersene.txt", "r")
line = file.read()
kiki = (line.replace('\n',''))

"""Without using Counter"""

print(Counter(kiki))
total = dict((x,kiki.count(x)) for x in set(kiki))
print(total)
