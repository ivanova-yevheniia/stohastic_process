import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

array = np.array([[-3, 1, 1, 0, 0],
                  [3, -5, 1, 0, 3],
                  [0, 2, -4, 4, 0],
                  [0, 0, 0, -4, 2],
                  [0, 2, 2, 0, -5]])

def func(p, t):
    p1, p2, p3, p4, p5 = p
    dp1dt = -3 * p1 + p2 + p3
    dp2dt = 3 * p1 - 5 * p2 + p3 + 3 * p5
    dp3dt = 2 * p2 - 4 * p3 + 4 * p4
    dp4dt = - 4 * p4 + 2 * p5
    dp5dt = 2 * p2 + 2 * p3 - 5 * p5
    return (dp1dt, dp2dt, dp3dt, dp4dt, dp5dt)

p0 = [0, 1, 0, 0]
t = np.linspace(0, 10, 101)

solution = odeint(func, p0, t)
plt.plot(t, solution[:, 0], label='p1(t)')
plt.plot(t, solution[:, 1], label='p2(t)')
plt.plot(t, solution[:, 2], label='p3(t)')
plt.plot(t, solution[:, 3], label='p4(t)')
plt.plot(t, solution[:, 4], label='p5(t)')


A = [[-1, 1/3, 1/3, 0, 0],
     [3 / 5, -1, 1/5, 0, 3/5],
     [0, 1 / 2, -1, 1, 0],
     [0, 0, 0, -1, 1/2],
     [0, 2 / 5, 2 / 5, 0, -1]]

A[-1] = [1, 1, 1, 1, 1]
B = [0, 0, 1, 0, 0]
solution = np.linalg.solve(A, B)
print(solution)
plt.axhline(y = solution[0], color = 'b', label = 'p1_final', linestyle = '--')
plt.axhline(y = solution[1], color = 'b', label = 'p2_final', linestyle = '--')
plt.axhline(y = solution[2], color = 'b', label = 'p3_final', linestyle = '--')
plt.axhline(y = solution[3], color = 'b', label = 'p4_final', linestyle = '--')
plt.axhline(y = solution[4], color = 'b', label = 'p5_final', linestyle = '--')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.grid()
plt.show()