import torch

from model import StudentModel


model = StudentModel()


# 加载训练参数
model.load_state_dict(
    torch.load(
        "student_mlp.pth"
    )
)


model.eval()


age = torch.tensor(
    [
        [26.0]
    ]
)


with torch.no_grad():

    score = model(age)


print(score)