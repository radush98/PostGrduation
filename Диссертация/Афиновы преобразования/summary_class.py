import findWeight2base
import findWeight4base
import nonlin
import nonlin4
import ci2

class Summary():
    def __init__(self, Sbox):
        self.Sbox = Sbox 
        self.calc()
    
    def calc(self):
        print('SAC 2:\n')
        f2 = findWeight2base.calculateWeight(self.Sbox)
        f2.createFuns()
        f2.presentMatrix()

        print('\nSAC 4:\n')
        f4 = findWeight4base.calculateWeight(self.Sbox)
        f4.createFuns()
        f4.presentMatrix()

        # print('\nNonlin 2:\n')
        # print(min(nonlin.calculateSbox(self.Sbox)))

        # print('\nNonlin 4:\n')
        # print(min(nonlin4.calculateSbox(self.Sbox)))

        # print('\nCI:\n')
        # print(ci2.correlationCalc(self.Sbox))


