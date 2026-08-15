import numpy as np
#print(np.__version__)测试安装numpy版本

#一维矩阵
import numpy as np
a = np.array([1,2,3,4])
print(a)
print(type(a))#类型numpy.ndarray

print("数组:",a)
print("维度:",a.ndim)
print("形状:",a.shape)
print("元素数量:",a.size)
print("数据类型:",a.dtype)


#二维数组
import numpy as np
matrix = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(matrix)
print("维度:", matrix.ndim)
print("形状:", matrix.shape)

#运算
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)#数组加法
print(a - b)#数组减法
print(a * b)#不是矩阵乘法，是对应位置相乘1*4 2*5 3*6
print(a / b)#数组除法1/4 2/5 3/6
print(a + 10)#数组和数字运算 numpy自动1+10 2+10 3+10
print(a * 2)#1*2 2*2 3*2

#二维数组运算
import numpy as np
matrix = np.array(
    [
        [1,2],
        [3,4]
    ]
)
print(matrix + 10)

#常用统计函数
import numpy as np
scores = np.array(
    [80,90,70,100]
)
print(scores.mean())#平均
print(scores.max())#最大
print(scores.min())#最小
print(scores.sum())#求和

#一维数组索引
import numpy as np
a = np.array([10,20,30,40,50])
print(a[0])
print(a[2])
#修改元素
a[1] = 99
print(a)
#切片
print(a[1:4])

#二维数组（矩阵）索引
import numpy as np
matrix = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
print(matrix)
print(matrix[0,0])#取某个元素（这里是第0行第0列
print(matrix[1,2])
print(matrix[1])#取整行
print(matrix[:,0])#取整列 ：表示所有行

#改变数组形状
import numpy as np
a = np.array(
    [1,2,3,4,5,6]
)
print(a.shape)#查看形状:一维，6个元素（6，）
b = a.reshape(2,3)#改变形状，变成2行3列
print(b)
print(b.shape)#查看二维数组的形状（2，3）
a.reshape(2,-1)#让numpy自动计算，比如6个数字：2*？，答案是3，所以（2，3）
