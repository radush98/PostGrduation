import os
import base4


def calculateBalance(seq):
    statistic = {}
    for i in seq:
        if statistic.get(i):
            statistic[i] += 1
        else:
            statistic[i] = 1

    matr_row = []
    for i in range(0, 4):
        try:
            matr_row.append(statistic[i])
        except:
            matr_row.append(0)

    return matr_row


def funcSum(fun1, fun2):
    return [(fun1[i] + fun2[i]) % 4 for i in range(0, len(fun1))]

allSequences = []

with open(os.getcwd()+'//256py.txt', 'r') as f:
    for i in f:
        allSequences.append(eval(i))

with open(os.getcwd()+'//256S.txt', 'w') as f:
    f.write('')

length = len(allSequences)


with open(os.getcwd()+'//256S.txt', 'a') as f:
    for i in range(0, length):
        temp1 = allSequences[i]
        print("Current block >>>", i);
        for j in range(i+1, length):
            temp2 = allSequences[j]
            if calculateBalance(funcSum(temp1, temp2)) == [64, 64, 64, 64]:
                for k in range(j+1, length):
                    temp3 = allSequences[k]
                    if calculateBalance(funcSum(temp1, temp3)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp2, temp3)) == [64, 64, 64, 64]:
                        for l in range(k+1, length):
                            temp4 = allSequences[l]
                            if calculateBalance(funcSum(temp1, temp4)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp2, temp4)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp3, temp4)) == [64, 64, 64, 64]:
                                Sbox = base4.compose([
                                    temp1,
                                    temp2,
                                    temp3,
                                    temp4
                                ]);

                                Su = set(Sbox);
                                if (len(Su) == 256):
                                    print(Sbox);
                                    f.write(str(Sbox) + '\n');
                                break
