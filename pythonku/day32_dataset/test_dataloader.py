from dataset import StudentDataset

from torch.utils.data import DataLoader#我应该怎么一批一批地把数据拿出来？

dataset = StudentDataset()

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

for batch_x,batch_y in loader:
    print("batch_x:")
    print(batch_x)
    print("batch_y:")
    print(batch_y)

    print("----------------")


