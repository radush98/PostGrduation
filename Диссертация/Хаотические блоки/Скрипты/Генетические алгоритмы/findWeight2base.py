import math

from pyrsistent import l

class calculateWeight():
    def __init__(self, Sbox):
        self.Sbox = Sbox;
        self.length = len(Sbox);
        self.binLength = int(math.log(self.length,2));
        self.weight_matrix = [];
        self.weight_row = [];

    def presentMatrix(self):
        print(self.binLength)
        for i in range(0, self.binLength):
            print(self.weight_matrix[i*self.binLength:i*self.binLength+self.binLength])
            
    def integral(self):           
        return sum(self.weight_matrix) / (self.binLength * self.binLength *  self.length)
    
    def isMatrixValid(self):
        for i in self.weight_matrix:
            if i != 128:
                return False
            
        return True

    def prepareMatrix(self):
        matrix = [];
        for i in range(0, self.binLength):
            matrix.append(self.weight_matrix[i*self.binLength:i*self.binLength+self.binLength]);
        return matrix;

    def createFuns(self):
        functions = [str(bin(i)[2:].zfill(self.binLength)) for i in self.Sbox]
        for j in range(0,self.binLength):
            self.createIndex([functions[i][j] for i in range(0,self.length)])
        return self.prepareMatrix();

    def createIndex(self, bool_fun):
        indexes = [i for i in range(0,self.length)] #находим индексы
        vectors = [2**i for i in range(0,self.binLength)] #находим парметр с поочередным изменением входа
        self.xorOperation(indexes,vectors,bool_fun)


    def xorOperation(self,indexes,vectors,bool_fun):
        result = []

        for i in range(0,self.binLength):

            for j in range(0,self.length):
                result.append(indexes[j] ^ vectors[i]) #находим результат xor параметра и xor-параметра
            self.compare(bool_fun,result)
            result.clear()

    def compare(self, bool_fun, result):
        compare_fun = []
        weight = 0
        for i in range(0,self.length):
            if bool_fun[i] != bool_fun[result[i]]:
                compare_fun.append(1)
            else:
                compare_fun.append(0)
        for i in compare_fun:
            if i==1:
                weight+=1

        self.weight_matrix.append(weight)


# a = calculateWeight([0,81,243,255,166,162,170,89,174,4,251,12,85,8,247,93,97,195,207,16,178,186,105,182,20,203,28,190,24,199,109,101,211,223,32,113,138,121,134,130,219,44,142,36,215,125,117,40,239,48,65,227,73,150,146,154,60,158,52,235,77,69,56,231,145,51,63,64,226,234,153,230,68,59,76,238,72,55,157,149,3,15,80,161,250,169,246,242,11,92,254,84,7,173,165,88,31,96,177,19,185,198,194,202,108,206,100,27,189,181,104,23,112,129,35,47,214,210,218,137,222,116,43,124,133,120,39,141,115,127,128,209,42,217,38,34,123,140,46,132,119,221,213,136,79,144,225,67,233,54,50,58,156,62,148,75,237,229,152,71,160,241,83,95,6,2,10,249,14,164,91,172,245,168,87,253,193,99,111,176,18,26,201,22,180,107,188,30,184,103,205,197,191,192,17,179,25,102,98,106,204,110,196,187,29,21,200,183,208,33,131,143,118,114,122,41,126,212,139,220,37,216,135,45,49,147,159,224,66,74,57,70,228,155,236,78,232,151,61,53,163,175,240,1,90,9,86,82,171,252,94,244,167,13,5,248]);
# a.createFuns();
# a.presentMatrix();
