"""wc command in Python"""


filename = "/home/ubuntu/daily_log/kaushik_03_09_2017.txt"
file_open = open(filename, "r+").read()
char = len(file_open)
lines = file_open.count("\n")
words = file_open.split(None)
print(char, lines, len(words))
