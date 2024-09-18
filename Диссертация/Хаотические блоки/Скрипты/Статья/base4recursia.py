import base4
import shift
import math
import findWeight4base
import findWeight2base

class Creation():
    def __init__(self,Sbox):
        self.origSbox = Sbox;
        self.length = len(Sbox);
        self.k = int(math.log(self.length, 4));

    def createDiad(self):
        d = 1;
        diad = [];
        for j in range(0,4):
            diad.append([base4.xor4base([x],base4.multiplication([d],j,self.k),self.k) for x in range(0,self.length)]);
        self.diad = diad;

    def createG1(self):
        oldest = base4.divideToFunctions(self.origSbox, True, self.length);
        self.G1 = oldest;
        for c in range(1,4):
            self.G1 += [base4.xor4base([oldest[i]], c, self.k) for i in self.diad[c]];

    def createG0(self):
        self.G0 = self.origSbox;
        for i in range(1,4):
            self.G0 += [self.origSbox[j] for j in self.diad[i]]

    def createSbox(self):
        self.createDiad();
        self.createG0();
        self.createG1();

        Sbox = [self.G1[i] * (4**self.k) + self.G0[i]  for i in range(0, self.length*4)];
        return Sbox

    def newSbox(self,Sbox):
        self.origSbox = Sbox;
        self.length = len(Sbox);
        self.k = int(math.log(self.length, 4));






