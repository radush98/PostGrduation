import os
import base4
import base2


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

with open(os.getcwd()+'//256pyUnique.txt', 'r') as f:
    for i in f:
        allSequences.append(eval(i))

with open(os.getcwd()+'//256S.txt', 'w') as f:
    f.write('')

length = len(allSequences)

with open(os.getcwd()+'//256S.txt', 'a') as f:
    for i in range(0, length):
        temp1 = allSequences[i]
        print("Current block >>>", i)
        for j in range(i+1, length):
            temp2 = allSequences[j]
            # if calculateBalance(funcSum(temp1, temp2)) == [64, 64, 64, 64]:
            for k in range(j+1, length):
                temp3 = allSequences[k]
                  # if calculateBalance(funcSum(temp1, temp3)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp2, temp3)) == [64, 64, 64, 64]:
                for l in range(k+1, length):
                    temp4 = allSequences[l]
                      # if calculateBalance(funcSum(temp1, temp4)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp2, temp4)) == [64, 64, 64, 64] and calculateBalance(funcSum(temp3, temp4)) == [64, 64, 64, 64]:
                    Sbox = base4.compose([
                         temp1,
                         temp2,
                         temp3,
                         temp4
                         ])
                    Su = set(Sbox)
                    if (len(Su) == 256):
                        f.write(str(Sbox) + '\n')
                    break
# ---------------------------------- Version 2 -----------------------------------

# def funcSum(fun1, fun2):
#     tf1 = base2.base2(fun1)
#     tf2 = base2.base2(fun2)

#     ff1 = tf1.separateToFuns(False)[-2:]
#     ff2 = tf2.separateToFuns(False)[-2:]

#     f11 = [int(i) for i in ff1[0]]
#     f12 = [int(i) for i in ff1[1]]

#     f21 = [int(i) for i in ff2[0]]
#     f22 = [int(i) for i in ff2[1]]

#     print(f11)
#     print(f12)
#     print(f21)
#     print(f22)

#     res1 = [(f11[i] + f21[i]) % 2 for i in range(0, len(fun1))]
#     res2 = [(f11[i] + f22[i]) % 2 for i in range(0, len(fun1))]
#     res3 = [(f12[i] + f21[i]) % 2 for i in range(0, len(fun1))]
#     res4 = [(f12[i] + f22[i]) % 2 for i in range(0, len(fun1))]
#     # res5 = [(f11[i] + f12[i]) % 2 for i in range(0, len(fun1))]
#     # res6 = [(f21[i] + f22[i]) % 2 for i in range(0, len(fun1))]

#     return [
#         sum(res1),
#         sum(res2),
#         sum(res3),
#         sum(res4)
#     ]


# allSequences = []

# with open(os.getcwd()+'//256pyUnique.txt', 'r') as f:
#     for i in f:
#         allSequences.append(eval(i))

# with open(os.getcwd()+'//256S.txt', 'w') as f:
#     f.write('')

# length = len(allSequences)

# with open(os.getcwd()+'//256S.txt', 'a') as f:
#     for i in range(0, length):
#         temp1 = allSequences[i]
#         print("Current block >>>", i)
#         for j in range(i+1, length):
#             temp2 = allSequences[j]
#             if funcSum(temp1, temp2) == [128, 128, 128, 128]:
#                 for k in range(j+1, length):
#                     temp3 = allSequences[k]
#                     if funcSum(temp1, temp3) == [128, 128, 128, 128] and funcSum(temp2, temp3) == [128, 128, 128, 128]:
#                         for l in range(k+1, length):
#                             temp4 = allSequences[l]
#                             if funcSum(temp1, temp4) == [128, 128, 128, 128] and funcSum(temp2, temp4) == [128, 128, 128, 128] and funcSum(temp3, temp4) == [128, 128, 128, 128]:
#                                 Sbox = base4.compose([
#                                     temp1,
#                                     temp2,
#                                     temp3,
#                                     temp4
#                                 ])

#                                 f.write(str(Sbox) + '\n')
