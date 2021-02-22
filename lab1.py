import random
import time
start_time=time.time()

a_0 = random.randint(0, 20)
a_1 = random.randint(0, 20)
a_2 = random.randint(0, 20)
a_3 = random.randint(0, 20)
print("A0 = ", a_0)
print("A1 = ", a_1)
print("A2 = ", a_2)
print("A3 = ", a_3)

arrX_1 = random.sample(range(1, 20), 8)
arrX_2 = random.sample(range(1, 20), 8)
arrX_3 = random.sample(range(1, 20), 8)
print("X1:  ", arrX_1)
print("X2:  ", arrX_2)
print("X3:  ", arrX_3)


def findY(a_0, a_1, a_2, a_3, arrX_1, arrX_2, arrX_3):
    arrY = []
    for i in range(8):
        Y = a_0 + a_1 * arrX_1[i] + a_2 * arrX_2[i] + a_3 * arrX_3[i]
        arrY.append(Y)
    return arrY
Y = findY(a_0, a_1, a_2, a_3, arrX_1, arrX_2, arrX_3)

def findX_write(arrX_1, arrX_2, arrX_3):
    X_0 = []
    X_0.append((max(arrX_1) + min(arrX_1))/2)
    X_0.append((max(arrX_2) + min(arrX_2)) / 2)
    X_0.append((max(arrX_3) + min(arrX_3)) / 2)
    return X_0

x0 = findX_write(arrX_1, arrX_2, arrX_3)


def findDX(arrX_1,arrX_2, arrX_3, X_0):
    DX = []
    DX.append(X_0[0] - min(arrX_1))
    DX.append(X_0[1] - min(arrX_2))
    DX.append(X_0[2] - min(arrX_3))
    return DX

x0 = findX_write(arrX_1, arrX_2, arrX_3)
DX = findDX(arrX_1,arrX_2, arrX_3, x0)
def findX_norm(arrX_1, arrX_2, arrX_3, x0, DX):
    Xn1=[]
    for i in range(8):
        xn1 = round((arrX_1[i] - x0[0]) / DX[0], 2)
        Xn1.append(xn1)
    print("XN1: ", Xn1)
    Xn2 = []
    for j in range(8):
        xn2 = round((arrX_2[j] - x0[1]) / DX[1], 2)
        Xn2.append(xn2)        
        '''за допомогою цього циклу ми знаходимо нормоване значення для кожного фактору, 
        що знаходиться у стовпці "X2"(у моєму випадку в списку arrX_2), 
        ідентичні цикли можна спостерігати у рядках 51 та 66, цей цикл перебирає кожен елемент списку arrX_2, 
        проводить із ним відповідні математичні операції і додає у список нові xn2 елементи з кожною ітерацією
        '''
    print("XN2: ", Xn2)
    Xn3 = []
    for k in range(8):
        xn3 = round((arrX_3[k] - x0[2]) / DX[2], 2)
        Xn3.append(xn3)
    print("XN3: ", Xn3)

def findcrit(arrX_1,arrX_2,arrX_3,Y):
    xs = []
    for i in range(8):
        if Y[i] == min(Y):
            xs.append(arrX_1[i])
            xs.append(arrX_2[i])
            xs.append(arrX_3[i])
            return xs , Y[i]

print("Y:   ", Y)
print("X0:  ", x0)
print("dx:  ", DX)
findX_norm(arrX_1, arrX_2, arrX_3, x0, DX)
print("Optimal point Ymin : ", findcrit(arrX_1, arrX_2, arrX_3,Y))
print("Execution time: %s seconds " % (time.time() - start_time))
