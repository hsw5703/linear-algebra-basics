import numpy as np

m1 = np.array([[10, 20, 30], [40, 50, 60]])

m2 = m1 + 10 # 스칼라는 2차원 배열로 브로드캐스트된 후 요소별 사칙연산한다.
m3 = m1 - 10
m4 = m1 * 10
m5 = m1 / 10

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)

