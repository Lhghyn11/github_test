import torch
from torch.utils.data import Dataset

from torchvision import datasets
from torchvision import transforms


class MNISTDataset(Dataset):

    def __init__(self):

        self.data = datasets.MNIST(
            root="./data",
            train=True,
            download=True,
            transform=transforms.ToTensor()
        )


    def __len__(self):

        return len(self.data)


    def __getitem__(self,index):

        image,label = self.data[index]

        return image,label
