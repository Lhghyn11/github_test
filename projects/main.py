#只负责菜单
import student

student.load_students()

while True:

    print("======学生管理系统======")
    print("1.添加学生")
    print("2.查看学生")
    print("3.删除学生")
    print("4.修改成绩")
    print("5.退出")

    choice = input("请选择：")
    
    if choice == "1":
        student.add_student()
    
    elif choice == "2":
        student.show_students()
    
    elif choice == "3":
        student.delete_student()

    elif choice == "4":
        student.update_student()

    elif choice == "5":
        #student.save_students()因为删除 添加 修改后都保存了，这里退出就不用保存了
        break
    
    else:
        print("输入错误")

