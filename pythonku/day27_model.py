#导入神经网络模块
import torch
import torch.nn as nn#torch.nn是pytorch的神经网络库

#创建第一个神经元
model = nn.Linear(
    2,
    1
)
print(model)#输入2个数字经过线性层输出1个数字

#查看模型参数
for name,param in model.named_parameters():
    print(name)
    print(param)

#放入GPU
device = "cuda"
#device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
print(next(model.parameters()).device)
