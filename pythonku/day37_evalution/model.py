import torch.nn as nn



class StudentModel(nn.Module):

    def __init__(self):

        super().__init__()


        self.net = nn.Sequential(

            nn.Linear(
                1,
                8
            ),

            nn.ReLU(),

            nn.Linear(
                8,
                1
            )
        )

        #增加
        #nn.Linear(
        #        64,
        #        1
        #    )

        #)


    def forward(self,x):

        return self.net(x)