import numpy as np
import base4 as b4
import findWeight2base
import itertools
import os

Ai = [
    0, 1, 141, 246, 203, 82, 123, 209, 232, 79, 41, 192, 176, 225, 229, 199,
    116, 180, 170, 75, 153, 43, 96, 95, 88, 63, 253, 204, 255, 64, 238, 178, 
    58, 110, 90, 241, 85, 77, 168, 201, 193, 10, 152, 21, 48, 68, 162, 194,
    44, 69, 146, 108, 243, 57, 102, 66, 242, 53, 32, 111, 119, 187, 89, 25,
    29, 254, 55, 103, 45, 49, 245, 105, 167, 100, 171, 19, 84, 37, 233, 9,
    237, 92, 5, 202, 76, 36, 135, 191, 24, 62, 34, 240, 81, 236, 97, 23,
    22, 94, 175, 211, 73, 166, 54, 67, 244, 71, 145, 223, 51, 147, 33, 59,
    121, 183, 151, 133, 16, 181, 186, 60, 182, 112, 208, 6, 161, 250, 129, 130, 
    131, 126, 127, 128, 150, 115, 190, 86, 155, 158, 149, 217, 247, 2, 185, 164, 
    222, 106, 50, 109, 216, 138, 132, 114, 42, 20, 159, 136, 249, 220, 137, 154, 
    251, 124, 46, 195, 143, 184, 101, 72, 38, 200, 18, 74, 206, 231, 210, 98, 12,
    224, 31, 239, 17, 117, 120, 113, 165, 142, 118, 61, 189, 188, 134, 87, 
    11, 40, 47, 163, 218, 212, 228, 15, 169, 39, 83, 4, 27, 252, 172, 230,
    122, 7, 174, 99, 197, 219, 226, 234, 148, 139, 196, 213, 157, 248, 144, 107,
    177, 13, 214, 235, 198, 14, 207, 173, 8, 78, 215, 227, 93, 80, 30, 179,
    91, 35, 56, 52, 104, 70, 3, 140, 221, 156, 125, 160, 205, 26, 65, 28
]

# affine_matrix = [
#     [1, 0, 2, 3],
#     [3, 1, 0, 2],
#     [2, 3, 1, 0],
#     [0, 2, 3, 1],
# ]

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
        v = [[int(symbol)] for symbol in b4.toFourBase(i, 4)]
        res = [str(weight) for weight in multiplicateInGf4(v, affine_matrix)]
        newSbox.append(int(''.join(res), 4))
        
    # f2 = findWeight2base.calculateWeight(newSbox)
    # f2.createFuns()
    
    # if len(set(newSbox)) == 256 and f2.isMatrixValid():
    if len(set(newSbox)) == 256:
        print(affine_matrix)
        return [newSbox, affine_matrix]
    
    return []

with open(os.getcwd()+'//256py.txt', 'a') as f:
    f.write('')
    k = 0
    permutations = itertools.product([0,1,2,3], repeat=16)
    for permutation in permutations:
        a_m = []
        for i in range(0, 16, 4):
            a_m.append(list(permutation[i:i+4]))
        value = generateSbox(a_m); 
        if (len(value) and value[0]):
            [S, affine_matrix] = value
            # print(S)
            for row in affine_matrix:
               f.write(str([int(s) for s in row]) + '\n');  
               f.write('\n\n');
            # f.write(str([int(i) for i in S]) + '\n'); 
        k += 1
        # print(k)

    




 


    
    