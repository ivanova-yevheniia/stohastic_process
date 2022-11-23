import matplotlib.pyplot as plt
import numpy as np
import math

'''create 3d figure'''
fig = plt.figure()
ax = plt.axes(projection ='3d')
plt.title("normalized correlation graph ")
plt.xlabel(r'$t$')
plt.ylabel(r'$t´$')

'''create t inteval [0, 4] with step 0,1'''
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

t = []
for i in np.linspace(0, 4, num=41):
    t.append(float(toFixed(i, 1)))

'''create date of correlation fuction depend on t'''
def corr_fixed_t1(t1, interval):
    corr_data =[]
    for dg in interval:
        val1 = float(toFixed(t1*t1-2, 2))
        val2 = float(toFixed(dg*dg-2, 2))
        if (val1 <= 0 and val2 <= 0) or (val1 >= 0 and val2 >= 0):
            print(t1, dg, val1, val2, float(toFixed(11 * math.sqrt(val1*val2), 2)))
            sq = 11 * math.sqrt(val1*val2)
            corr_data.append(sq/(math.sqrt(11*math.sqrt(val1*val1))*math.sqrt(11*math.sqrt(val2*val2))))
    return corr_data



def draw():
    for num in t:
        k = corr_fixed_t1(num, t)
        t1 = []
        for i in range(len(k)):
            t1.append(num)

        t2 = []
        if num<= 1.4:
            for el in t:
                if el <= 1.4:
                    t2.append(el)
        else:
            for el in t:
                if el >= 1.5:
                    t2.append(el)
        print('x: ', t1)
        print('y: ', t2)
        print('z: ', k)
        ax.plot3D(t1, t2, k, 'green')

draw()
plt.show()