import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

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

def expected_value():
        sum = 0
        ex_val = []
        for i in range(len(t)):
            for key in data.keys(): sum += data[key][i]
            val = sum/12
            sum = 0
            ex_val.append(val)
        return ex_val

ex_val = expected_value()

def dispersion():
        sum = 0
        dis = []
        for i in range(len(t)):
            for key in data.keys():
                    sum += np.square(data[key][i]) - np.square(ex_val[i])
            val = sum/11
            sum = 0
            dis.append(val)
        return dis

dispr = dispersion()

def standard_deviation():
        return np.sqrt(dispr)

std_dev = standard_deviation()
print(std_dev)

plt.title("Realization")
plt.xlabel(r'$t$')
plt.ylabel(r'$X(t)$')

ax.minorticks_on()

ax.grid(which='major',
        color = 'k',
        linewidth = 0.5)

ax.grid(which='minor',
        color = 'k',
        linewidth = 0.2)

plt.plot(t, data[1], color = '0', label=r'$x1(t)$')
plt.plot(t, data[10], color = '0.1', label=r'$x10(t)$')
plt.plot(t, data[17], color = '0.15', label=r'$x17(t)$')
plt.plot(t, data[30], color = '0.2', label=r'$x30(t)$')
plt.plot(t, data[38], color = '0.25', label=r'$x38(t)$')
plt.plot(t, data[44], color = '0.3', label=r'$x44(t)$')
plt.plot(t, data[57], color = '0.35', label=r'$x57(t)$')
plt.plot(t, data[69], color = '0.4', label=r'$x69(t)$')
plt.plot(t, data[74], color = '0.45', label=r'$x74(t)$')
plt.plot(t, data[83], color = '0.5', label=r'$x83(t)$')
plt.plot(t, data[92], color = '0.55', label=r'$x92(t)$')
plt.plot(t, data[100], color = '0.6', label=r'$x100(t)$')
plt.plot(t, ex_val, color = 'red', label=r'$m_x$')
plt.plot(t, std_dev, color = 'blue', label=r'$sigma$')
plt.legend(loc='center left', bbox_to_anchor= (1, 0.5), fancybox=True, shadow=True)
plt.show()