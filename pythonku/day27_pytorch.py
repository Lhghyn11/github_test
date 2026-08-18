import torch
#tensor基础操作
x = torch.tensor([1,2,3])#创建tensor
print(x)
print(x + 10)
print(x * 2)#这和numpy：x=np.array([1,2,3])非常像

#tensor的shape
print(x.shape)
print(x.dtype)#和numpy的x.shape/x.dtype非常相似

#二维tensor(创建一个矩阵)
a = torch.tensor([
    [1,2],
    [3,4]
])
print(a)
print(a.shape)

#矩阵乘法
b = torch.tensor([
    [5,6],
    [7,8]
])
print(a @ b)

#自动求导
x = torch.tensor(
    2.0,
    requires_grad=True#请帮我记录x的计算过程，以后我要对它求导。
)
y = x ** 2#y=x的平方:4
print("y=",y)
y.backward()#让·pytorch自动计算：dy/dx=2x，因为x=2，所以结果是4（tensor(4.)
print("x的梯度=",x.grad)

#tensor和GPU实战
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

x = torch.tensor(
    [1,2,3],
    device=device
)

print(x)
print(x.device)
