import matplotlib.pyplot as plt
import numpy as np

def f(x) :
    return -np.log(x)

data_x = np.arange(0.01, 2, 0.01)
data_y = f(data_x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='r') # y축선
plt.axhline(y=0, color='r') # x축선
ax.plot(data_x, data_y)
ax.set_xticks([]) # x축 틱을 없앤다.
ax.set_yticks([]) # y축 틱을 없앤다.
plt.show()