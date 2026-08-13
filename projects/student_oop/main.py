from managers.student_manager import StudentManager

manager = StudentManager()#创建一个SM对象，会自动调用init，现在manager.students就是[]

manager.load_students()#加载学生数据

while True:

    print("======学生管理系统======")
    print("1.添加学生")
    
    print("2.查看学生")
    print("3.删除学生")
    print("4.修改成绩")
    print("5.退出")

    choice = input("请选择：")

    if choice == "1":
        #result = manager.add_student()#python实际上StudentManager.add_student(manager).result被赋值true或false
        manager.add_student()#现在 add_student() 已经负责保存到数据库了。
        #if result:
            #manager.save_students()


    elif choice == "2":
        manager.show_students()这是给students.json准备的


    elif choice == "3":
        #result = manager.delete_student()
        manager.delete_student()
        #if result:
            #manager.save_students()


    elif choice == "4":
        #result = manager.update_student()
        manager.update_student()#内部已经自己负责数据库操作
        #if result:
            #manager.save_students()main.py不应该再负责保存数据


    elif choice == "5":
        break


    else:
        print("输入错误")