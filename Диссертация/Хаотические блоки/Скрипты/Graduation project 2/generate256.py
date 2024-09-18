import findWeight2base
import findWeight4base
import findWeight2baseFUN
import base4
import base4recursia
import os

def base4ToBase2(fun4):
    temp = [bin(int(elem))[2:].zfill(2) for elem in fun4];
    binFuns = [];
    for i in range(0,2):
        binFuns.append([int(temp[j][i]) for j in range(0,len(temp))]);
    
    return binFuns;

def calculate():
    with open(os.getcwd()+'//256py.txt', 'w') as f:
        f.write('');

    results = [];

    with open(os.getcwd()+'//16py.txt', 'r') as f, open(os.getcwd()+'//256py.txt', 'a') as f1:
        for i in f:
            temp = base4recursia.Creation(eval(i))
            Sbox = temp.createSbox()

            temp.newSbox(Sbox)
            Sbox = temp.createSbox()

            a = base4.divideToFunctions(Sbox, False, 256)

            for fun in a:
                binfuns = base4ToBase2(fun);

                b1 = findWeight2baseFUN.calculateWeight(binfuns[0]);
                b1.calculateFun();

                b2 = findWeight2baseFUN.calculateWeight(binfuns[1]);
                b2.calculateFun();

                if b1.presentMatrix() == [128, 128, 128, 128, 128, 128, 128, 128] and b2.presentMatrix() == [128, 128, 128, 128, 128, 128, 128, 128]:
                    f1.write(str([int(i) for i in fun]) + '\n');

calculate()