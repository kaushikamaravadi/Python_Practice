import os
import time
import datetime

path = '/home/ubuntu/workspace/Python_Practice/Transcend'
for root, dirs, files in os.walk(path):
    for name in files:
        file_open = os.path.join(name)
        all = file_open
        print((os.stat(root+"/"+file_open).st_size,os.stat(root+"/"+file_open).st_atime,os.stat(root+"/"+file_open).st_mtime,os.stat(root+"/"+file_open).st_mode,os.stat(root+"/"+file_open).st_gid,os.stat(root+"/"+file_open).st_uid))
