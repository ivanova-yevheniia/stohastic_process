import matplotlib.pyplot as plt
import numpy as np
def s_1(arr):
    s_1 = []
    for t in arr:
        if t<1:
            s_1.append(1)
        elif 1 <= t < 2:
            s_1.append(0.4)
        elif 2 <= t < 3:
             s_1.append(0.25)
        elif 3 <= t < 4:
            s_1.append(0.187)
        elif 4 <= t < 5:
            s_1.append(0.1594)
        elif 5 <= t < 6:
            s_1.append(0.147)
        elif 6 <= t < 7:
            s_1.append(0.1414)
        elif 7 <= t < 8:
            s_1.append(0.1388)
        elif 8 <= t < 9:
            s_1.append(0.1376)
        elif 9 <= t < 10:
            s_1.append(0.137)
        else:
            s_1.append(0.1368)
    return s_1

#t = np.arange(0, 8)

#print(t)
#s1 = s_1(t)
#print(s1)
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s1 = [1, 0.4, 0.25, 0.187, 0.1594, 0.147, 0.1414, 0.1388, 0.1376, 0.137, 0.1368]
s2 = [0, 0.3, 0.33, 0.354, 0.3675, 0.3743, 0.3776, 0.3791, 0.3799, 0.3802, 0.3803]
s3 = [0, 0.2, 0.35, 0.413, 0.4406, 0.453, 0.4586, 0.4612, 0.4624, 0.4629, 0.4632]
s4 = [0, 0.01, 0.07, 0.046, 0.0325, 0.0257, 0.0224, 0.0208, 0.0201, 0.0198, 0.0196]
p = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
fig, ax = plt.subplots()
ax.step(t, s1)
plt.xlabel('t')
plt.xticks(np.arange(len(t)), t)
plt.yticks(p)
plt.show()