import base4recursia
import findWeight2base
import findWeight4base
import os

class goodBlock():
    def __init__(self):
        self.avalacheTargetValue = 32

    def calculate(self):
        with open(os.getcwd()+'\\64py.txt', 'w') as target_f:
            target_f.write('')
        
        with open(os.getcwd()+'\\16py.txt', 'r') as f:
            for i in f:
                temp = base4recursia.Creation(eval(i))
                Sbox = temp.createSbox()

                matrix = findWeight2base.calculateWeight(Sbox).createFuns();

                self.check(matrix, Sbox, i)

    def check(self, matrix, Sbox, origSbox):        
        with open(os.getcwd()+'\\64py.txt', 'a') as target_f:
            target_f.write(str(Sbox) + '\n')
            
g = goodBlock()
g.calculate()

        

