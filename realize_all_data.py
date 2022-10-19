import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

data = {3:  [0.834,	0.000,	-0.603,	-0.021,	0.526,	1.160,	1.370,	0.599,	0.904,	 0.712],
        7: [-0.609,	-0.297,	-0.565,	-0.403,	0.208,	0.972,	0.777,	0.476,	0.465,	-0.361],
        12:	[0.081,	-0.178,	-0.788,	-0.477,	0.471,	-0.354,	1.410,	0.006,	0.315,	 0.658],
        27: [0.330,	-0.289,	-0.519,	-0.274,	-0.258,	1.010,	0.534,	0.569,	0.468,	 0.626],
        34:	[-0.554,-1.390,	-0.577,	 0.454,	0.129,	0.853,	0.378,	0.245,	-0.289,	-0.297],
        37:	[0.670,	-0.755,	-0.819,	-0.040,	0.688,	0.439,	0.768,	0.385,	-0.071,	 0.559],
        48:	[0.093,	0.569,	-0.592,	 0.235,	0.506,	-0.170,	0.369,	0.309,	-0.035,	-0.427],
        54:	[-0.746,-0.582,	 0.009,	-0.203,	0.874,	0.826,	0.994,	1.000,	-0.045,	-0.459],
        67:	[0.232,	-0.364,	-0.641,	-0.315,	-0.341,	0.277,	0.317,	1.240,	0.296,	0.317],
        71:	[0.274,	1.190,	-0.841,	0.416,	0.482,	-0.092,	1.480,	-0.013,	-0.061,	-0.290],
        85:	[-0.505,-0.520,	-0.620,	0.043,	0.561,	1.220,	0.700,	1.020,	0.201,	-0.136],
        93: [-0.992,-1.150,	-0.326,	-0.008,	0.248,	0.221,	0.708,	0.675,	-0.112,	0.927]
}
t = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10']

#Mx - find expexted value
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
print(ex_val)
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


def standard_deviation(dispr):
        return np.sqrt(dispr)

std_dev = standard_deviation(dispersion())
#print(std_dev)

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

plt.plot(t, data[3], label=r'$x3(t)$')
plt.plot(t, data[7], label=r'$x7(t)$')
plt.plot(t, data[12], label=r'$x12(t)$')
plt.plot(t, data[27], label=r'$x27(t)$')
plt.plot(t, data[34], label=r'$x34(t)$')
plt.plot(t, data[37], label=r'$x37(t)$')
plt.plot(t, data[48], label=r'$x48(t)$')
plt.plot(t, data[54], label=r'$x54(t)$')
plt.plot(t, data[67], label=r'$x67(t)$')
plt.plot(t, data[71], label=r'$x71(t)$')
plt.plot(t, data[85], label=r'$x85(t)$')
plt.plot(t, data[93], label=r'$x93(t)$')
#plt.plot(t, ex_val, color = 'red', label=r'$m_x$')
#plt.plot(t, std_dev, color = 'blue', label=r'$sigma$')
plt.legend(loc='center left', bbox_to_anchor= (1, 0.5), fancybox=True, shadow=True)
plt.show()