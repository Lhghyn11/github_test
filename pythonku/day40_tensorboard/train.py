import torch
import torch.nn as nn

from torch.utils.tensorboard import SummaryWriter

from torch.utils.data import DataLoader
from dataset import StudentDataset
from model import StudentModel

# 数据

dataset = StudentDataset()


train_loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)


# 模型

model = StudentModel()


# 损失

loss_fn = nn.MSELoss()


# 优化器

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)


#日志保存位置
writer = SummaryWriter(
    "runs/student"
)

sample_x = torch.tensor(
    [[20.]],
    dtype=torch.float32
)

writer.add_graph(
    model,
    sample_x
)

for epoch in range(5000):


    # train

    #train_loss = ...
    train_loss = 0   # 每轮开始清零


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

    # TensorBoard记录
    writer.add_scalar(
        "train loss",
        train_loss,
        epoch
    )

    for name,param in model.named_parameters():

        writer.add_histogram(
            name,
            param,
            epoch
        )

    if epoch % 100 == 0:

        print(
            epoch,
            "train loss:",
            train_loss
        )


    # validation

    #val_loss = ...


    #writer.add_scalar(
        #"val loss",
        #val_loss,
        #epoch)



writer.close()