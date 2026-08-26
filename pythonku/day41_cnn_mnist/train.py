import torch
import torch.nn as nn

from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision.transforms import ToTensor



from model import CNNModel



# =====================
# device
# =====================

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


print("device:",device)



# =====================
# 数据
# =====================


train_data = datasets.MNIST(
    #root="./data",
    root=r"D:\A\github_test\pythonku\day41_cnn_mnist\data",
    train=True,
    download=True,
    transform=ToTensor()
)


test_data = datasets.MNIST(
    #root="./data",
    root=r"D:\A\github_test\pythonku\day41_cnn_mnist\data",
    train=False,
    download=True,
    transform=ToTensor()
)



train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)


test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)



print(
    "训练集:",
    len(train_data)
)


print(
    "测试集:",
    len(test_data)
)



# =====================
# 模型
# =====================


model = CNNModel()

model = model.to(device)



print(model)



# =====================
# loss
# =====================


loss_fn = nn.CrossEntropyLoss()



# =====================
# optimizer
# =====================


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



# =====================
# train
# =====================


epochs = 5



for epoch in range(epochs):


    model.train()


    total_loss = 0


    correct = 0
    total = 0



    for x,y in train_loader:


        # GPU

        x = x.to(device)
        y = y.to(device)



        # forward

        pred = model(x)



        loss = loss_fn(
            pred,
            y
        )


        # backward

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()



        total_loss += loss.item()



        # accuracy

        result = torch.argmax(
            pred,
            dim=1
        )


        correct += (
            result == y
        ).sum().item()


        total += y.size(0)



    acc = correct / total



    print(
        "epoch:",
        epoch,
        "loss:",
        total_loss,
        "acc:",
        acc
    )



# =====================
# save
# =====================


torch.save(
    model.state_dict(),
    "cnn_mnist.pth"
)


print("模型保存完成")