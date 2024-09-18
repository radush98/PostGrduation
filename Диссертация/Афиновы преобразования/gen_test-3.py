import numpy as np

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

irreducible_poly = 0x11B

def generateKey(w0, x0, y0, z0, uw, ux, uy, uz): #∀ ∈ [0, 1], #∀ ∈ [3.57, 4]
    wn, xn, yn, zn = w0, x0, y0, z0
    for n in range(256):
        wn1 = uw*wn*(1-wn)
        xn1 = ux*xn*(1-xn)
        yn1 = uy*yn*(1-yn)
        zn1 = uz*zn*(1-zn)
        
        wn, xn, yn, zn = wn1, xn1, yn1, zn1
    t = wn1 + xn1 + yn1 + zn1
    k = int(abs(t) * 10**4) % 256
    k_binary = format(k, '08b')
    
    return [k, k_binary]  

def generateAffineMatrix(k_binary):
    Rk = np.zeros([8,8])
    Rk[0, :] = [int(i) for i in k_binary]
    
    for m in range(2, 9):
        Rk[m-1, :] = np.roll(Rk[m-2, :], 1)
        
    det = np.linalg.det(Rk)
        
    if det % 2 != 0:
        return Rk
    
    #In other case return to the key generation

def generate_sbox(Rk_matrix):
    sbox = []
    for index in range(0, 256):
        col_vector = np.zeros([8, 1])
        bin_code = format(Ai[index], '08b')
        col_vector[:, 0] = [int(i) for i in bin_code]
        Si = np.dot(Rk_matrix, col_vector) % 2
        createdBinCode = ''.join([str(int(i[0])) for i in Si])
        sbox.append(int(createdBinCode, 2))
    return sbox
   
[k, k_binary] = generateKey(0.5, 0.6, 0.8, 0.7, 3.95, 3.58, 3.92, 3.66); 

# rotationMatrix = generateAffineMatrix(format(k_binary, '08b'))
rotationMatrix = generateAffineMatrix(format(11, '08b'))
print("Matrix >>> ", rotationMatrix)
sbox = generate_sbox(rotationMatrix)

print(sbox)
 


    
    