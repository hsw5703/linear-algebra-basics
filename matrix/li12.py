import numpy as np

# 전치행렬을 행과 열을 바꾸는 행렬이다.

a = np.arange(15).reshape(3, 5)
print(a)

a1 = a.T
print(a1)

a2 = np.transpose(a)
print(a2)

a3 = np.swapaxes(a, 0, 1) # a의 0과 1축을 바꾼다.
print(a3)
