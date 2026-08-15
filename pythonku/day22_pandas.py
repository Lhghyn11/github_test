import pandas as pd
#print(pd.__version__)测试安装numpy版本,有两个pandas，

#创建第一个DataFrame
import pandas as pd
data = {
    "姓名":["小明","小红","小刚"],
    "年龄":[18,19,20],
    "成绩":[88,92,85]
}
df = pd.DataFrame(data)
print(df)
print(type(df))#查看数据类型
print(df.columns)#查看列名
print(df.shape)#查看数据规模（形状
print(df.head())#默认显示前5行，不会全部打印数据

print(df["成绩"])#获取一列
print(df[["姓名","成绩"]])#获取多列
print(df.loc[0])#获取第一行

#读取csv文件
import pandas as pd
df = pd.read_csv("pythonku/students.csv")
print(df)