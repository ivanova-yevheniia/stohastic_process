import numpy as np
import matplotlib.pyplot as plt
numbers = []
for i in range(1000):
    numbers.append(round(np.random.uniform(0, 1), 3))
print(numbers)

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


x_list = get_x(numbers)
labels, counts = np.unique(x_list, return_counts=True)
plt.bar(labels, counts, align='center')
plt.show()
