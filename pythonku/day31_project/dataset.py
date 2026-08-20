import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

from config import BATCH_SIZE


def get_dataloader():

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

#创建 TensorDataset,现在：dataset就是一个数据集。
    dataset = TensorDataset(
        x,
        y
    )


# DataLoader(我应该怎么一批一批地把数据拿出来
    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True
    )


    return loader