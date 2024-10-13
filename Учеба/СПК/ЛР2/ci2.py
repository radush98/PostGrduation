import math

def correlationCalc(Sbox):
    n = len(Sbox)
    k = int(math.log(n, 2))
    qeue = [i for i in range(n)]

    binQeue = [bin(i)[2:].zfill(k)[::-1] for i in qeue]
    binSbox = [bin(i)[2:].zfill(k)[::-1] for i in Sbox]

    matrix = []
    for i in range(k):
        row = []
        for j in range(k):
            res = sum(1 for num in range(n) if int(binSbox[num][i]) ^ int(binQeue[num][j]) == 0)
            correlation = res / n - 0.5 
            row.append(correlation)
        matrix.append(row)

    return matrix