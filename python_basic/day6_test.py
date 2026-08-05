def say_hello():
    print("你好.Python")
say_hello()

def say_hello(name):
    print(f"你好 {name}")
say_hello("张三")
say_hello("李四")

def introduce(name,age):
    print(f"我叫{name},今年{age}岁")
introduce("培瑞",20)

def add(a, b):
    return a+b
result = add(5,3)
print(result)

def get_student():
    name = "培瑞"
    age = 20
    return name,age
name,age = get_student()
print(f"姓名：{name}")
print(f"年龄：{age}")

def introduce(name, age=18):
    print(f"{name}今年{age}岁")
introduce("培瑞")
introduce("培瑞",20)