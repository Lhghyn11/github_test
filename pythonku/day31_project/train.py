import torch
import torch.nn as nn

from dataset import get_dataloader
from model import get_model

from config import EPOCHS, LEARNING_RATE, MODEL_PATH



# 数据

loader = get_dataloader()


# 模型

model = get_model()



# Loss

loss_fn = nn.MSELoss()



# 优化器

optimizer = torch.optim.SGD(
    model.parameters(),
    #lr=0.01
    lr=LEARNING_RATE
)



# 训练

#for epoch in range(100):
for epoch in range(EPOCHS):

    total_loss = 0


    for batch_x, batch_y in loader:


        prediction = model(batch_x)


        loss = loss_fn(
            prediction,
            batch_y
        )


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()


        total_loss += loss.item()



    if epoch % 10 == 0:

        print(
            epoch,
            total_loss
        )



print("训练完成")

print(
    "weight:",
    model.weight
)

print(
    "bias:",
    model.bias
)



# 保存

torch.save(
    model.state_dict(),
    MODEL_PATH
)

print("模型保存完成")