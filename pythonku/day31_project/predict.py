import torch

from model import get_model#模型模块

from config import MODEL_PATH#模型保存路径


# 创建模型

model = get_model()


# 加载参数

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        weights_only=True
    )
)


# 推理模式

model.eval()


# 新数据

x = torch.tensor([
    [10.0],
    [20.0]
])


# 不计算梯度

with torch.no_grad():

    y = model(x)


print("预测结果:")
print(y)