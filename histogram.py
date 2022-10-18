import matplotlib.pyplot as plt
import numpy as np

data = {1:  [0.834,-0.609, 0.081, 0.330, -0.554, 0.670, 0.093, -0.746, 0.232, 0.274, -0.505, -0.992],
        2:  [0.000, -0.297, -0.178, -0.289, -1.390, -0.755, 0.569, -0.582,-0.364, 1.190, -0.520, -1.150],
        3:	[-0.603, -0.565, -0.788, -0.519, -0.577,-0.819, -0.592, 0.009,-0.641, -0.841, -0.620, -0.326],
        4:  [-0.021, -0.403, -0.477, -0.274, 0.454, -0.040, 0.235, -0.203,-0.315, 0.416, 0.043, -0.008],
        5:	[0.526,  0.208,   0.471, -0.258, 0.129,  0.688, 0.506,  0.874,-0.341, 0.482, 0.561, 0.248],
        6:	[1.160,  0.972, -0.354,   1.010, 0.853,  0.439, -0.170, 0.826, 0.277,-0.092, 1.220, 0.221],
        7:	[1.370,  0.777,  1.410,   0.534, 0.378,  0.768,  0.369, 0.994, 0.317, 1.480, 0.700, 0.708],
        8:	[0.599,  0.476,  0.006,  0.569,  0.245,  0.385,  0.309, 1.000, 1.240, -0.013, 1.020, 0.675],
        9:	[0.904, 0.465, 0.315, 0.468, -0.289, -0.071, -0.035, -0.045, 0.296, -0.061, 0.201, -0.112],
        10:	[0.712, -0.361,0.658, 0.626, -0.297, 0.559, -0.427, -0.459, 0.317, -0.290, -0.136, 0.927],
}

t = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10']

rez_numb = 1

x_max = max(data[rez_numb])
x_min = min(data[rez_numb])
n = 10

def len_of_interval():
        h = (x_max - x_min)/(np.log10(n)*3.32 + 1)
        return h

h = len_of_interval()

def num_of_interval():
        num = (x_max - x_min)/h
        if num.is_integer():
                return num
        return int(num) + 2

interval_numb = num_of_interval()


def create_bins():
        b = []
        for i in range(interval_numb): b.append(x_min + i*h)
        return b

x = sorted(data[rez_numb])

print(h, interval_numb)
print(x)
b = create_bins()

fig, ax = plt.subplots()
ax.hist(x, bins=b, color = 'skyblue', ec="white")
ax.xaxis.set_major_locator(plt.IndexLocator(base=0.2, offset = 0))
ax.edgecolor = 'r'
plt.grid()
plt.show()