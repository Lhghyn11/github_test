import torch


from model import StudentModel



# =================
# 创建模型
# =================

model = StudentModel()



# =================
# 加载最佳模型
# =================

model.load_state_dict(
    torch.load(
        "best_model.pth"
    )
)



model.eval()



# =================
# 输入年龄
# =================

x = torch.tensor(
    [
        [24.]
    ]
)



# =================
# 预测
# =================

with torch.no_grad():


    y = model(x)



print(
    "预测成绩:"
)

print(y)

print("weight:")
print(model.linear.weight)

print("bias:")
print(model.linear.bias)