import numpy as np

# print(np.__version__)    #1.20.1
# # ------ array() 可將 Python list 或元組 (tuple) 的值建立為 NumPy array。
# #(1) List
# a=np.array([1,2,3,4,5])
# print(a,type(a))
#
# #(2) tuple
# b = np.array((6,7,8))
# print(b,type(b))
#
# #(3) 使用 arange() 與 linspace() 函式產生等差一維陣列
# # numpy.arange([start, ]stop, [step, ]dtype=None)
#
# c = np.arange(10)
# print(c)   #[0 1 2 3 4 5 6 7 8 9]
#
# d = np.arange(2,10,2)
# print(d)
#
# f = np.arange(1.0, 3.0, 0.5, dtype='float64')
# print(f)

# 當在 arange() 使用非整數的間隔值時，有可能會產生不一致的結果,使用 linspace() 函式
# a = np.arange(0.13, 0.16, step=0.01)
# print("沒有包含結束值：", a)  # [0.13 0.14 0.15]
#
# b = np.arange(0.12, 0.16, step=0.01)
# print("包含結束值：", b)   #  [0.12 0.13 0.14 0.15 0.16]

# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# c = np.linspace(2, 10, num=4, endpoint=False)
# print(c,type(c))
#
# d= np.linspace(2.0, 3.0, num=5, retstep=True)   # # 顯示間值值
# print(d,type(d))

# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
#
# print(a.shape)

# b = np.array([[[1, 2, 3], [4, 5, 6],
#               [7, 8, 9], [10, 11, 12]],
#               [[1, 2, 3], [4, 5, 6],
#               [7, 8, 9], [10, 11, 12]]])
#
# print(b,b.shape,b.ndim)

# 維度必須一致
# c= np.zeros((5, 3))
# print(c,c.shape,c.ndim)
#
# d= np.ones([2, 3])
# print(d,d.shape,d.ndim)
#
# e = np.empty((2, 2, 2))
# print(e,e.shape,e.ndim)

from numpy.random import rand




