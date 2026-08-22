import torch
import torch.nn as nn


# =====================
# device
# =====================
#判断GPU是否可用
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


print("当前设备:", device)



# =====================
# 创建模型
# =====================

model = nn.Linear(
    1,
    1
)


# 放GPU
model.to(device)#参数位置


print(
    "模型设备:",
    next(model.parameters()).device
)



# =====================
# 保存
# =====================

torch.save(
    model.state_dict(),
    "gpu_linear.pth"
)


print("模型保存完成")