import numpy as np

m1 = np.zeros((3, 3))
print(m1)  # 3*3의 영행렬을 반환.

m2 = np.zeros_like(np.arange(1, 10).reshape(3, 3))
print(m2)  # 행렬의 shape를 가져와 0으로 채워 반환.