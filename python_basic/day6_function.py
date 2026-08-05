def greet(name):
    print(f"你好 {name}")
greet("张三")
greet("李四")

def add(a, b):
    print(a+b)
add(10,20)

def add(a,b):
    return a+b
result = add(10,20)
print(result)

def get_info():
    name = "培瑞"
    age = 20
    return name, age
name, age = get_info()
print(name)
print(age)

a = int(input("输入第一个数字: "))
b = int(input("输入第二个数字: "))
operator = input("输入运算符（+、-、*、/）: ")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "除数不能为零"
    return a/b
if operator == "+":
    result = add(a,b)
    print(result)
elif operator == "-":
    result = subtract(a,b)
    print(result)
elif operator == "*":
        result = multiply(a,b)
        print(result)
elif operator == "/":
        print(divide(a,b))
else:
    print("无效的运算符")