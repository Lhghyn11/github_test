class Student:

    def __init__(self, name, age, score):

        self.name = name
        self.age = age
        self.__score = score


    def show_info(self):
        #print(f"姓名：{self.name} 年龄：{self.age} 成绩：{self.__score}")
        return f"姓名：{self.name} 年龄：{self.age} 成绩：{self.__score}"#返回字符串
    
    def update_score(self,score):

        if score < 0 or score > 100:
            print("成绩范围错误")
            return False
        
        self.__score = score#私有属性

        print("成绩修改完成")
        return True


    def get_score(self):
        return self.__score#用于读取成绩

s1 = Student("培瑞",20,100)

s1.show_info()

s1.update_score(95)

s1.show_info()

s1.update_score(120)#测试成绩范围

s1.show_info()

print(s1.show_info())
    


