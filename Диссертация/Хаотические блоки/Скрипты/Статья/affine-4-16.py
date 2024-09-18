import numpy as np
import base4 as b4
import itertools
import os
import findWeight2base as f2
import findWeight4base as f4
import nonlin as n2
import nonlin4 as n4
    
Ai = [0, 17, 51, 55, 46, 34, 42, 25, 38, 12, 59, 4, 29, 8, 63, 21, 33, 3, 7, 16, 50, 58, 41, 62, 28, 11, 20, 54, 24, 15, 37, 45, 19, 23, 32, 49, 10, 57, 14, 2, 27, 36, 6, 44, 31, 53, 61, 40, 39, 48, 1, 35, 9, 30, 18, 26, 52, 22, 60, 43, 5, 13, 56, 47]

gf_4_mult = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
]

targetMatrix = [
    [24, 32, 32, 32, 32, 32],
    [32, 32, 32, 32, 32, 32],
    [24, 32, 32, 32, 24, 32],
    [32, 32, 32, 32, 32, 32],
    [40, 32, 32, 32, 40, 32],
    [32, 32, 32, 32, 32, 32]
]

def satisfiesSAC4(matrix):   
    for row in matrix:
        for elem in row:
            if elem != 16:
                return False
    
    return True

def isNonLinear(matrix):
    m = np.array(matrix)
    rank = np.linalg.matrix_rank(m)
    
    if rank == min(m.shape):
        return True
    
    return False

def multiplicateElems(elem1, elem2):
    return gf_4_mult[elem1][elem2]

def multiplicateInGf4(v_col, matrix):
    if (len(v_col) != len(matrix)):
        print("Dimensions mismatched")
        return []
    
    res_matrix = []
    for i in range(len(v_col)):
       v = v_col[i][0]
       res_matrix.append(sum([multiplicateElems(v, matrix[j][i]) for j in range(len(matrix))]) % 4)
       
    return res_matrix

def generateSbox(affine_matrix):
    newSbox = []
    for i in Ai:
        v = [[int(symbol)] for symbol in b4.toFourBase(i, 3)]
        res = [str(weight) for weight in multiplicateInGf4(v, affine_matrix)]
        newSbox.append(int(''.join(res), 4))
    
    w2 = f2.calculateWeight(newSbox)
    w4 = f4.calculateWeight(newSbox)
    non2 = min(n2.calculateSbox(newSbox))
            
    if len(set(newSbox)) == 64 and isNonLinear(affine_matrix) and non2 == 16 and satisfiesSAC4(w4.createFuns()):
        return [newSbox, affine_matrix]
    
    return []

def main():
    with open('bijective-non2-SAC4.txt', 'w') as f1, open('bijective-non2-matrix-SAC4.txt', 'w') as f2:
        f1.write('')
        f2.write('')
    
    permutations = itertools.product([0,1,2,3], repeat=9)
    i = 0
    with open('bijective-non2-SAC4.txt', 'a') as f1, open('bijective-non2-matrix-SAC4', 'a') as f2:
        for perm in permutations:
            p = list(perm)

            a_m = [
                p[0:3],
                p[3:6],
                p[6:9]
            ]

            value = generateSbox(a_m)
            
            if len(value) > 0:
                f1.write(str(value[0]) + '\n')
                f2.write(str(value[1]) + '\n')

main()

 


    
    