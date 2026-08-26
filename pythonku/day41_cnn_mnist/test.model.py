import torch

from model import CNNModel



model = CNNModel()



x = torch.randn(
    4,
    1,
    28,
    28
)


y = model(x)



print(y.shape)

#print(model)