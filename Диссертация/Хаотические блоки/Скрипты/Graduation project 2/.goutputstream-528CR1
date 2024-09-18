import numpy as np

L = np.array([
    [1, 0],
    [1, 1],
])


def createRow(rule, matrix):
    row = [[] for j in range(len(matrix))]
    for i in rule:
        row = np.concatenate((row, matrix * i), axis=1)
    return row


def createL(matrix):
    row1 = createRow(L[0], matrix)
    row2 = createRow(L[1], matrix)

    VK = np.concatenate((
        np.concatenate((row1, row2), axis=0),
    ), axis=0)
    return VK


def createLn(k):
    matrix = L;
    while k != 1:
        matrix = createL(matrix)
        k -= 1
    return matrix


# print([int(i % 2) for i in np.matmul(createLn(3), [1, 0, 0, 1, 0, 0, 1, 1])])

print([int(i % 2) for i in np.matmul(createLn(5), [1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0])])

