# Regular Expressions
# Raw Strings
# Searching
# character class
# anchors
# metacharacters
# Quantifiers

import re
p = re.compile('[a-z]+')
print(p)
m = p.match("tempo")
print(m)

p = re.compile('\d+')
ml = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(ml)


greetings = "hello Ubuntu"
print(re.search(r"u", greetings))
re.search(r'[aeiou]', greetings)
print(re.search(r'[aeiou]', "rhthm"))
print(re.search(r'[a-zA-Z0-9_]', "2e_"))
print(re.search(r'^a', "ashritha"))
print(re.search(r'a$', "mounika"))
print(bool(re.search(r'^a.*z$', "abz")))

print(re.search(r'\d', greetings))
print(re.search(r'\d+', "101"))
print(re.search(r'\D', '100'))
print(re.search(r'^\w*$', 'hello'))

print(re.search(r'^[A-Za-z0-9_]*$', 'hello40'))
print(re.search(r'^\s*$', " _\n"))
print(re.search(r'^\s*$', " "))


