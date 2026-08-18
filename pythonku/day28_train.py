import torch
import torch.nn as nn#torch.nn：就是 PyTorch 的神经网络库。

#输入数据
x = torch.tensor(
    [
        [1.0],
        [2.0],
        [3.0],
        [4.0]
    ]
)

#标签
y = torch.tensor(
    [
        [3.0],
        [5.0],
        [7.0],
        [9.0]
    ]
)

print(x)
print(y)

#创建模型
#import torch.nn as nn
model = nn.Linear(
    1,
    1#一个输入→一个输出
)
print(model)


print("训练前 weight:", model.weight)
print("训练前 bias:", model.bias)


#定义损失函数
loss_fn = nn.MSELoss()#均方误差

#优化器
optimizer = torch.optim.SGD(
    model.parameters(),#返回生成器generator
    lr=0.01
)

#训练循环
for epoch in range(1000):
    #1.前向传播
    prediction = model(x)
    #2.计算Loss
    loss =loss_fn(prediction,y)
    #3.清空旧梯度
    optimizer.zero_grad()
    #4.反向传播
    loss.backward()#负责计算梯度，告诉模型weight应该往哪个方向调整？bias也是如此

    #到底有没有算出梯度/第一次训练时查看梯度
    if epoch == 0:
        print("weight梯度:", model.weight.grad)
        print("bias梯度:", model.bias.grad)

    #5.更新参数
    optimizer.step()

   #每100轮打印一次
    if epoch % 100 == 0:
        print(
            epoch,
            loss.item()
        )

#最后查看模型学到了什么/查看训练结果
print("训练后:weight:",model.weight)
print("训练后:bias:",model.bias)

#让模型真正“预测”
model.eval()
test_x = torch.tensor([
    [5.0],
    [10.0]
])
with torch.no_grad():  
    prediction = model(test_x)
#prediction = model(test_x)这种会出现grad_fn=<AddmmBackward0>这说明 PyTorch （预测阶段通常不需要计算梯度
print("预测结果：")
print(prediction)

