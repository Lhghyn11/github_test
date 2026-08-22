import torch
import torch.nn as nn

from torch.utils.data import DataLoader

from dataset import StudentDataset
from model import StudentModel



# =====================
# device
# =====================
#判断GPU是否可用
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


print("device:",device)



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


# 模型放GPU
model = model.to(device)#参数位置


print(
    "model device:",
    next(model.parameters()).device
)



loss_fn = nn.MSELoss()


optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)



# =====================
# train
# =====================

for epoch in range(1000):


    total_loss = 0


    for x,y in loader:


        # 数据放GPU

        x = x.to(device)

        y = y.to(device)



        prediction = model(x)


        loss = loss_fn(
            prediction,
            y
        )


        optimizer.zero_grad()


        loss.backward()


        optimizer.step()


        total_loss += loss.item()



    if epoch % 100 == 0:

        print(
            epoch,
            total_loss
        )



print("训练完成")


print(model.linear.weight)

print(model.linear.bias)