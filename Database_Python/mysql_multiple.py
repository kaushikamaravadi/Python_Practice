import pymysql


class Mysql(object):
    # connection = None
    # cur = None

    # dbc = (user='root', password='austere', database='dbo')

    def __init__(self):
        db = pymysql.connect(user='root', password='austere', database='dbo')
        self.cursor = db.cursor()

    def queries(self, sql):
        select = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for row in data:
            print(row)

    def rows(self):
        return self.cursor.rowcount


first = Mysql()
first.queries("select name from tblemployees")
