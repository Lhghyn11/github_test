import json

from student import Student

class StudentManager:

    def __init__(self):
        self.students = []

    def load_students(self):
    #global students

        try:
            with open("students.json", "r") as file:
                #self.students = json.load(file)
                data = json.load(file)
                for item in data:
                    student = Student(
                        item["name"],
                        item["age"],
                        item["score"]
                    )
                    self.students.append(student)


                print("读取成功")

        except FileNotFoundError:
            self.students = []

            print("没有找到数据文件")


    def save_students(self):
    #print("保存的数据：", students)
        data = []
        for student in self.students:
            data.append(
                {
                    "name":student.name,
                    "age":student.age,
                    "score":student.score
                }
            )

        with open("students.json", "w") as file:
            json.dump(data, file)

        print("保存完成")


    def add_student(self):

        name = input("请输入姓名：")
        try:
            age = int(input("请输入年龄："))
            score = int(input("请输入成绩："))
        except ValueError:
            print("年龄和成绩必须输入数字")

            return False

        #student = {
        #    "name": name,
        #    "age": age,
        #    "score": score
        #}这是字典

        student = Student(name,age,score)#这是Student对象

        self.students.append(student)#等价于manager.students.append(student)

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
                self.students.remove(student)
                print("删除成功")
                return True
            
        print("没有找到该学生")
        return False


    def update_student(self):
        name = input("请输入修改学生的姓名：")

        for student in self.students:
            #if student["name"] == name:
            if student.name == name:

                try:
                    score = int(input("请输入新的成绩："))

                except ValueError:
                    print("成绩必须输入数字")
                    return False
                
                #student["score"] = score
                #student.score = score
                #student.update_score(score)
                result = student.update_score(score)
                if result:
                    print("修改成功")
                    return True
                else:    
                    return False
            
        print("没有找到该学生")

        return False