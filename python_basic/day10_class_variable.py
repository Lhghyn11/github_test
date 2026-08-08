class Student():

    school = "Python学院"

    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("培瑞",20)
s2 = Student("张三",18)

print(s1.name)
print(s1.school)

print(s2.name)
print(s2.school)