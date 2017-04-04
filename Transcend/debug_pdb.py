import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for val in values:
    mysum = 0
    mysum = mysum + val
    pdb.set_trace()

print(mysum)
