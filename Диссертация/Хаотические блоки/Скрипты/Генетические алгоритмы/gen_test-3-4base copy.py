import numpy as np
import base4 as b4
import findWeight2base
import itertools
import os

Ai = [
    4, 63, 26, 38, 137, 157, 168, 187, 1, 90, 48, 108, 140, 248, 130, 241, 17, 165, 127, 204, 188, 39, 237, 113, 20, 192, 85, 134, 185, 66, 199, 59, 49, 53, 144, 147, 227, 200, 125, 81, 52, 80, 186, 217, 230, 173, 87, 27, 36, 175, 245, 121, 214, 114, 56, 155, 33, 202, 223, 51, 211, 23, 18, 209, 78, 74, 95, 92, 44, 7, 2, 46, 251, 159, 197, 166, 153, 210, 152, 212, 91, 208, 58, 182, 25, 189, 71, 228, 238, 5, 160, 76, 172, 104, 221, 30, 123, 64, 213, 233, 70, 82, 215, 196, 206, 149, 79, 19, 243, 135, 77, 62, 110, 218, 176, 3, 115, 232, 146, 14, 219, 15, 42, 249, 198, 61, 8, 244, 254, 250, 239, 236, 156, 183, 178, 158, 75, 47, 117, 22, 41, 98, 40, 100, 235, 96, 138, 6, 169, 13, 247, 84, 94, 181, 16, 252, 28, 216, 109, 174, 203, 240, 101, 89, 246, 226, 103, 116, 126, 37, 255, 163, 67, 55, 253, 142, 222, 106, 0, 179, 195, 88, 34, 190, 107, 191, 154, 73, 118, 141, 184, 68, 180, 143, 170, 150, 57, 45, 24, 11, 177, 234, 128, 220, 60, 72, 50, 65, 161, 21, 207, 124, 12, 151, 93, 193, 164, 112, 229, 54, 9, 242, 119, 139, 129, 133, 32, 35, 83, 120, 205, 225, 132, 224, 10, 105, 86, 29, 231, 171, 148, 31, 69, 201, 102, 194, 136, 43, 145, 122, 111, 131, 99, 167, 162, 97
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
        
    return [newSbox, affine_matrix]
    

affine_matrix = [[0,0,0,0],
                 [0,0,0,0],
                 [1,1,2,3],
                 [0,0,0,0],]

value = generateSbox(affine_matrix); 
print(len(set(value[0])))
print(value[0])
print(value[1])

# with open(os.getcwd()+'//256py.txt', 'a') as f:
#     f.write('')
#     k = 0
#     permutations = itertools.product([0,1,2,3], repeat=16)
#     for permutation in permutations:
#         a_m = []
#         for i in range(0, 16, 4):
#             a_m.append(list(permutation[i:i+4]))
#         value = generateSbox(a_m); 
#         if (len(value) and value[0]):
#             [S, affine_matrix] = value
#             # print(S)
#             for row in affine_matrix:
#                f.write(str([int(s) for s in row]) + '\n');  
#                f.write('\n\n');
#             # f.write(str([int(i) for i in S]) + '\n'); 
#         k += 1
#         # print(k)

    




 


    
    