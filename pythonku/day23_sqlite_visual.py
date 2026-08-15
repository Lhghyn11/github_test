import sqlite3
import pandas as pd#Pandas读取
import matplotlib.pyplot as plt#Matplotlib画图


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False#解决中文乱码


#连接数据库
conn = sqlite3.connect(
    "projects/student_oop/students.db"
)


#读取数据
df = pd.read_sql(
    "SELECT name,score FROM students",
    conn
)


print(df)


#画图
plt.bar(
    df["name"],#获取名字这一列
    df["score"]
)


plt.title("学生成绩统计")

plt.xlabel("姓名")

plt.ylabel("成绩")


plt.show()