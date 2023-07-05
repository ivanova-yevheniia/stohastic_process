import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

array = np.array([[-7, 1, 0, 1],
                  [3, -4, 4, 0],
                  [0, 0, -7, 0],
                  [4, 3, 3, -1]])

def func(p, t):
    p1, p2, p3, p4 = p
    dp1dt = -7*p1 + p2 + p4
    dp2dt = 3*p1 + 4*p3 - 4*p2
    dp3dt = -7*p3
    dp4dt = 4*p1 + 3*p2 +3*p3 - p4
    return (dp1dt, dp2dt, dp3dt, dp4dt)

p0 = [0, 0, 0, 1]
t = np.linspace(0, 10, 101)

solution = odeint(func, p0, t)
plt.plot(t, solution[:, 0], label='p1(t)')
plt.plot(t, solution[:, 1], label='p2(t)')
plt.plot(t, solution[:, 2], label='p3(t)')
plt.plot(t, solution[:, 3], label='p4(t)')


A = [[-1, 1/7, 0, 1/7],
    [3/4, -1, 1, -0],
    [0, 0, -1, 0],
    [4, 3, 3, -1]]

A[-1] = [1, 1, 1, 1]
B = [0, 0, 0, 1]
solution = np.linalg.solve(A, B)
print(solution)
plt.axhline(y = solution[0], color = 'b', label = 'p1_final', linestyle = '--')
plt.axhline(y = solution[1], color = 'b', label = 'p2_final', linestyle = '--')
plt.axhline(y = solution[2], color = 'b', label = 'p3_final', linestyle = '--')
plt.axhline(y = solution[3], color = 'b', label = 'p4_final', linestyle = '--')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.grid()
plt.show()