import math
import base4

class calculateWeight():
    def __init__(self,Sbox):
        self.Sbox = Sbox;
        self.length = len(Sbox);
        self.fourBaseLen = int(math.log(self.length,4));
        self.functions = []
        self.matrix = []
        #print(self.matrix)

    def presentMatrix(self):
        row_length = int(len(self.matrix)/self.fourBaseLen)
        for i in range(0,len(self.matrix),row_length):
            print(self.matrix[i:i+row_length])

    def prepareMatrix(self):
        matrix = [];
        row_length = int(len(self.matrix)/self.fourBaseLen);
        for i in range(0,len(self.matrix),row_length):
            matrix += self.matrix[i:i+row_length];
        return matrix;

    def createFuns(self):
        for i in self.Sbox:
            self.functions.append(base4.toFourBase(i,self.fourBaseLen))

        for i in range(0,self.fourBaseLen):
            self.createIndex([self.functions[j][i] for j in range(0,self.length)]);

        return self.prepareMatrix();

    def createIndex(self, fun4):
        #bool_len = len(bool_fun) #находим длину булевой функции
        #paramLen = int(math.log(length, 4)) #находим длину индекса в битах
        param = [i for i in range(0,self.length)] #находим индексы

        xor_param = []
        for i in range(0, self.fourBaseLen): #находим парметр с поочередным изменением входа
            for j in range(1,4):
                xor_param.append(4**i*j)

        self.createMatrix(param,xor_param,fun4)

    def createMatrix(self, param,xor_param,fun4):
        weigth_matrix = [] #создаем матрицу весов значений S-блока
        result = []
        for i in range(0,3*self.fourBaseLen): # 3*self.fourBaseLen 4 состояния входа для каждого входа
            for j in range(0,self.length):
                result.append(base4.xor4base([j],xor_param[i],self.fourBaseLen)) #находим результат xor параметра и xor-параметра
            #weigth_matrix.append(self.compare(fun4, result))
            self.matrix.append(self.compare(fun4, result))
        #print(result)
            result.clear()
        #print(weigth_matrix);
        #self.matrix.append(weigth_matrix)

    def compare(self, bool_fun, result):
        compare_fun = []
        for i in range(0,self.length):
            temp = int(bool_fun[result[i]]) - int(bool_fun[i])
            if temp < 0:
                temp = temp+4
            compare_fun.append(temp)
        return self.calculateWeight(compare_fun)

    def sortNums(self,statistic): #сортирует значения от 0 до 3, так как в словаре statistic они будут в разброс
        matr_row = []
        for i in range(0,4):
            try:
                matr_row.append(statistic[i])
            except:
                matr_row.append(0);
        return matr_row


    def calculateWeight(self,compare_fun):
        statistic = {}
        for i in compare_fun:
            if statistic.get(i):
                statistic[i] += 1
            else:
                statistic[i] = 1
        return self.sortNums(statistic)
