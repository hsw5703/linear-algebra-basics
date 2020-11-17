import numpy as np

arr1 = np.arange(0, 10)
print(f'{arr1}\n{arr1.shape}\n{arr1.ndim}')

arr2 = arr1[:, np.newaxis] # 기존 arr1의 데이터를 행방향으로 배열하고 1축 벡터를 2축 배열로 바꾼다.
print(f'{arr2}\n{arr2.shape}\n{arr2.ndim}')

arr3 = arr1[np.newaxis, :] # 기존 arr1의 데이터를 열방향으로 배열하고 1축 벡터를 2축 배열로 바꾼다.
print(f'{arr3}\n{arr3.shape}\n{arr3.ndim}')

print('----------------------------------------')

arr1 = np.zeros(5) # 모든 데이터가 0인 크기 5의 벡터
print(f'{arr1}\n{arr1.shape}\n{arr1.dtype}')

arr2 = np.ones((3, 4)) # 모든 데이터가 1인 3*4 배열
print(f'{arr2}\n{arr2.shape}\n{arr2.dtype}')

arr3 = np.full(2, 5) # 모든 데이터가 5인 크기 2의 벡터
print(f'{arr3}\n{arr3.shape}\n{arr3.dtype}')

arr4 = np.full((4, 3), 2) # 모든 데이터가 2인 4*3 배열
print(f'{arr4}\n{arr4.shape}\n{arr4.dtype}')

arr1 = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
row, col = arr1.shape
print(row, col) # 배열의 행과 열을 출력한다. 배열의 값들을 출력할 때 사용할 수 있다.

