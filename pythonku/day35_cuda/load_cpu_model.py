import torch
import torch.nn as nn



# 创建模型
model = nn.Linear(
    1,
    1
)



# 加载参数
state_dict = torch.load(
    "gpu_linear.pth",
    map_location="cpu"
)


model.load_state_dict(
    state_dict
)



print(
    "模型设备:",
    next(model.parameters()).device
)