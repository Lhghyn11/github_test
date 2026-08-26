import torch
import torch.nn as nn


class CNNModel(nn.Module):

    def __init__(self):

        super().__init__()


        self.conv = nn.Sequential(

            # 第一层卷积
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),


            # 池化:大小减半。
            nn.MaxPool2d(
                kernel_size=2
            ),


            # 第二层卷积
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),


            nn.MaxPool2d(
                kernel_size=2
            )
        )


        self.fc = nn.Sequential(

            nn.Linear(
                32 * 7 * 7,
                128
            ),

            nn.ReLU(),


            nn.Linear(
                128,
                10
            )
        )



    def forward(self,x):

        x = self.conv(x)


        # 展平
        x = x.view(
            x.size(0),
            -1
        )


        x = self.fc(x)


        return x

