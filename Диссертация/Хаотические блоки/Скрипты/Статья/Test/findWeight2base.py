import math

class calculateWeight():
    def __init__(self, Sbox):
        self.Sbox = Sbox;
        self.length = len(Sbox);
        self.binLength = int(math.log(self.length,2));
        self.weight_matrix = [];
        self.weight_row = [];

    def presentMatrix(self):
        for i in range(0, self.binLength):
            print(self.weight_matrix[i*self.binLength:i*self.binLength+self.binLength])

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

