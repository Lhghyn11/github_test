import torch

from model import StudentModel

#创建模型结构
model = StudentModel()

#加载参数
model.load_state_dict(
    torch.load(
        "student_model.pth"
    )
)

#推理模式
model.eval()

#新学生年龄
age = torch.tensor(
    [
        [26.0]
    ]
)

#不计算梯度
with torch.no_grad():
    score = model(age)

print("预测成绩")
print(score)