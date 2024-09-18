import findWeight2base
import findWeight4base
import nonlin
import nonlin4
import ci2

Sbox = [35, 54, 11, 10, 23, 56, 12, 24, 46, 61, 30, 49, 8, 41, 9, 62, 26, 55, 32, 59, 14, 44, 53, 2, 25, 15, 28, 13, 63, 27, 58, 37, 38, 48, 31, 42, 22, 20, 29, 51, 43, 34, 33, 7, 5, 0, 50, 45, 57, 4, 40, 3, 36, 39, 1, 18, 52, 17, 60, 19, 16, 47, 6, 21]


print('SAC 2:\n')
f2 = findWeight2base.calculateWeight(Sbox)
f2.createFuns()
f2.presentMatrix()

print('\nSAC 4:\n')
f4 = findWeight4base.calculateWeight(Sbox)
f4.createFuns()
f4.presentMatrix()

print('\nNonlin 2:\n')
print(min(nonlin.calculateSbox(Sbox)))

print('\nNonlin 4:\n')
print(min(nonlin4.calculateSbox(Sbox)))

print('\nCI:\n')
print(ci2.correlationCalc(Sbox))
