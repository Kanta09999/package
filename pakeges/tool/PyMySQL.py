from tool.imports import *
"""-------------------------------------------------------------------sql----------------------------------------------------------------------------------"""
class PyMySQL:
    global conn, cursor, mSql
    def __init__(self, mHost='127.0.0.1', mPort=3306, mUser='root', mPassword='', mDb='sode', mCharset='utf8'):
        self.conn = pymysql.connect(host=mHost,
                           port=mPort,
                           user=mUser,
                           password=mPassword,
                           db=mDb,
                           charset=mCharset,
                           cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor();

    def costomSet(self, costomSql):
        self.mSql = costomSql

    def costomQuery(self, values):
        self.cursor.execute(self.mSql, values)
        self.conn.commit()

    def costomExe(self, values):
        self.cursor.execute(self.mSql, values)

    def exeSelect(self, sql) :
        self.cursor.execute(sql)

    def exeInsert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def exeUpdate(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def getData(self):
        dbdata = self.cursor.fetchall()
        return dbdata