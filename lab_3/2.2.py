import numpy as np
import scipy
import matplotlib.pyplot as plt

def custom_cdf(x):
    if (x<=-np.pi/2):
        return 0
    elif(x>-np.pi/2 and x<=np.pi/2):
        return 0.5 * np.sin(x)+ 0.5
    else:
        return 1
class CustomDistClass(scipy.stats.rv_continuous):
    def _cdf(self, x):
        return custom_cdf(x)

dist_class = CustomDistClass()
sample = dist_class.rvs(size = 50)
print(sample)

#plt.hist(sample)

#функція розподілу
def f(x):
    if x >= -np.pi/2 and x <= np.pi/2:
        return 0.5 * np.cos(x)
    else:
        return 0


x = np.linspace(-np.pi / 2, np.pi / 2, 50)
y = [f(i) for i in x]
print(x)
plt.hist(sample, density=True)
plt.plot(x, y, color='r')

plt.show()