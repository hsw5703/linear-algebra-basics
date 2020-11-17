import numpy as np

s = np.array(50)
print('스칼라 : ', s, s.ndim, s.shape)  # 스칼라는 차원이 0이고 형상은 빈 튜플을 반환한다.

v = np.array([50, 10])
print('벡터 : ', v, v.ndim, v.shape)  # 벡터는 차원이 1이고 형상은 1개 요소를 가지는 튜플이다.

m = np.array([[10, 20], [30, 40]])
print('행렬 : \n', m)
print(m.ndim, m.shape)  # 행렬은 차원이 2이고 형상은 2개의 요소를 가지는 튜플이다.

