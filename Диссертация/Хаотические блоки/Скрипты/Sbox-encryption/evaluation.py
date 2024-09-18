import numpy as np

def UACI(E1, E2):
    result_matrix = []

    for i in range(len(E1)):
        row = []
        for j in range(len(E1[i])):
            row.append(E1[i][j] - E2[i][j])
        result_matrix.append(row)
        
    matrix = np.matrix(result_matrix)
    return matrix.sum()/(255 * len(E1) * len(E1[0]))

def NPCR(E1, E2):
    result_matrix = []
    
    print(len(E1), len(E1[0]))

    for i in range(len(E1)):
        row = []
        for j in range(len(E1[i])):
            if (E1[i][j] == E2[i][j]):
                row.append(0)
            else:
                row.append(1)
        result_matrix.append(row)
        
    matrix = np.matrix(result_matrix)
    return matrix.sum()/(len(E1) * len(E1[0]))
    