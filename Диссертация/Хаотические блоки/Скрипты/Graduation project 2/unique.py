import os;
import numpy as np;

allSequences = []

with open(os.getcwd()+'//256pyUnique.txt', 'w') as f1:
    f1.write('');


with open(os.getcwd()+'//256py.txt', 'r') as f:
    for i in f:
        allSequences.append(eval(i))

unique_rows = np.unique(allSequences, axis=0)

with open(os.getcwd()+'//256pyUnique.txt', 'a') as f1:
    for i in unique_rows:
        f1.write(str(list(i)) + '\n');