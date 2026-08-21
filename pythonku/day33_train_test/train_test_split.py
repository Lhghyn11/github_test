from dataset import StudentDataset

from torch.utils.data import random_split#划分数据


dataset = StudentDataset()


train_size = int(
    len(dataset)*0.75
)


test_size = (
    len(dataset)-train_size
)


train_dataset, test_dataset = random_split(
    dataset,
    [
        train_size,
        test_size
    ]
)


print("全部数据:")
print(len(dataset))


print("训练集:")
print(len(train_dataset))


print("测试集:")
print(len(test_dataset))