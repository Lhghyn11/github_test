import torch
import torch.nn as nn

from dataset import StudentDataset
from model import StudentModel

from torch.utils.data import DataLoader, random_split

#dataset = StudentDataset()

#loader = torch.utils.data.DataLoader(
#    dataset,
#    batch_size=8,
#    shuffle=True
#)

# ===================
# 数据
# ===================
dataset = StudentDataset()


# 划分训练集和验证集
train_size = int(len(dataset) * 0.75)
val_size = len(dataset) - train_size


train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size]
)


train_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=True
)


val_loader = DataLoader(
    val_dataset,
    batch_size=2,
    shuffle=False
)


print("训练集:", len(train_dataset))
print("验证集:", len(val_dataset))

# ===================
# 模型
# ===================


model = StudentModel()

# ===================
# loss
# ===================

loss_fn = nn.MSELoss()


# ===================
# optimizer
# ===================

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

#SGD版本
#optimizer = torch.optim.SGD(
#Adam版本：更智能
#optimizer = torch.optim.Adam(
#   model.parameters(),
#    lr=0.01
#)

#for epoch in range(1000):
#    total_loss = 0
#    for x,y in loader:
#        pred = model(x)
#        loss = loss_fn(
#            pred,
#            y
#        )
#        optimizer.zero_grad()
#        loss.backward()
#        optimizer.step()
#        total_loss+=loss.item()

#    if epoch % 100 == 0:
#        print(
#            epoch,
#            total_loss
#        )


    # =================
    # train
    # =================

for epoch in range(5000):

    # -------- train --------

    model.train()

    train_loss = 0


    for x,y in train_loader:


        pred = model(x)


        loss = loss_fn(
            pred,
            y
        )


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()


        train_loss += loss.item()



    # =================
    # validation
    # =================

    model.eval()


    val_loss = 0


    with torch.no_grad():


        for x,y in val_loader:


            pred = model(x)


            loss = loss_fn(
                pred,
                y
            )


            val_loss += loss.item()



    if epoch % 100 == 0:

        print(
            epoch,
            "train loss:",
            train_loss,
            "val loss:",
            val_loss
        )

print("训练完成")

print(
    "weight:",
    model.linear.weight
)

print(
    "bias:",
    model.linear.bias
)