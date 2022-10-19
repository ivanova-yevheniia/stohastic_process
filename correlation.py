#pip install pandas openpyxl xlsxwriter xlrd
import numpy as np
import pandas as pd
data = [[ 0.834,  0.000,	-0.603,	-0.021,	 0.526,	 1.160,	1.370,	 0.599,	 0.904,	 0.712],
        [-0.609, -0.297,	-0.565,	-0.403,	 0.208,	 0.972,	0.777,	 0.476,	 0.465,	-0.361],
        [ 0.081, -0.178,	-0.788,	-0.477,	 0.471,	-0.354,	1.410,	 0.006,	 0.315,	 0.658],
        [ 0.330, -0.289,	-0.519,	-0.274,	-0.258,	 1.010,	0.534,	 0.569,	 0.468,	 0.626],
        [-0.554, -1.390,	-0.577,	 0.454,	 0.129,	 0.853,	0.378,	 0.245,	-0.289,	-0.297],
        [ 0.670, -0.755,	-0.819,	-0.040,	 0.688,	 0.439,	0.768,	 0.385,	-0.071,	 0.559],
        [ 0.093,  0.569,	-0.592,	 0.235,	 0.506,	-0.170,	0.369,	 0.309,	-0.035,	-0.427],
        [-0.746, -0.582,	 0.009,	-0.203,	 0.874,	 0.826,	0.994,	 1.000,	-0.045,	-0.459],
        [ 0.232, -0.364,	-0.641,	-0.315,	-0.341,	 0.277,	0.317,	 1.240,	 0.296,	 0.317],
        [ 0.274,  1.190,	-0.841,	 0.416,	 0.482,	-0.092,	1.480,	-0.013,	-0.061,	-0.290],
        [-0.505, -0.520,	-0.620,	 0.043,	 0.561,	 1.220,	0.700,	 1.020,	 0.201,	-0.136],
        [-0.992, -1.150,	-0.326,	-0.008,	 0.248,	 0.221,	0.708,	 0.675,	-0.112,	 0.927]]


################################# Main Funktions #################################
# Mx
def expected_value(t: int):
    sum = 0
    for i in range(len(data)):
        sum += data[i][t]
    val = sum / 12
    return val

# R(ti, tj)
def corr_koef(i: int, j: int):
    sum = 0
    m = expected_value(i)*expected_value(j)
    for n in range(12):
        sum += data[n][i]*data[n][j] - m
    return sum/11

# Dx
def dispersion(x: int):
    m = expected_value(x)
    sum = 0
    for n in range(12):
        sum += np.square(data[n][x])-np.square(m)
    dis = sum / 11
    return dis

def corr_norm(corr_koef: float, dxi: float, dxj: float):
    return corr_koef/np.sqrt(dxi*dxj)


################################# Matrix Maker #################################

def matrix_maker(typ: str):
    matrix = [[0] * 10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            if typ == "corr":
                matrix[i][j] = float('{:.4f}'.format(corr_koef(i, j)))
            elif typ == "norm corr":
                matrix[i][j] = float('{:.4f}'.format(corr_norm(corr_koef(i, j), dispersion(i), dispersion(j))))
    return matrix



def matrix_print(matrix: list):
    for row in matrix: print(row)

matrix = matrix_maker("norm corr")
#matrix_print(matrix_maker("norm corr"))
#matrix = matrix_maker("corr")
matrix_print(matrix)

df = pd.DataFrame({'1': matrix[0],
                   '2': matrix[1],
                   '3': matrix[2],
                   '4': matrix[3],
                   '5': matrix[4],
                   '6': matrix[5],
                   '7': matrix[6],
                   '8': matrix[7],
                   '9': matrix[8],
                   '10': matrix[9]})
df.to_excel('norm_corr_m.xlsx')
#print(corr_koef(0, 0))
#print(dispersion(0))
#print(corr_norm(corr_koef(0, 0), dispersion(0), dispersion(0)))

#test for t=10
#print((0.712-0.361+0.658+0.626-0.297+0.559-0.427-0.459+0.317-0.290-0.136+0.927)/12)