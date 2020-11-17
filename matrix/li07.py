import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

v = np.diag(m)  # 2차원 배열의 대각 행렬을 벡터로 반환.
print(v, type(v))

v = np.diag(m, 1)  # 2차원 배열의 대각 행렬 (위치 + 1)을 벡터로 반환.
print(v, type(v))

