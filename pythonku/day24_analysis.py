import sqlite3
import pandas as pd
#连接数据库
conn = sqlite3.connect(
    "projects/student_oop/students.db"
)

#读取学生数据
df = pd.read_sql(
    "SELECT * FROM students",
    conn
)
print(df)


#计算平均成绩
avg_score = df["score"].mean()
print("平均成绩：",avg_score)


#最高分
max_score = df["score"].max()
print("最高成绩：",max_score)


#谁最高？
top_student = df.loc[
    df["score"].idxmax()
]
print(top_student)


#谁最低
low_student = df.loc[
    df["score"].idxmin()
]
print(low_student)


#根据姓名去重
df = df.drop_duplicates(
    subset=["name"]
)
#按成绩从高到低排序
rank_df = df.sort_values(
    by="score",
    ascending=False
    #ascending=True从低到高
)
print(rank_df)

#只显示姓名和成绩排名
print(rank_df[["name","score"]])


#按成绩统计人数
print(
    df.groupby("score").size()#多少人拿多少分
)
#按照年龄统计平均成绩：
print(
    df.groupby("age")["score"].mean()
)


#成绩等级分类
def get_level(score):
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    else:
        return "D"
df["level"] = df["score"].apply(get_level)#创建新列，把函数应用到每一行数据
print(df)


#保存分析报告
df.to_csv(
    "student_report.csv",#生成文件名
    index=False,#去掉索引那一列
    encoding="utf-8-sig"#保证excel打开中文不会乱码
)