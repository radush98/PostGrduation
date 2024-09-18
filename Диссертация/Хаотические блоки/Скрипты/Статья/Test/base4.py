import math

def inverse(Sbox):
    length = len(Sbox);
    binlength = int(math.log(length,4));
    funcs = divideToFunctions(Sbox, False, length);
    newSbox = [];

    for i in range(0,length):
        temp = ' '
        for j in range(0, binlength):
            temp += str(xor4base([3], int(funcs[j][i]), binlength));
        newSbox.append(int(temp,4))

    print(newSbox);


def divideToFunctions(Sbox, getOldest, length):
    fourBaseLen = int(math.log(length,4));
    functions = []

    for i in Sbox:
        functions.append(toFourBase(i,fourBaseLen));

    if getOldest ==True:
        return [int(functions[j][-1]) for j in range(0,length)]

    funcs = [];
    for i in range(0,fourBaseLen):
        #print([functions[j][i] for j in range(0,length)]);
        funcs.append([functions[j][i] for j in range(0,length)])
        #funcs.append([functions[j][i] for j in range(0,len(Sbox)])
    return funcs

def toFourBase(number, length): #перевод в четверичную систему
    b = ''
    while number > 0:
        b = str(number % 4) + b
        number = number//4
    return b.zfill(length)

def numToList(first, last, paramLen):
    first = toFourBase(first.pop(),paramLen)[::-1] #переводим в 4 систему индекс и обращаем строку для удобства операции xor
    last = toFourBase(last,paramLen)[::-1]#переводим в 4 систему n-ое изменение i-го входа и обращаем строку для удобства операции xor
    return first,last

def xor4base(first, last, paramLen):
    res = 0
    dec = 1
    first, last = numToList(first, last, paramLen)
    for i in range(0,len(last)):
        res = res + dec * int(math.fmod(int(first[i]) + int(last[i]),4))
        dec = 10**(i+1)
    return int(str(res),4)

#----------------------Test----------------------------
def multiplication(first, last, paramLen):
    res = 0
    dec = 1
    first, last = numToList(first, last, paramLen)
    for i in range(0,len(last)):
        res = res + dec * int(math.fmod(int(first[i]) * int(last[i]),4))
        dec = 10**(i+1)
    return int(str(res),4)

print(multiplication([1],1,2))

#print(multiplication([4],5,2))