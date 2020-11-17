import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return 2 ** x


def f2(x):
    return np.log2(x)  # 밑이 2인 log함수


data_x1 = np.arange(-2, 5, 0.1)
data_y1 = f1(data_x1)
data_y2 = f2(data_y1)

fig, ax = plt.subplots(3, 1)
ax[0].axvline(x=0, color='r')  # y축선
ax[0].axhline(y=0, color='r')  # x축선
ax[0].plot(data_x1, data_y1)
ax[0].set_xticks([])  # x축 틱을 없앤다.
ax[0].set_yticks([])  # y축 틱을 없앤다.

ax[1].axvline(x=0, color='r')  # y축선
ax[1].axhline(y=0, color='r')  # x축선
ax[1].plot(data_y1, data_y2)
ax[1].set_xticks([])  # x축 틱을 없앤다.
ax[1].set_yticks([])  # y축 틱을 없앤다.

ax[2].axvline(x=0, color='k')  # y축선
ax[2].axhline(y=0, color='k')  # x축선
ax[2].plot(data_x1, data_y1)
ax[2].set_xticks([])  # x축 틱을 없앤다.
ax[2].set_yticks([])  # y축 틱을 없앤다.

ax[2].axvline(x=0, color='k')  # y축선
ax[2].axhline(y=0, color='k')  # x축선
ax[2].plot(data_y1, data_y2)
ax[2].set_xticks([])  # x축 틱을 없앤다.
ax[2].set_yticks([])  # y축 틱을 없앤다.

plt.show()
