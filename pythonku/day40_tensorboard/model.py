import torch.nn as nn


class StudentModel(nn.Module):

    def __init__(self):

        super().__init__()


        self.linear = nn.Linear(
            1,
            1
        )


    def forward(self,x):

        return self.linear(x)