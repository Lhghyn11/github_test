#连接你的pandas数据
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#现实的数据来自：students.csv或者students.db
df = pd.read_csv("pythonku/students.csv")#读取csv
print(df)

#获取数据
name = df["name"]#获取这一列
score = df["score"]
#画图
plt.bar(name,score)

plt.title("学生成绩")
plt.xlabel("姓名")
plt.ylabel("成绩")
plt.show()

#折线图
import matplotlib.pyplot as plt

epoch = [1,2,3,4,5]
loss = [60,70,75,85,92]

plt.plot(epoch,loss)

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")#准确率

plt.show()
