import numpy as np

v = np.arange(1, 4)  # diag()는 대각행렬의 주 대각선 요소를 벡터로 전달.
m = np.diag(v)  # 주대각의 경우엔 대각선의 위치 번호가 0으로 생략 가능.
print(m) # 대각선 요소를 제외한 나머지를 0으로 채운다.
m = np.diag(v, -1) # 밑으로 한칸 이동
print(m)
n = np.diag(v, 1) # 위로 한칸 이동
print(n)

print(m + n)  # 대각행렬로 이루어진 행렬은 이렇게 표현할 수도 있다.


