import torch
import torch.nn as nn


from torch.utils.data import DataLoader, random_split


from dataset import StudentDataset

from model import StudentModel



# ======================
# 数据
# ======================


dataset = StudentDataset()



train_size = 6

test_size = 2



train_dataset, test_dataset = random_split(
    dataset,
    [
        train_size,
        test_size
    ]
)



train_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=True
)


test_loader = DataLoader(
    test_dataset,
    batch_size=2
)



print(
    "训练集:",
    len(train_dataset)
)


print(
    "测试集:",
    len(test_dataset)
)



# ======================
# 模型
# ======================


model = StudentModel()



# ======================
# loss
# ======================

loss_fn = nn.MSELoss()



# ======================
# optimizer
# ======================

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)



# ======================
# 训练
# ======================

for epoch in range(1000):


    model.train()


    train_loss = 0



    for x,y in train_loader:


        pred = model(x)#进入训练模式


        loss = loss_fn(
            pred,
            y
        )


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()


        train_loss += loss.item()



    if epoch % 100 == 0:

        print(
            epoch,
            "train loss:",
            train_loss
        )



print("训练完成")

#训练结束，保存模型
torch.save(
    model.state_dict(),
    "student_day37.pth"
)

print("模型保存完成")