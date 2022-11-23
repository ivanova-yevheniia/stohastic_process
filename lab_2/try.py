import numpy as np
import math

'''create t inteval [0, 4] with step 0,1'''
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

t = []
for i in np.linspace(0, 4, num=41):
    t.append(float(toFixed(i, 1)))


def corr_fixed_t1(t1, interval):
    corr_data =[]
    for dg in interval:
        val1 = float(toFixed(t1*t1-2, 2))
        val2 = float(toFixed(dg*dg-2, 2))
        if (val1 < 0 and val2 < 0) or (val1 > 0 and val2 > 0):
            print(t1, dg, val1, val2, float(toFixed(11 * math.sqrt(val1*val2), 2)))
            corr_data.append(float(toFixed(11 * math.sqrt(val1*val2), 2)))
        elif val1 == 0 or val2 == 0:
            print(t1, dg, val1, val2, float(toFixed(11 * math.sqrt(val1 * val2), 2)))
            corr_data.append(0)
    return corr_data

def corr_all_val(interval_1, interval_2):
    corr_all_data = []
    for dg in interval_1:
        corr_all_data.append(corr_fixed_t1(dg, interval_2))
    return corr_all_data
print(t)
print(corr_all_val(t, t))