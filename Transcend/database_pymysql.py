import pymysql

db = pymysql.connect(user='user', password='password', database='database_name')
cursor = db.cursor()
cursor.execute("Your Query")
data = cursor.fetchall()
for row in data:
    print(row)
print("Database version : %s " % data)
db.cursor.close()
db.close()
