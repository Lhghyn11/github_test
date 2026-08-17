import torch
import pandas as pd

df = pd.DataFrame({
    "age":[20,21,19],
    "score":[90,85,95]
})
print(df)
data = df.to_numpy()#把pandas数据转成numpy


tensor = torch.tensor(data)#把numpy数据转成pytorch

print(tensor)
print(type(tensor))

print(tensor.shape)#torch.Size([3, 2])三行两列

if torch.cuda.is_available():
    tensor = tensor.cuda()
    print(tensor.device)#cuda:0成功进入RTX3050 GPU