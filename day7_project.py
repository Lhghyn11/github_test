students = []
def add_student():
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    student = {
        "name" : name,
        "age" : age,
        "score" : score
    }
    students.append(student)
    print("添加成功")

def show_students():
    for student in students:
        print(f"姓名：{student['name']} 年龄：{student['age']} 成绩：{student['score']}")

def delete_student():
    name = input("请输入删除学生的名字：")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("删除成功")
            break
        else:
            print("没有找到该学生")

def update_student():
    name = input("请输入修改学生的姓名：")
    for student in students:
        if student["name"] == name:
            score = int(input("请输入新的成绩："))
            student["score"] = score
            print("修改成功")
            break

while True:
    print("======学生管理系统======")
    print("1.添加学生")
    print("2.查看学生")
    print("3.删除学生")
    print("4.修改成绩")
    print("5.退出")

    choice = input("请选择：")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        break

    else:
        print("输入错误")