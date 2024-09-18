import base4 as b4
import os
import summary_class as sm

    
Ai = [0, 1, 57, 46, 37, 26, 23, 33, 43, 31, 13, 51, 50, 10, 41, 39, 44, 29, 54, 35, 63, 60, 32, 6, 25, 24, 5, 36, 45, 17, 42, 9, 22, 7, 55, 19, 27, 4, 40, 15, 38, 14, 30, 8, 16, 28, 3, 56, 53, 58, 12, 11, 59, 48, 18, 34, 47, 2, 49, 52, 21, 62, 61, 20]

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
    
    if len(set(newSbox)) == 64:
        return [newSbox, affine_matrix]
    
    return []

def main():
     with open(os.getcwd()+'\\gen4-matrix.txt', 'r') as f:
        for matrix in f:
            value = generateSbox(eval(matrix))
            if value:
                sm.Summary(value[0])

main()

 


    
    