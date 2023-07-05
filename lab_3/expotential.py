import seaborn as sns
import math
import numpy as np
import matplotlib.pyplot as plt
numbers_2 = []
for i in range(50):
    numbers_2.append(round(np.random.uniform(0, 1), 3))
print('y', numbers_2)
m = 0
x_list = []
while m < len(numbers_2):
  x_list.append(round(math.log(1 - numbers_2[m])/(-0.8), 3))
  m += 1
print('x', x_list)
#sns.histplot(x = x_list)
#plt.show()

x = [1 for i in range(20)]
y = [0.52, 0.402, 0.362, 0.861, 0.259, 0.001, 0.646, 0.358, 0.398, 0.75, 0.544, 0.856, 0.955, 0.542, 0.454, 0.481, 0.733, 0.591, 0.019, 0.794]
def get_time(y):
    t = []
    sum = 0
    for el in y:
        t.append(round(sum+el, 3))
        sum += el
    return t
t = get_time(y)
print(t)
fig, ax = plt.subplots()
#plt.axhline(t, color = 'b', linestyle = 'o')
ax.hlines(1, 0, 11,
          color = 'b',
          linewidth = 2)
ax.scatter(t, x, c='r')
ax.scatter(0, 1, c='r')
x_el = [0.917, 0.643, 0.562, 2.467, 0.375, 0.001, 1.298, 0.554, 0.634, 1.733, 0.982, 2.422, 3.876, 0.976, 0.756, 0.82, 1.651, 1.118, 0.024, 1.975]
for i in range(len(x_el)):
    if t[i] == 2.405:
        plt.text(2.405, 0.985, str(x_el[i]), rotation=-45)
    elif t[i] == 9.732:
        plt.text(9.732, 0.985, str(x_el[i]), rotation=-45)
    else: plt.text(round(t[i], 3), 1.01, str(x_el[i]), rotation=45)
plt.text(0, 1.01, str(0), rotation=45)
#plt.xlim([0, 11])
#plt.tight_layout()
plt.show()
