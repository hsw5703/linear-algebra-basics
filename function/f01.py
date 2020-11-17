import matplotlib.pyplot as plt

data_x = [2, 6]
data_y = [81, 91]

a =  (data_y[1]-data_y[0]) / (data_x[1]-data_x[0])
b = data_y[1]-data_x[1]*a

print(f'직선 y = {a}x+{b}')

# (x, y1)과 직선 사이의 오차를 보고 이를 줄여나가는 것이 목표.

x = [2, 4, 6, 8]
y1 = [81, 93, 91, 97]
y2 = [a*i+b for i in x]

fig, ax = plt.subplots()
plt.scatter(x, y1)
ax.plot(x, y2)
plt.show()