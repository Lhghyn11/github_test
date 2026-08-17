import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#中文显示
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

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

#生成成绩等级
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

#根据姓名、成绩、年龄判断数据是否重复（数据清洗）
df = df.drop_duplicates(
    subset=["name","age","score"]
)

print("清洗后数据:")
print(df)

#统计分析
#平均分
avg_score = df["score"].mean()
print("平均成绩：",avg_score)#一行输出

#最高分学生
top_student = df.loc[#获取某一行
    df["score"].idxmax()#最大值所在位置
]
print("最高分学生：")
print(top_student)
#print(top_student)

#成绩排名
rank = df.sort_values(
    by = "score",
    ascending=False#从高到低
)
print("成绩排名：")
print(rank[["name","score"]])

#生成报告csv
report = df[
    ["name","score","level"]
]
report.to_csv(
    "student_report.csv",
    index=False,
    encoding="utf-8-sig"
)
#生成成绩图
#plt.bar(
#    df["name"],
#    df["score"]
#)

#生成有序成绩图
#按成绩排名
chart_df = df.sort_values(
    by = "score",
    ascending=False#从高到低
)
plt.bar(
    chart_df["name"],
    chart_df["score"]
)#效果：最高分在左边

plt.title("学生成绩分析")
plt.xlabel("姓名")
plt.ylabel("成绩")
plt.xticks(rotation=45)

#把plt.show()升级成
#plt.savefig(
#    "score_chart.png"#生成真正的分析报告图
#)
#优化
plt.savefig(
    "score_chart.png",
    dpi=300,#图片清晰度，默认dqi=100
    bbox_inches="tight"#避免文字被裁剪
)