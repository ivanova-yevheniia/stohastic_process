import matplotlib.pyplot as plt
import numpy as np

data = {1:  [-0.588, -0.896, -0.867, 0.075,  0.729, 0.494, 0.771, 0.113,  0.231,  0.4],
        10: [0.724,	 -1.17,  -0.775, 0.417, -0.013, 0.223, 0.355, 0.485,  0.526,  0.068],
        17:	[0.128,  -0.386, -1.13, -0.255,  0.679, 0.662, 0.982, 1.14,  -0.239,  0.425],
        30: [0.055,   0.062, -0.312,-0.189,	 0.421,	0.377, 0.411, 0.916,  0.350, -0.559],
        38:	[0.076,   0.189, -0.845,-0.357,	 0.661, 0.672, 0.647, 0.349,  0.846, -0.096],
        44:	[0.24,   -1.48,  -1.01,  0.407,  0.427, 0.679, 1.29, -0.042, -0.112, -0.031],
        57:	[0.611,   0.049, -0.455, 0,      0.107, 0.857, 0.258, 0.487,  0.356,  0.134],
        69:	[0.237,	 -0.411, -0.369, 0.084,	 0.277,	0.982, 0.651, 0.375, -0.083,  0.133],
        74:	[0.172,	  1.44,  -0.608, 0.084,  0.58,  0.205, 0.838, 1.12,	  0.119,  0.287],
        83:	[0.343,	 -0.162, -0.98,	 0.183,	 0.339,	0.234, 1.13,  0.595,  0.169,  0.097],
        92:	[-0.153, -0.798, -0.463,-0.006,	 1.16, -0.244, 0.304, 0.424,  0.249, -0.505],
        100:[-0.204,  0.289, -0.828, 0.39,	 0.12, -1.02,  1.21,  -0.411, 0.171,  0.222]
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
ax.hist(x, bins=b, color = 'skyblue', ec="blue")
ax.xaxis.set_major_locator(plt.IndexLocator(base=0.2, offset = 0))
ax.edgecolor = 'r'
plt.grid()
plt.show()