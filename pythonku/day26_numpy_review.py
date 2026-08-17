#数组运算
import numpy as np
x = np.array([1,2,3,4])
print(x)
print(x+10)
print(x*2)

#矩阵乘法
a = np.array(
    [
        [1,2],
        [3,4]
    ]
)
b = np.array(
    [
        [5,6],
        [7,8]
    ]
)
print(a @ b)

#随机数据
np.random
data = np.random.randn(5,3)
print(data)

#把pandas数据转成numpy
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "age":[20,21,19],
    "score":[90,85,95]
})
print(df)
data = df.to_numpy()
print(data)
print(type(data))
scores = df["score"].to_numpy()

#选择真正用于计算的数据
print(scores)
print(scores.mean())
print(scores.max())
print(scores.min())

#把numpy数据转成pytorch
import torch
tensor = torch.tensor(data)
print(tensor)
print(type(tensor))

#把numpy数据转成tensor
tensor = torch.from_numpy(
    data.copy()
)
print(tensor)
print(type(tensor))

#把rensor数据转成numpy
array = tensor.numpy()
print(array)
print(type(array))

#把数据送进显卡，让GPU计算。
if torch.cuda.is_available():
    tensor = tensor.cuda()
print(tensor.device)
