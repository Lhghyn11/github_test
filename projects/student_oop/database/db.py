import sqlite3

from models.student import Student

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("students.db")#连接数据库
        self.cursor = self.conn.cursor()

        self.create_table()#创建数据表


#创建表的方法
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            score INTEGER
        )
        """)

        self.conn.commit()  

#添加学生
    def add_student(self, student):
        self.cursor.execute(
            """
            INSERT INTO students(name, age, score)
            VALUES(?,?,?)
            """,
            (student.name, student.age, student.score)
        )

        self.conn.commit()

#获取学生
    def get_students(self):
        self.cursor.execute(
            "SELECT id,name,age,score FROM students"#告诉sqlite从表中取出数据
        )

        rows = self.cursor.fetchall()

        print("数据库原始数据：", rows)#

        students = []

        for row in rows:
            student = Student(
                row[1],
                row[2],
                row[3],
                row[0]#传给student_id
            )

            students.append(student)

        return students

    #修改数据库里的学生成绩
    def update_student(self, student_id, score):
        self.cursor.execute(
            """
            UPDATE students
            SET score = ?
            WHERE id = ?
            """,
            (score, student_id)
        )

        self.conn.commit()


    #删除学生
    def delete_student(self, student_id):
        self.cursor.execute(
            """
            DELETE FROM students
            WHERE id = ?
            """,
            (student_id,)
        )

        self.conn.commit()