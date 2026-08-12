import sqlite3


conn = sqlite3.connect("students.db")

cursor = conn.cursor()#创建一个：数据库操作对象


# 创建表
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    score INTEGER
)
""")


# 插入学生
cursor.execute(#执行sql
    """
    INSERT INTO students(name, age, score)
    VALUES(?,?,?)
    """,
    ("培瑞",20,95)
)


conn.commit()


print("学生添加成功")

#查看数据
cursor.execute(
    "SELECT * FROM students"
)


students = cursor.fetchall()


for student in students:
    print(student)



conn.close()