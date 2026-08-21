import torch
import torch.nn as nn

from dataset import StudentDataset

from torch.utils.data import DataLoader, random_split


# =====================
# 数据
# =====================

dataset = StudentDataset()


train_size = int(len(dataset)*0.75)

test_size = len(dataset)-train_size


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


# =====================
# 模型
# =====================

model = nn.Linear(
    1,
    1
)


loss_fn = nn.MSELoss()


optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)


# =====================
# 训练
# =====================

for epoch in range(1000):

    model.train()

    train_loss = 0


    for x,y in train_loader:


        prediction = model(x)


        loss = loss_fn(
            prediction,
            y
        )


        optimizer.zero_grad()

        loss.backward()

        optimizer.step()


        train_loss += loss.item()



    if epoch % 100 == 0:

        print(
            "epoch:",
            epoch,
            "train loss:",
            train_loss
        )



# =====================
# 测试
# =====================

model.eval()


test_loss = 0


with torch.no_grad():

    for x,y in test_loader:


        prediction = model(x)


        loss = loss_fn(
            prediction,
            y
        )


        test_loss += loss.item()



print("================")

print(
    "test loss:",
    test_loss
)


print("weight:")
print(model.weight)


print("bias:")
print(model.bias)