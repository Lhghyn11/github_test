import torch
import torch.nn as nn

from torch.utils.data import DataLoader

from dataset import StudentDataset
from model import StudentModel



# =====================
# 数据
# =====================

dataset = StudentDataset()


loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)



# =====================
# 模型
# =====================

model = StudentModel()


print(model)



# =====================
# 损失函数
# =====================

loss_fn = nn.MSELoss()



# =====================
# 优化器
# =====================

#optimizer = torch.optim.SGD(
#Adam 是现代深度学习常用优化器。
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



# =====================
# 训练
# =====================

for epoch in range(2000):

    total_loss = 0


    for x,y in loader:


        # 1. 前向传播

        prediction = model(x)


        # 2. 计算loss

        loss = loss_fn(
            prediction,
            y
        )


        # 3. 清空梯度

        optimizer.zero_grad()


        # 4. 反向传播

        loss.backward()


        # 5. 更新参数

        optimizer.step()


        total_loss += loss.item()



    if epoch % 100 == 0:

        print(
            epoch,
            total_loss
        )



print("训练完成")

#保存模型
torch.save(
    model.state_dict(),
    "student_mlp.pth"
)
print("模型保存完成")



# 查看参数

for name,param in model.named_parameters():

    print(name)

    print(param)

    print("----------------")