from database.db import Database


db = Database()

print("数据库对象创建成功")


db.conn.close()