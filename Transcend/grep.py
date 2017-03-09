"""grep"""


import os

find = input("enter anything you want to search")
count = 0
path = '/home/ubuntu/workspace/Python_Practice/Transcend'
for root, dirs, files in os.walk(path):
    for name in files:
        file_open = open(os.path.join(root,name)).read()
        if find in file_open:
            count += 1

print(count)
   # for name in dirs:
   #     print(os.path.join(root, name))
