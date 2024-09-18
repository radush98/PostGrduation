import math

def correlationCalc(Sbox):
    n = len(Sbox)
    k = int(math.log(n,2))
    qeue = [i for i in range(0,n)]

    binQeue = [bin(i)[2:].zfill(k)[::-1] for i in qeue]
    binSbox = [bin(i)[2:].zfill(k)[::-1] for i in Sbox]

    matrix = []
    for i in range(0, k):
        matrix.append([])
        for j in range(0,k):
            res = sum([int(binSbox[num][i]) ^ int(binQeue[num][j]) for num in range(0,n)])
            matrix[i].append(1 - (res/(2**(k-1))))

    return matrix