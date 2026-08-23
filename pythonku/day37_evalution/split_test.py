from dataset import StudentDataset


from torch.utils.data import random_split



dataset = StudentDataset()



train_size = 6

test_size = 2



train_dataset, test_dataset = random_split(
    dataset,
    [
        train_size,
        test_size
    ]
)



print(
    "全部数据:",
    len(dataset)
)


print(
    "训练集:",
    len(train_dataset)
)


print(
    "测试集:",
    len(test_dataset)
)