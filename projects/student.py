import json

students = []


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

            print("函数里面：", students)

    except FileNotFoundError:
        students = []
        print("没有找到数据文件，创建新的学生列表")


def save_students():
    print("保存的数据：", students)

    with open("students.json", "w") as file:
        json.dump(students, file)

    print("保存完成")


def add_student():
    name = input("请输入姓名：")

    try:
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
    except:
        print("年龄和成绩必须输入数字")
        return #如果输入错误，停止当前函数，不会继续append

    student = {
        "name" : name,
        "age" : age,
        "score" : score
    }

    students.append(student)

    save_students()

    print("添加成功")


def show_students():
    for student in students:
        print(f"姓名：{student['name']} 年龄：{student['age']} 成绩：{student['score']}")

def delete_student():
    name = input("请输入删除学生的名字：")

    for student in students:
        if student["name"] == name:
            students.remove(student)

            save_students()

            print("删除成功")
            return #找到并删除，直接结束函数

    print("没有找到该学生")  #整个循环都没找到，执行最后一句  


def update_student():
    name = input("请输入修改学生的姓名：")
    for student in students:
        if student["name"] == name:
            try:
                score = int(input("请输入新的成绩："))

            except ValueError:
                print("成绩必须输入数字")
                return

            student["score"] = score

            save_students()

            print("修改成功")
            return

    print("没有找到该学生")