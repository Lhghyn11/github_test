from database.db import Database
from models.student import Student
#from models.student import Student简化，不需要row[]

db = Database()

#print("数据库对象创建成功")
db.create_table()

student = Student("测试学生", 18, 90)

db.add_student(student)

print("学生添加成功")#增加


db.update_student(12, 88)#修改

print("修改完成")

db.delete_student(12)#删除

print("删除完成")


students = db.get_students()


#print(students)输出是元组
#for row in students:

 #   student = Student(
  #      row[1],
   #     row[2],
    #    row[3]
    #)

for student in students:
    print("ID:", student.id,student.show_info())
    #print(student.show_info())#row[0]是id跳过他。
    #例如row = (12, "测试学生", 18, 90)

db.conn.close()
