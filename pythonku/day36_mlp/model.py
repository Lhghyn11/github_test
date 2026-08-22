import torch.nn as nn

#你的模型是 PyTorch 神经网络。
class StudentModel(nn.Module):

#初始化PyTorch 内部功能。
    def __init__(self):

        super().__init__()

#作用：把多个层连接起来。
        self.net = nn.Sequential(

            # 输入层 → 隐藏层：输入：1个数字，输出：16个特征
            nn.Linear(
                1,
                8
            ),


            # 激活函数
            nn.ReLU(),


            # 隐藏层 → 输出层把：16个隐藏特征转换：1个预测结果
            nn.Linear(
                8,
                1
            )

        )

#决定数据怎么流动。
    def forward(self,x):

        return self.net(x)