#import json现在不用json了
#from json import JSONDecodeError#文件被改坏，程序停止

from models.student import Student#里面有check

from utils.input_helper import input_int

from exceptions.student_error import StudentError

from database.db import Database

from repositories.student_repository import StudentRepository

from utils.logger import logger#日志

class StudentManager:

    def __init__(self,repository):
        self.students = []
        #self.db = Database()#新增sqlite
        #self.db = db#database不由我创建，别人给我
        #self.db.create_table()#创建数据表
        self.repository = repository#manager以后只认识学生仓库，不认识sqlite

    def load_students(self):
        print("进入load_students")#测试
    #global students
        #self.students = []#读取前清空student

       #self.students = self.db.get_students()#sqlite
        self.students = self.repository.get_all_students()

        print("从数据库读取成功")
        print("学生数量：", len(self.students))#测试

        #try:没有意义现在不是json文件读取了，这是针对json的try
            #with open("data/students.json", "r") as file:
                #self.students = json.load(file)
                #data = json.load(file)
                #for item in data:
                 #   student = Student(
                  #      item["name"],
                   #     item["age"],
                   #     item["score"]
                    #)
                    #self.students.append(student)
                #print("读取成功")

        #except FileNotFoundError:
            #self.students = []
            #print("没有找到数据文件")

        #except JSONDecodeError:
            #self.students = []
            #print("数据文件格式错误")


    #def save_students(self):以前负责studentmanager到students.json现在已经完全没用了
    #print("保存的数据：", students)
        #data = []
        #for student in self.students:
            #data.append(
                #{
                 #   "name":student.name,
                  #  "age":student.age,
                  #  "score":student.score
                #}
            #)

        #with open("data/students.json", "w") as file:
         #   json.dump(data, file)

        #print("保存完成")


    def add_student(self):

        name = input("请输入姓名：")

        #if name.strip() == "":
            #print("姓名不能为空")
            #return False#已经接入了check_name
        
        age = input_int("请输入年龄：")#以前通过try自己处理，现在交给input_put

        score = input_int("请输入成绩：")   

        #if age <= 0:
            #print("年龄必须大于0")
            #return False
            
        #student = {
        #    "name": name,
        #    "age": age,
        #    "score": score
        #}这是字典

        try:
            student = Student(name,age,score)#这是Student对象

        except StudentError as e:
            print(e)
            return False#告诉调用者，这次操作失败了

        #self.db.add_student(student)#负责：student对象→sqlite
        self.repository.add_student(student)

        self.students.append(student)#等价于manager.students.append(student)

        #print("添加成功")
        logger.info(f"添加学生:{student.name}")
        print("添加成功")

        return True


    def show_students(self):
        for student in self.students:
            #print(f"姓名：{student.name} 年龄：{student.age} 成绩：{student.score}")
            #student.show_info()
            print(student.show_info())


    def delete_student(self):
        name = input("请输入删除学生的名字：")

        for student in self.students:
            #if student["name"] == name:
            if student.name == name:

                #self.db.delete_student(student.id)#核心就是增加这一句
                self.repository.delete_student(student.id)

                self.students.remove(student)
                #print("删除成功")
                logger.info(f"删除学生:{student.name}")
                print("删除成功")
                
                return True
            
        print("没有找到该学生")
        return False


    def update_student(self):
        name = input("请输入修改学生的姓名：")

        for student in self.students:
            #if student["name"] == name:
            if student.name == name:

                #try:
                    #score = int(input("请输入新的成绩："))

                #except ValueError:
                    #print("成绩必须输入数字")
                    #return False因为已经调用input_put了，不用自己处理
                score = input_int("请输入新的成绩：")
                
                #student["score"] = score
                #student.score = score
                #student.update_score(score)
                #result = student.update_score(score)
                try:
                    student.update_score(score)

                #except ValueError as e:
                except StudentError as e:
                    print(e)
                    return False
                
                #self.db.update_student(student.id, score)
                self.repository.update_student(student.id,score)
                
                #print("修改成功")
                logger.info(f"修改学生成绩:{student.name}->{score}")
                print("修改成功")

                return True

            
        print("没有找到该学生")

        return False