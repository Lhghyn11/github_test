import torch
import torch.nn as nn
import matplotlib.pyplot as plt#画图
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader


# 数据
x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0],
    [7.0],
    [8.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0],
    [13.0],
    [15.0],
    [17.0]
])


# Dataset(创建 TensorDataset
dataset = TensorDataset(x, y)


# DataLoader(我应该怎么一批一批地把数据拿出来
loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)


# 模型(创建第一个神经元
model = nn.Linear(1, 1)


# Loss(定义损失函数
loss_fn = nn.MSELoss()


# 优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

#添加Loss记录
loss_history = []

# 训练
for epoch in range(100):

    total_loss = 0

    for batch_x, batch_y in loader:

        # 1. 前向传播
        prediction = model(batch_x)

        # 2. 计算Loss
        loss = loss_fn(
            prediction,
            batch_y
        )

        # 3. 清空梯度
        optimizer.zero_grad()

        # 4. 反向传播
        loss.backward()

        # 5. 更新参数
        optimizer.step()


        # 累加loss
        total_loss += loss.item()

    # 平均loss
    avg_loss = total_loss / len(loader)
    loss_history.append(avg_loss)


    if epoch % 10 == 0:
        print(
            "epoch:",
            epoch,
            "loss:",
            #loss.item()
            avg_loss
        )


print("训练后 weight:", model.weight)
print("训练后 bias:", model.bias)

#画训练曲线
plt.plot(loss_history)#折线图
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()

#保存模型
torch.save(
    model.state_dict(),
    "linear_model.pth"#运行后会出现pth文件，里面保存weight和bias
)
print("模型保存完成")

#加载模型
new_model = nn.Linear(1,1)#重新创建模型
#加载
new_model.load_state_dict(
    torch.load("linear_model.pth")
)
#进入预测模式
new_model.eval()

#测试
test_x = torch.tensor([
    [10.0]
])
with torch.no_grad():
    result = new_model(test_x)
print("预测结果：")
print(result)