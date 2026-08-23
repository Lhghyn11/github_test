#作用：加载模型，然后测试。
import torch
import torch.nn as nn


from torch.utils.data import DataLoader, random_split


from dataset import StudentDataset

from model import StudentModel



dataset = StudentDataset()



train_dataset, test_dataset = random_split(
    dataset,
    [
        6,
        2
    ]
)



test_loader = DataLoader(
    test_dataset,
    batch_size=2
)



model = StudentModel()



# 加载训练好的模型

model.load_state_dict(
    torch.load(
        "student_day37.pth"
    )
)



# 测试模式
model.eval()



loss_fn = nn.MSELoss()


test_loss = 0


with torch.no_grad():


    for x,y in test_loader:


        pred = model(x)


        loss = loss_fn(
            pred,
            y
        )


        test_loss += loss.item()



print(
    "test loss:",
    test_loss
)