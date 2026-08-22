import torch
import time


# 创建矩阵
x = torch.randn(
    5000,
    5000
)


y = torch.randn(
    5000,
    5000
)


# CPU计时
start = time.time()


z = x @ y#矩阵乘法


end = time.time()


print(
    "CPU耗时:",
    end-start,
    "秒"
)


# =====================
# GPU
# =====================


device = torch.device("cuda")


x_gpu = x.to(device)

y_gpu = y.to(device)


# GPU同步计时

torch.cuda.synchronize()


start = time.time()


z_gpu = x_gpu @ y_gpu


torch.cuda.synchronize()


end = time.time()


print(
    "GPU耗时:",
    end-start,
    "秒"
)