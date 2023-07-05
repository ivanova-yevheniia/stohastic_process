import random
import numpy as np
import matplotlib.pyplot as plt
#y = [round(random.random(), 2) for i in range(50)]
#print(y)


def get_x(y):
    x = []
    for element in y:
        if element>0 and element<=0.15:
            x.append(-4)
        elif element>0.15 and element<=0.2:
            x.append(-3)
        elif element>0.15 and element<=0.4:
            x.append(-2)
        elif element>0.4 and element<=0.55:
            x.append(-1)
        elif element>0.55 and element<=0.65:
            x.append(0)
        elif element>0.65 and element<=0.95:
            x.append(1)
        elif element>0.95 and element<=1:
            x.append(2)
        else: x.append('inf')
    return x

#print(get_x(y))
fig, ax = plt.subplots()
x = [1, 0, -4, -2, 1, -4, 1, 0, -4, 1, -4, 0, -2, -2, 0, 0, -4, 0, -3, 1, 0, 0, 1, 0, -2, 1, 0, 1, -2, -4, -2, 1, -4, 0,\
    -4, -1, 1, -2, -1, 0, -4, 1, -1, -1, 1, -4, -1, 1, -2, -2]
labels, counts = np.unique(x, return_counts=True)
plt.bar(labels, counts, align='center')
plt.show()
