#创建Dataset
import torch
from torch.utils.data import TensorDataset

from torch.utils.data import DataLoader#DataLoader

#准备昨天的数据
x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0],
    [7.0],
    [8.0]
])
y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0],
    [13.0],
    [15.0],
    [17.0]
])

#创建TensorDataset
dataset = TensorDataset(x,y)#dataset是一个数据集
print(dataset)
print("数据集大小：",len(dataset))

#取出一条数据
print("第0条数据:",dataset[0])
#再试
print("第3条数据:",dataset[3])

#DataLoader
loader = DataLoader(
    dataset,
    batch_size = 2,#每次拿两条数据
    shuffle=True#每次训练之前随机打乱数据
)

#查看Batch
for batch_x,batch_y in loader:#8个数据 batch=2 所以每轮应该有4个batch
    print("batch_x:")
    print(batch_x)#输出两行
    print("batch_y:")
    print(batch_y)


