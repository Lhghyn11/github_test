score = int(input("请输入成绩："))

if score >= 90:
    print("优秀")
elif score >=80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


username =input("请输入用户名：")
password = input("请输入密码：")
if username == "admin" and password == "123456":
    print("登录成功")
else:
    print("用户名或密码错误")


username = input("请输入用户名：")
password = input("请输入密码：")
if username == "admin":
    if password =="123456":
        print("欢迎进入游戏")
    else:
        print("密码错误")
else:
    print("用户不存在")
