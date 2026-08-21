from dataset import StudentDataset

dataset = StudentDataset()

print("数据集大小：")
print(len(dataset))
print()

print("第0条数据:")
print(dataset[0])
print()

print("第3条数据:")
print(dataset[3])