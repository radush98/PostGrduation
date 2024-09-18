from PIL import Image
import numpy as np
import os
import hc_mrlm
import evaluation

Sbox = [5, 0, 10, 122, 91, 161, 194, 101, 191, 103, 219, 244, 28, 145, 238, 188, 20, 30, 78, 25, 181, 214, 121, 111, 123, 239, 200, 131, 165, 242, 128, 32, 34, 82, 45, 40, 234, 77, 115, 137, 243, 220, 151, 79, 198, 148, 52, 185, 102, 49, 60, 54, 81, 71, 157, 254, 224, 171, 83, 199, 168, 8, 141, 218, 65, 75, 187, 70, 226, 3, 166, 152, 164, 24, 53, 252, 210, 47, 253, 93, 95, 143, 90, 85, 23, 186, 172, 246, 44, 9, 192, 184, 51, 193, 97, 230, 147, 110, 105, 99, 142, 176, 202, 43, 29, 212, 140, 48, 213, 117, 250, 7, 114, 125, 119, 167, 132, 222, 63, 146, 232, 144, 4, 33, 73, 206, 27, 233, 136, 248, 135, 130, 64, 231, 217, 35, 89, 118, 61, 229, 108, 62, 158, 19, 204, 155, 150, 156, 251, 237, 55, 84, 74, 1, 249, 109, 2, 162, 39, 112, 175, 170, 160, 208, 241, 11, 104, 207, 21, 205, 113, 94, 182, 59, 68, 22, 190, 180, 228, 179, 31, 124, 211, 197, 209, 69, 98, 41, 15, 88, 42, 138, 57, 196, 195, 201, 36, 26, 96, 129, 183, 126, 38, 154, 127, 223, 80, 173, 216, 215, 221, 13, 46, 116, 149, 56, 66, 58, 174, 139, 227, 100, 177, 67, 235, 225, 17, 236, 72, 169, 12, 50, 14, 178, 159, 86, 120, 133, 87, 247, 245, 37, 240, 255, 189, 16, 6, 92, 134, 163, 106, 18, 153, 107, 203, 76]

# Sbox = [4, 63, 26, 38, 137, 157, 168, 187, 1, 90, 48, 108, 140, 248, 130, 241, 17, 165, 127, 204, 188, 39, 237, 113, 20, 192, 85, 134, 185, 66, 199, 59, 49, 53, 144, 147, 227, 200, 125, 81, 52, 80, 186, 217, 230, 173, 87, 27, 36, 175, 245, 121, 214, 114, 56, 155, 33, 202, 223, 51, 211, 23, 18, 209, 78, 74, 95, 92, 44, 7, 2, 46, 251, 159, 197, 166, 153, 210, 152, 212, 91, 208, 58, 182, 25, 189, 71, 228, 238, 5, 160, 76, 172, 104, 221, 30, 123, 64, 213, 233, 70, 82, 215, 196, 206, 149, 79, 19, 243, 135, 77, 62, 110, 218, 176, 3, 115, 232, 146, 14, 219, 15, 42, 249, 198, 61, 8, 244, 254, 250, 239, 236, 156, 183, 178, 158, 75, 47, 117, 22, 41, 98, 40, 100, 235, 96, 138, 6, 169, 13, 247, 84, 94, 181, 16, 252, 28, 216, 109, 174, 203, 240, 101, 89, 246, 226, 103, 116, 126, 37, 255, 163, 67, 55, 253, 142, 222, 106, 0, 179, 195, 88, 34, 190, 107, 191, 154, 73, 118, 141, 184, 68, 180, 143, 170, 150, 57, 45, 24, 11, 177, 234, 128, 220, 60, 72, 50, 65, 161, 21, 207, 124, 12, 151, 93, 193, 164, 112, 229, 54, 9, 242, 119, 139, 129, 133, 32, 35, 83, 120, 205, 225, 132, 224, 10, 105, 86, 29, 231, 171, 148, 31, 69, 201, 102, 194, 136, 43, 145, 122, 111, 131, 99, 167, 162, 97]
Pbox = [0, 1, 2, 163, 210, 240, 83, 120, 150, 217, 57, 60, 70, 104, 200, 80, 115, 142, 110, 30, 33, 40, 194, 221, 50, 154, 178, 235, 98, 37, 19, 58, 216, 20, 218, 62, 183, 29, 117, 114, 21, 143, 149, 140, 136, 106, 88, 172, 198, 103, 24, 207, 229, 202, 119, 74, 184, 10, 31, 109, 11, 108, 35, 176, 101, 167, 144, 161, 134, 153, 12, 179, 96, 234, 55, 214, 191, 196, 219, 193, 15, 241, 212, 6, 112, 188, 180, 175, 46, 99, 169, 186, 111, 182, 170, 113, 72, 118, 28, 89, 105, 64, 155, 49, 13, 100, 45, 165, 61, 59, 18, 92, 84, 95, 39, 16, 192, 38, 97, 54, 7, 211, 162, 127, 204, 233, 129, 123, 157, 126, 238, 205, 208, 201, 68, 195, 44, 215, 189, 213, 43, 220, 17, 41, 66, 203, 228, 197, 190, 42, 8, 164, 242, 69, 25, 102, 239, 128, 232, 230, 209, 67, 122, 3, 151, 107, 171, 65, 224, 90, 94, 166, 47, 174, 173, 87, 63, 199, 26, 71, 86, 222, 93, 36, 56, 236, 91, 223, 85, 138, 148, 76, 116, 79, 22, 135, 77, 147, 48, 177, 14, 133, 53, 145, 124, 131, 226, 51, 132, 160, 4, 121, 82, 139, 75, 137, 32, 9, 34, 78, 141, 23, 181, 187, 168, 231, 206, 237, 146, 52, 159, 225, 158, 125, 73, 27, 185, 227, 130, 156, 5, 81, 152]
H = 0
W = 0

# Separating to the blocks 9x9x3
def decompose_image(image_path, block_size=(9, 9, 3), addModification=False):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    if(addModification):
        R = img_array[:,:,0]
        G = img_array[:,:,1]
        B = img_array[:,:,2]
        
        R[23,65] = 100
        G[155, 321] = 50
        B[322, 100] = 150
        
        img_array=np.stack([R, G, B], axis=-1)

    height, width, channels = img_array.shape
    
    num_blocks_height = height // block_size[0]
    num_blocks_width = width // block_size[1]
    
    global H, W
    H = num_blocks_height * 9
    W = num_blocks_width * 9

    blocks = []

    for i in range(num_blocks_height):
        for j in range(num_blocks_width):
            block = img_array[i * block_size[0]: (i + 1) * block_size[0],
                              j * block_size[1]: (j + 1) * block_size[1], :]
            blocks.append(block)
    return blocks

# Replace matrix by the S-box rule
def replaceMatrixWithSbox(matrix):
    newMatrix = []
    for row in matrix:
        newMatrix.append([Sbox[item] for item in row])
    
    return newMatrix

def replaceMatrixWithPbox(matrix):
    sequence = np.array(matrix).flatten('F')
    print(sequence)
    
    permuted_sequence = np.zeros(243)
    
    for i in range(243):
        permuted_sequence[Pbox[i]] = sequence[i]
                
    return permuted_sequence
    
    # permuted_block = permuted_sequence.reshape((9, 9, 3))
    # return permuted_block

def replaceWithSbox(blocks):
    replacedBlocks = []
    for block in blocks:
        newBlock = np.dstack((
            replaceMatrixWithSbox(block[:,:,0]),
            replaceMatrixWithSbox(block[:,:,1]),
            replaceMatrixWithSbox(block[:,:,2])
        ))
                
        replacedBlocks.append(newBlock)
        
    return replacedBlocks

def replaceWithPBox(blocks):
    replacedBlocks = []
    for block in blocks:
        matrix_1D = np.concatenate([
            np.array(block[:, :, 0]).flatten('F'),
            np.array(block[:, :, 1]).flatten('F'),
            np.array(block[:, :, 2]).flatten('F')
        ])

        replacedBlocks.append(matrix_1D)
    return np.concatenate(replacedBlocks)

def gammaToInteger(binaries):
    integers = []
    for i in range(0, len(binaries), 8):
        sequence = binaries[i:i+8]
        integers.append(int(''.join([str(elem) for elem in sequence]), 2))
    
    return integers

def xor(blocks, gamma):
    res = []
    res.append(blocks[0]^gamma[0])
    
    for i in range(1, len(blocks)):
        res.append(blocks[i]^blocks[i-1]^gamma[i])
        
    return res

def convert1Dto3D(array_1d:list, H, W):
    target = np.array(array_1d)
    
    r_array = target[0:H*W].reshape((H, W), order='F')
    g_array = target[H*W: H*W*2].reshape((H, W), order='F')
    b_array = target[H*W*2: H*W*3].reshape((H, W), order='F')
    
    return np.dstack((r_array, g_array, b_array)) 

image_path = os.path.abspath("./test.jpg")
blocks = decompose_image(image_path)
blocks_S = replaceWithSbox(blocks)
blocks_P = replaceWithPBox(blocks_S)
gamma = gammaToInteger(hc_mrlm.hyperChaos(len(blocks_P) * 8))
xored = xor(blocks_P, gamma)
blocks_decrypted = np.array(convert1Dto3D(xored, H, W))

# -------------------------------------------------------------

blocks1 = decompose_image(image_path, (9, 9, 3), True)
blocks_S1 = replaceWithSbox(blocks1)
blocks_P1 = replaceWithPBox(blocks_S1)
gamma1 = gammaToInteger(hc_mrlm.hyperChaos(len(blocks_P1) * 8))
xored1 = xor(blocks_P1, gamma1)
blocks_decrypted1 = convert1Dto3D(xored1, H, W)

NPCR_R = evaluation.NPCR(blocks_decrypted[:,:,0], blocks_decrypted1[:,:,0])
NPCR_G = evaluation.NPCR(blocks_decrypted[:,:,1], blocks_decrypted1[:,:,1])
NPCR_B = evaluation.NPCR(blocks_decrypted[:,:,2], blocks_decrypted1[:,:,2])

UACI_R = evaluation.UACI(blocks_decrypted[:,:,0], blocks_decrypted1[:,:,0])
UACI_G = evaluation.UACI(blocks_decrypted[:,:,1], blocks_decrypted1[:,:,1])
UACI_B = evaluation.UACI(blocks_decrypted[:,:,2], blocks_decrypted1[:,:,2])

print(NPCR_R, NPCR_G, NPCR_B)
print(UACI_R, UACI_G, UACI_B)