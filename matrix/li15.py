import numpy as np

m1 = np.array([[1, 2], [3, 4], [5, 6]])  # 3*2 행렬
m2 = np.array([[10, 10], [20, 20]])  # 2*2 행렬

m3 = m1 @ m2  # @는 np.dot()과 동일하다.
m4 = np.dot(m1, m2)
# m5 = np.dot(m2, m1) # 앞뒤 순서 중요. 2*2 * 3*2는 Error

print(f'{m3} \n {m4}')
print(np.dot(m2, 10))  # 스칼라는 대각행렬로 변환되어 곱해진다.

m1 = np.array([[1, 2], [3, 4], [5, 6]])  # 3*2 행렬
m2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2*3 행렬
v = np.array([10, 100])  # 벡터값과 dot연산

m3 = np.dot(v, m2)  # 벡터가 앞에 있을 경우 행렬의 행과 벡터 크기가 일치해야 한다
# m4 = np.dot(m2, v) 벡터가 뒤에 있을 경우 행렬의 열과 벡터 크기가 일치해야 한다.

print(m3)

