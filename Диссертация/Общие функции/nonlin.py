import math
import numpy
import base2
from scipy.linalg import hadamard

class nonlin2():
    def __init__(self, boolean):
        self.prepareBoolean(boolean)
        self.length = len(boolean);
        self.pow = int(math.log(self.length,2));

    def multiplicate(self, X,Y):
        X = numpy.array(X);
        Y = numpy.array(Y);
        return X.dot(Y)

    def getDistance(self):
        H = hadamard(self.length);
        res = self.multiplicate(self.boolean, H);
        res = [abs(i) for i in res];

        N = 2**(self.pow - 1) - max(res)/2;
        return int(N)

    def prepareBoolean(self, boolean):
        self.boolean = [];
        for i in boolean:
            if i == 1:
                self.boolean.append(-1);
            else:
                self.boolean.append(1);


def calculateSbox(Sbox):
    Sbox = base2.base2(Sbox);
    funcs = Sbox.separateToFuns(False);
    funcs = base2.funcs2int(funcs);

    distances = []
    for fun in funcs:
        distance = nonlin2(fun);
        distances.append(distance.getDistance());

    return distances





