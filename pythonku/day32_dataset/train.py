import torch
import torch.nn as nn

from dataset import StudentDataset
from torch.utils.data import DataLoader


# 数据
dataset = StudentDataset()

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)


# 模型

model = nn.Linear(
    1,
    1
)


# 损失
loss_fn = nn.MSELoss()


# 优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)


# 训练
for epoch in range(500):

    total_loss = 0

    for batch_x, batch_y in loader:

        # 前向
        prediction = model(batch_x)


        # loss
        loss = loss_fn(
            prediction,
            batch_y
        )


        # 梯度清零
        optimizer.zero_grad()


        # 反向
        loss.backward()


        # 更新
        optimizer.step()


        total_loss += loss.item()


    if epoch % 50 == 0:
        print(
            epoch,
            total_loss
        )

# 注意：这一行必须完全退出 for epoch 循环
print("最终 loss:", total_loss)

print("训练完成")

print("weight:", model.weight)

print("bias:", model.bias)