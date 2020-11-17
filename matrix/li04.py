import numpy as np

v = np.arange(1, 11)

print(np.sum(v)) # 1차원 배열이므로 축 지정 유무와 관계없이 결과는 같다.
print(np.sum(v, axis=0))