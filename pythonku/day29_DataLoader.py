import torch
import torch.nn as nn
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


# 训练
for epoch in range(100):

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


    if epoch % 10 == 0:
        print(
            "epoch:",
            epoch,
            "loss:",
            loss.item()
        )


print("训练后 weight:", model.weight)
print("训练后 bias:", model.bias)