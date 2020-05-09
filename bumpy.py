import numpy as np
//numpy矩阵运算练习

G = np.array([[0, 2, 0.5, 0, 0],
              [0.95, 0, 0, 0, 0],
              [0, 0.9, 0, 0, 0],
              [0, 0, 0.85, 0, 0],
              [0, 0, 0, 0.7, 0]])   #  numpy矩阵表示方法
x = np.array([[1.2, 2, 2.4, 1.8, 0.5]])  # 行向量
x = np.transpose(x)  # matrix transpose 转置成列向量
print(x)

print(G.shape[1] == x.shape[0])  # 判断矩阵是否可以相乘
x = G.dot(x)    # 点乘
print(x)

print(G.shape[1] == x.shape[0])
x = G.dot(x)
print(x)