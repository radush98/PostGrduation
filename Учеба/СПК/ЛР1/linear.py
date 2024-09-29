import lsfr

polinoms = [
    [1,0,1,0,0,1],
    [1,0,0,1,0,1],
    [1,1,1,1,0,1],
    [1,1,1,0,1,1],
    [1,1,0,1,1,1],
    [1,0,1,1,1,1]
]

for polinom in polinoms:
    res = lsfr.enlarge([1,1,1,1,1], 31, polinom)
    sequence = ''.join([str(i) for i in res])
    sequence = sequence.replace('0000', '00000')
    
    zerosIndex = sequence.index('00000')
    newSequence = sequence[zerosIndex:] + sequence[0:zerosIndex]
    
    print(int(newSequence, 2))
    
    






