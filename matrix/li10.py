import numpy as np

# 항등행렬은 단위행렬의 다른 이름이다.

m = np.identity(3) # 3*3의 단위행렬(항등행렬)을 생성.
print(m)

s = np.arange(1, 10).reshape(3, 3)
print(s)

print(np.dot(m, s)) # 행렬의 곱

m1 = np.zeros((3, 3))
print(m1)  # 3*3의 영행렬을 반환.

m2 = np.zeros_like(np.arange(1, 10).reshape(3, 3))
print(m2)  # 행렬의 shape를 가져와 0으로 채워 반환.

