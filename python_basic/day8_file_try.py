with open("hello.txt","w") as file:
    file.write("Hello Python")
with open("hello.txt","r") as file:
    content = file.read()
print(content)

import json
student = {
    "name" : "培瑞",
    "age" : 20,
    "score" : 95
}
with open("student.json","w") as file:
    json.dump(student,file)

import json
with open("student.json","r") as file:
    student = json.load(file)
print(student)
print(student["name"])
print(student["score"])

try:
    age = int(input("请输入年龄："))
except:
    print("请输入数字")