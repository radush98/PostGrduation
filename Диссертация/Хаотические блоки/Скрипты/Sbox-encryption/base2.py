import math

class base2():
    def __init__(self,Sbox):
        self.Sbox = Sbox;
        self.length = len(Sbox);
        self.binLength = int(math.log(self.length,2));

    def showFunctions(self, funcs, title, show):
        if not show:
            return

        print('\n',title)
        for i in funcs:
            print(i)

    def binaryPresentation(self):
        binSbox = [bin(i)[2:].zfill(self.binLength) for i in self.Sbox];
        return binSbox;

    def separateToFuns(self, show):
        binSbox = self.binaryPresentation();
        funcs = [];
        for j in range(0, self.binLength):
            funcs.append([binSbox[i][j] for i in range(0, self.length)]);

        self.showFunctions(funcs, 'Boolean funcs', show);
        return funcs

    def inverse(self, show):
        funcs = self.separateToFuns(show)
        newFuncs = []
        for i in funcs:
            newFuncs.append([str(int(j)^1) for j in i])

        self.showFunctions(newFuncs, 'Inversed funcs', show);
        return newFuncs

    def reverse(self, show):
        funcs = self.separateToFuns(show)
        newFuncs = []
        for i in funcs:
            newFuncs.append(i[::-1])

        self.showFunctions(newFuncs, 'Revesed funcs', show);
        return newFuncs

    def compose(self, funcs):
        self.Sbox = []
        for i in range(0, self.length):
            a= ''
            for j in range(0, self.binLength):
                a = a + funcs[j][i];
            self.Sbox.append(int(a,2))
        print('\n','New S-box:\n',self.Sbox)

    def calculateWeight(self):
        funcs = self.separateToFuns(False);
        for i in funcs:
            sum = 0;
            for j in range(0, self.length):
                sum+=int(i[j]);
            print(sum)

#-----------Additional functions---------------

def funcs2str(funcs):
    strfuncs = [];
    for f in funcs:
        F = []
        for i in range(0,len(f)):
            F.append(str(f[i]))
        strfuncs.append(F)
    return strfuncs

def funcs2int(funcs):
    intfuncs = [];
    for f in funcs:
        F = []
        for i in range(0,len(f)):
            F.append(int(f[i]))
        intfuncs.append(F)
    return intfuncs

def compose(funcs, binLength, length):
    Sbox = []
    for i in range(0, length):
        a= ''
        for j in range(0, binLength):
            a = a + funcs[j][i];
        Sbox.append(int(a,2))
    print('\n','New S-box:\n', Sbox)
    return Sbox
