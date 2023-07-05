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
    dp1dt = -3*p1 + p2 + p3
    dp2dt = 3*p1 -5*p2 + p3 + 3*p5
    dp3dt = 2 * p2 - 4 * p3 + 4*p4
    dp4dt = - 4 * p4 + 2 * p5
    dp5dt = 2 * p2 + 2 * p3 - 5 * p5
    return (dp1dt, dp2dt, dp3dt, dp4dt, dp5dt)


p0 = [0, 0, 1, 0, 0]
epsilon = 0.0001
nodes_numb = 101
t_0 = 0
delta = 10
t_n = delta
t = np.linspace(t_0, t_n, nodes_numb)
solution = odeint(func, p0, t)
probabs = solution
approx_probab_limits = [None] * 5

while any([element is None for element in approx_probab_limits]):
    for i in range(len(solution) - 1):
        for j in range(len(solution[i])):
            if abs(solution[i][j] - solution[i + 1][j]) < epsilon and approx_probab_limits[j] is None:
                approx_probab_limits[j] = solution[i][j]
                print("------")
                print(f"p_{j + 1}(t_i) = {solution[i][j]}")
                print(solution[i])
                print(solution[i + 1])
                print(f"t[i] = {t[i]}, t_i+1 = {t[i + 1]}")
        if all([element is not None for element in approx_probab_limits]):
            approx_probab_limits = solution[i]
            break

    p0 = solution[-1]
    t_0 = t_n
    t_n += delta
    t = np.linspace(t_0, t_n, nodes_numb)[1:]
    solution = odeint(func, p0, t)
    probabs = np.concatenate((probabs, solution))

# print(f"solutions:")
# [print(s) for s in probabs[:-100]]
print(f"Approximate limits with accuracy {epsilon}:")
approx_probab_limits = np.array(approx_probab_limits)
print(approx_probab_limits)
t = np.linspace(0, t_n, int(t_n / delta) * 100 + 1)
[plt.plot(t, probabs[:, i], label=f'p{i + 1}(t)') for i in range(5)]

A = [[-1, 1/3, 1/3, 0, 0],
     [3 / 5, -1, 1/5, 0, 3/5],
     [0, 1 / 2, -1, 1, 0],
     [0, 0, 0, -1, 1/2],
     [0, 2 / 5, 2 / 5, 0, -1]]

A[-1] = [1, 1, 1, 1, 1]
B = [0, 0, 1, 0, 0]
limits = np.linalg.solve(A, B)
print("limits:")
print(limits)
#[plt.axhline(p_final, color='black', linestyle='--') for p_final in limits]
plt.axhline(y = 0.1724, color = 'b', label = 'p1_final', linestyle = '--')
plt.axhline(y = 0.2759, color = 'b', label = 'p2_final', linestyle = '--')
plt.axhline(y = 0.2414, color = 'b', label = 'p3_final', linestyle = '--')
plt.axhline(y = 0.1034, color = 'b', label = 'p4_final', linestyle = '--')
plt.axhline(y = 0.2069, color = 'b', label = 'p5_final', linestyle = '--')
print("[approx_i - final_i]:")
print(limits - approx_probab_limits)
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
