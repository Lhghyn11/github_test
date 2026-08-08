class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"你好，我是{self.name}")

    def show_age(self):
        print(f"我的年龄是{self.age}")

s1 = Student("培瑞",20)

s1.say_hello()

s1.show_age()