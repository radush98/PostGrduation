import base4recursia;
import os;

with open(os.getcwd() + '//256npy.txt', 'w') as f1:
    f1.write('')

with open(os.getcwd()+'//16py.txt', 'r') as f, open(os.getcwd() + '//256npy.txt', 'a') as f1:
    for i in f:
        temp = base4recursia.Creation(eval(i))
        Sbox = temp.createSbox()

        temp.newSbox(Sbox)
        Sbox = temp.createSbox()

        f1.write(str(Sbox).replace(' ', ''))
        f1.write('\n')
