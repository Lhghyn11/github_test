import torch


from torch.utils.data import Dataset



class StudentDataset(Dataset):

    def __init__(self):

        self.x = torch.tensor(
            [
                [18],
                [19],
                [20],
                [21],
                [22],
                [23],
                [24],
                [25]
            ],
            dtype=torch.float32
        )


        self.y = torch.tensor(
            [
                [60],
                [65],
                [70],
                [75],
                [80],
                [85],
                [90],
                [95]
            ],
            dtype=torch.float32
        )


    #数据集一共有多少条数据。
    def __len__(self):

        return len(self.x)


    #给我第 index 条数据。
    def __getitem__(self,index):

        return self.x[index], self.y[index]