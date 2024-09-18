import numpy as np
import base4 as b4
import itertools
import os
import findWeight2base as f2
import findWeight4base as f4
import nonlin as n2
import nonlin4 as n4
    
Ai = [35, 54, 11, 10, 23, 56, 12, 24, 46, 61, 30, 49, 8, 41, 9, 62, 26, 55, 32, 59, 14, 44, 53, 2, 25, 15, 28, 13, 63, 27, 58, 37, 38, 48, 31, 42, 22, 20, 29, 51, 43, 34, 33, 7, 5, 0, 50, 45, 57, 4, 40, 3, 36, 39, 1, 18, 52, 17, 60, 19, 16, 47, 6, 21]

gf_4_mult = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
]

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
          
    print(len(set(newSbox)))  
    if len(set(newSbox)) == 64:
        return [newSbox, affine_matrix]
    
    return []

def main():
    with open('bijective-test-2.txt', 'r') as f1:
        f1.write('')
    
    with open('bijective-test-2.txt', 'a') as f1, open('bijective-non2-matrix-SAC4.txt', 'r') as f2:
        for matrix in f2:
            value = generateSbox(eval(matrix))
            
            if len(value) > 0:
                f1.write(str(value[0]) + '\n')

main()

 


    
    