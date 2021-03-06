import csv
import json
import gzip

paths = "/home/ubuntu/Downloads/Vote.txt"
with open(paths,'rb') as something, open("gzip.txt", 'wb') as out_put:
    sout = gzip.GzipFile(something)

#CSV File
with open("/home/ubuntu/Downloads/Vote.txt", 'r') as path:
    reader = csv.reader(path, dialect="excel-tab")

#JSON File
data = {}
with open('json.txt', 'w') as outfile, open(paths, "r") as f:
    for line in f:
        sp = line.split()
        data.setdefault("data", []).append({"user_id": sp[0], "movie_id": sp[1], "rating": sp[2], "junk": sp[3], "timetsmap": sp[4]})
    json.dump(data, outfile)
#print(data)
