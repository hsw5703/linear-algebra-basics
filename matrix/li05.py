import numpy as np

v = np.arange(1, 11)
print(np.sum(v))
print(np.sum(v, axis=0))
print(type(np.sum(v)))
# 1차원 배열(벡터)이므로 축 지정 유무와 관계없이 결과는 같다.

m = np.array([[10, 20], [1, 2]])
print(np.sum(m))
print(np.sum(m, axis=0))
print(np.sum(m, axis=1))
print(type(np.sum(m, axis=1)))
# 행렬의 경우 축이 두 개이기 때문에 지정 유무에 따라 값이 다르다.


