import sqlite3
import pandas as pd


conn = sqlite3.connect(
    "projects/student_oop/students.db"
)


df = pd.read_sql(
    "SELECT * FROM students",
    conn
)


print(df)


print("平均成绩:", df["score"].mean())


print("最高分学生:")
print(
    df.loc[df["score"].idxmax()]
)


print("最低分学生:")
print(
    df.loc[df["score"].idxmin()]
)

#根据姓名去重
df = df.drop_duplicates(
    subset=["name"]
)

print("成绩排名:")
rank_df = df.sort_values(
    by="score",
    ascending=False#从高到低
)

print(
    rank_df[["name","score"]]
)

print("按成绩统计人数")
print(
    df.groupby("score").size()
)


def get_level(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


df["level"] = df["score"].apply(get_level)

print(df[["name","score","level"]])#只显示这三列

#保存分析报告
df.to_csv(
    "student_test.csv",#生成文件名
    index=False,#去掉索引那一列
    encoding="utf-8-sig"#保证excel打开中文不会乱码
)