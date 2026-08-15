import matplotlib
#print(matplotlib.__version__)测试安装matplotlib版本

#创建第一个折线图
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,25]
plt.plot(x,y)#连接这些点（1，10）....(5,25)形成折线

plt.title("My First Chart")#标题
plt.xlabel("Day")#横轴名字
plt.ylabel("Score")#纵轴
plt.show()#展示

#连接你的pandas数据
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

names = ["张三","李四","王五"]
scores = [90,85,95]#数据是手写的

#画图
plt.bar(names,scores)

plt.title("学生成绩")
plt.xlabel("姓名")
plt.ylabel("成绩")
plt.show()

#折线图
import matplotlib.pyplot as plt

epoch = [1,2,3,4,5]
loss = [0.9,0.7,0.5,0.3,0.2]

plt.plot(epoch,loss)

plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")#模型错误程度

plt.show()