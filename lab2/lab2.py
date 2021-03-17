import random
import numpy as np
import math

var = 317
m = 6

yMax = (30 - var) * 10
yMin = (20 - var) * 10
x1Min = -10
x1Max = 50
x2Min = 20
x2Max = 60

xn = [[-1, -1], [1, -1], [-1, 1]]

Y = [[random.randint(yMin, yMax) for i in range(m)] for j in range(3)]
print(f"Planning matrix for m = {m}:")
for i in range(3):
    print(Y[i])

Y_average = []
for i in range(len(Y)):
    Y_average.append(np.mean(Y[i]))

dispersions = []
for i in range(len(Y)):
    sum = 0
    for k in Y[i]:
        sum += (k - np.mean(Y[i])) ** 2
    dispersions.append(sum / len(Y[i]))
print("Dispersion:", dispersions)


def determinant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    deter = x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33
    return deter



sigma_teta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

fuv = [max(dispersions[0], dispersions[1]) / min(dispersions[0], dispersions[1]),
       max(dispersions[2], dispersions[0]) / min(dispersions[2], dispersions[0]),
       max(dispersions[2], dispersions[1]) / min(dispersions[2], dispersions[1])]

teta = [((m - 2) / m) * fuv[0], ((m - 2) / m) * fuv[1], ((m - 2) / m) * fuv[2]]

ruv = [abs(teta[0] - 1) / sigma_teta, abs(teta[1] - 1) / sigma_teta, abs(teta[2] - 1) / sigma_teta]

r_kr = 2

if ruv[0] > r_kr:
    print("Inhomogeneous dispersion")
elif ruv[1] > r_kr:
    print("Inhomogeneous dispersion")
elif ruv[2] > r_kr:
    print("Inhomogeneous dispersion")
else:
    print("Experimental values for Romanovsky criterion:")
    for i in range(3):
        print(ruv[i])

    mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
    mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
    my = (Y_average[0] + Y_average[1] + Y_average[2]) / 3

    a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
    a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
    a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
    a11 = (xn[0][0] * Y_average[0] + xn[1][0] * Y_average[1] + xn[2][0] * Y_average[2]) / 3
    a22 = (xn[0][1] * Y_average[0] + xn[1][1] * Y_average[1] + xn[2][1] * Y_average[2]) / 3

    b0 = determinant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
    b1 = determinant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
    b2 = determinant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

    yNorm1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
    yNorm2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
    yNorm3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]

    dx1 = abs(x1Max - x1Min) / 2
    dx2 = abs(x2Max - x2Min) / 2
    x10 = (x1Max + x1Min) / 2
    x20 = (x2Max + x2Min) / 2

    a_0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
    a_1 = b1 / dx1
    a_2 = b2 / dx2

    yNat1 = a_0 + a_1 * x1Min + a_2 * x2Min
    yNat2 = a_0 + a_1 * x1Max + a_2 * x2Min
    yNat3 = a_0 + a_1 * x1Min + a_2 * x2Max

    print("Average values:", Y_average[0], Y_average[1], Y_average[2])
    print("Normalized coefficients:", round(yNorm1, 4), round(yNorm2, 4), round(yNorm3, 4))
    print("Naturalized coefficients:", round(yNat1, 4), round(yNat2, 4), round(yNat3, 4))
