import pandas as pd
import torch

from torch.utils.data import Dataset#导入数据


class StudentDataset(Dataset):

    def __init__(self):

        #读取csv文件
        df = pd.read_csv(
            "students.csv"
        )


        #输入数据
        self.x = torch.tensor(
            df[["age"]].values,
            dtype=torch.float32
        )


        #标签
        self.y = torch.tensor(
            df[["score"]].values,
            dtype=torch.float32
        )

    #数据集一共有多少条数据。
    def __len__(self):

        return len(self.x)


    #给我第 index 条数据。
    def __getitem__(self,index):

        return (
            self.x[index],
            self.y[index]
        )
