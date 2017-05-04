import mysql.connector

cnx = mysql.connector.connect(user='root', password='austere', database='dbo')
cursor = cnx.cursor()
query = ("select name from tblemployees")
print(cursor.execute(query))
cursor.close()
cnx.close()
