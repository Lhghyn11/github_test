#运算
import numpy as np
a = np.array([10,20,30])
b = np.array([1,2,3])
print(a + b)
print(a - b)
print(a * b)


#常用统计函数
import numpy as np
scores = np.array(
    [80,90,75,95,100]
)
print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.sum())

#广播
import numpy as np
a = np.array([1,2,3])
print(a+100)
print(a*10)

#一维数组切片
import numpy as np
a = np.array([10,20,30,40,50])
print(a[0])
print(a[3])
print(a[1:4])
a[2] = 100
print(a)

#二维数组（矩阵）索引
import numpy as np
matrix = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
print(matrix[0,2])
print(matrix[2,1])
print(matrix[1])
print(matrix[:,0])

#查看形状
import numpy as np
a = np.array(
    [1,2,3,4,5,6]
)
print(a.shape)
b = a.reshape(2,3)
print(b)
print(b.shape)
c=a.reshape(3,2)
print(c)