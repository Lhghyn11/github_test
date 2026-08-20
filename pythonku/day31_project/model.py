import torch.nn as nn#创建一个神经元


def get_model():

    model = nn.Linear(
        1,
        1
    )

    return model