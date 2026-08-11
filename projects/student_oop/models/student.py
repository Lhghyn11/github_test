class Student:

    def __init__(self, name, age, score):

        self.name = name
        self.age = age

        if score < 0 or score > 100:
            raise ValueError("成绩范围错误")

        self.__score = score

    @property
    def score(self):

        return self.__score


    def show_info(self):
        #print(f"姓名：{self.name} 年龄：{self.age} 成绩：{self.__score}")
        return f"姓名：{self.name} 年龄：{self.age} 成绩：{self.__score}"#返回字符串
    
    def update_score(self,score):

        if score < 0 or score > 100:
            #print("成绩范围错误")
            raise ValueError("成绩范围错误")
            #return False
        
        self.__score = score#私有属性

        print("成绩修改完成")#现在是错误然后raise valueerror然后交给调用者处理
        #return True以前是报错然后print然后return false


    def get_score(self):
        return self.__score#用于读取成绩

#s1 = Student("培瑞",20,100)
#s1.show_info()
#s1.update_score(95)成绩修改完成
#s1.show_info()
#s1.update_score(120)#测试成绩范围   成绩范围错误
#s1.show_info()
#print(s1.show_info())姓名：培瑞 年龄：20 成绩：95
if __name__ == "__main__":#加主程序保护，判断：当前文件是不是被直接运行

    s1 = Student("培瑞",20,100)

    s1.show_info()

    s1.update_score(95)

    print(s1.show_info())
    


