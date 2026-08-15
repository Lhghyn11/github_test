import pandas as pd
data = {
    "name":["张三","李四","王五"],
    "age":[20,21,19],
    "score":[90,85,95]
}
df = pd.DataFrame(data)
print(df)#DataFrame
print(type(df))#类型
print(df.columns)#列名
print(df.shape)#shape

print(df["score"])#获取一列
print(df[["name","score"]])#获取多列
print(df.loc[0])#获取第一行

#条件筛查
print(df[df["score"] > 90])
print(df[df["age"] > 19])
print(df[df["score"] == 85])

print(df["score"].mean())#平均成绩
print(df["score"].max())#最大成绩
print(df["score"].min())#最小成绩
print(df.describe())#统计全部数据，自动计算数量、平均、标准差、最小、最大
