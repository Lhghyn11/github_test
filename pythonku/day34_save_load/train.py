import torch
import torch.nn as nn


from torch.utils.data import DataLoader

from dataset import StudentDataset

from model import StudentModel



dataset = StudentDataset()


loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)


#模型
model = StudentModel()

#损失
loss_fn = nn.MSELoss()

#优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)



for epoch in range(1000):

    total_loss = 0

    for x,y in loader:

        prediction = model(x)


        loss = loss_fn(
            prediction,
            y
        )

        #梯度清零
        optimizer.zero_grad()
        #反向
        loss.backward()
        #更新
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



# 保存模型参数

torch.save(
    model.state_dict(),
    "student_model.pth"
)


print("模型保存完成")