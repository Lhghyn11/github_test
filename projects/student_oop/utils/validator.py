from exceptions.student_error import StudentError

def check_score(score):#负责检查

    if score < 0 or score > 100:

        raise StudentError("成绩范围错误")

    return True



def check_name(name):

    if name.strip() == "":
        raise ValueError("姓名不能为空")

    return True



def check_age(age):

    if age <= 0:
        raise ValueError("年龄必须大于0")

    return True