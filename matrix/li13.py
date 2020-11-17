import numpy as np

m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[10, 20, 30], [40, 50, 60]])

# 행렬의 사칙연산은 같은 자리 행렬의 요소끼리의 연산이다.

m3 = m1 + m2
m4 = np.add(m1, m2)
print(m3)  # 덧셈과 np.add는 같다.

m5 = m1 - m2
m6 = np.subtract(m1, m2)
print(m5)  # 뺄셈과 np.subtract는 같다.

m7 = m1 * m2
m8 = np.multiply(m1, m2)
print(m7)  # 곱셈과 np.multiply는 같다.

m9 = m1 / m2
m10 = np.divide(m1, m2)
print(m9)  # 나눗셈과 np.divide는 같다.
