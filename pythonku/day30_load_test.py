import torch 
import torch.nn as nn

#加载模型
model = nn.Linear(1,1)#重新创建模型
#加载
model.load_state_dict(
    torch.load("linear_model.pth")
)
#进入预测模式
model.eval()

#测试
x = torch.tensor([
    [10.0],
    [20.0]
])
with torch.no_grad():
    result = model(x)
print("预测结果：")
print(result)