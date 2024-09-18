import findWeight2base
import findWeight4base
import nonlin
import nonlin4
import ci2

Sbox =  [0, 1, 57, 46, 37, 26, 23, 33, 43, 31, 13, 51, 50, 10, 41, 39, 44, 29, 54, 35, 63, 60, 32, 6, 25, 24, 5, 36, 45, 17, 42, 9, 22, 7, 55, 19, 27, 4, 40, 15, 38, 14, 30, 8, 16, 28, 3, 56, 53, 58, 12, 11, 59, 48, 18, 34, 47, 2, 49, 52, 21, 62, 61, 20]

print('SAC 2:\n')
f2 = findWeight2base.calculateWeight(Sbox)
f2.createFuns()
f2.presentMatrix()
print(f2.integral())

print('\nSAC 4:\n')
f4 = findWeight4base.calculateWeight(Sbox)
f4.createFuns()
f4.presentMatrix()
print(f4.integral())

print('\nNonlin 2:\n')
print(min(nonlin.calculateSbox(Sbox)))

print('\nNonlin 4:\n')
print(min(nonlin4.calculateSbox(Sbox)))

print('\nCI:\n')
print(ci2.correlationCalc(Sbox))
