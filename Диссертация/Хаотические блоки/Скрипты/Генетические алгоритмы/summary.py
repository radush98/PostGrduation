import findWeight2base
import findWeight4base
import nonlin
import nonlin4
import ci2

Sbox = [8, 10, 1, 9, 3, 11, 0, 2, 14, 12, 13, 5, 15, 7, 6, 4]

print('SAC 2:\n')
f2 = findWeight2base.calculateWeight(Sbox)
f2.createFuns()
f2.presentMatrix()
f2.integral()

print('\nSAC 4:\n')
f4 = findWeight4base.calculateWeight(Sbox)
f4.createFuns()
f4.presentMatrix()
f4.integral()

print('\nNonlin 2:\n')
print(min(nonlin.calculateSbox(Sbox)))

print('\nNonlin 4:\n')
print(min(nonlin4.calculateSbox(Sbox)))

print('\nCI:\n')
print(ci2.correlationCalc(Sbox))
