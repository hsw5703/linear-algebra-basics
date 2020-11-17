import matplotlib.pyplot as plt
import numpy as np

# 6x+20
def f(x) :
    return 6*x + 20

data_x = np.arange(-10, 10, 0.1)
data_y = f(data_x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='r') # y축선
plt.axhline(y=0, color='r') # x축선
ax.plot(data_x, data_y)
ax.set_xticks([-10, -5, 0, 5, 10]) # x축 틱을 재설정한다.
ax.set_yticks([-100, -50, 0, 50, 100]) # y축 틱을 재설정한다.
plt.show()