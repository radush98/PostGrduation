import numpy as np
import math
import base4

V4 = np.array([
                [0, 0, 0, 0],
                [0, 1, 2, 3],
                [0, 2, 0, 2],
                [0, 3, 2, 1]
            ]);

def createRow(rule, matrix):
    row = [ [] for j in range(len(matrix)) ];
    for i in rule:
        row = np.concatenate((row, matrix + i), axis=1);
    return row

def mod4(matrix):
    for i in range(0, len(matrix)):
        matrix[i] = [math.fmod(elem, 4) for elem in matrix[i]];
    return matrix;

def toComplex(row):
    complexRow = [];
    for i in row:
        if i == 0:
            complexRow.append(complex(1,0))
        if i == 1:
            complexRow.append(complex(0,1))
        if i == 2:
            complexRow.append(complex(-1,0))
        if i == 3:
            complexRow.append(complex(0,-1))
    return complexRow

def toComplexMatrix(matrix):
    complexMatrix = [[] for i in range(0, len(matrix))]
    for i in range(0, len(matrix)):
        complexMatrix[i] = toComplex(matrix[i]);
    return complexMatrix

def createV(matrix):
    row1 = createRow(V4[0], matrix);
    row2 = createRow(V4[1], matrix);
    row3 = createRow(V4[2], matrix);
    row4 = createRow(V4[3], matrix);

    VK = np.concatenate((
        np.concatenate((row1,row2), axis = 0),
        np.concatenate((row3,row4), axis = 0),
    ),axis = 0)
    return mod4(VK)

def createVk(k):
    matrix = V4;
    while k != 1:
        matrix = createV(matrix);
        k -= 1;
    return toComplexMatrix(matrix);

def getDistance(func4):
    k = math.log(len(func4), 4);
    VK = createVk(k);
    f4 = np.array(toComplex(func4));

    absValues = [abs(i) for i in f4.dot(VK)];
    L = max([abs(i) for i in absValues])
    distance = 4**k - L;
    return distance

def calculateSbox(Sbox):
    S = base4.divideToFunctions(Sbox, False, len(Sbox));
    distances = [];

    for func in S:
        func = [int(i) for i in func];
        distances.append(getDistance(func));
    return distances