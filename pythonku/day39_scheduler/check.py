import torch


checkpoint = torch.load(
    "checkpoint.pth"
)


print(checkpoint.keys())