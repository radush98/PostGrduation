
from itertools import product
import findWeight2baseFUN

print("Started...")

etalon = [0, 0, 0, '?', 0, '?', '?', '?', 0, '?', '?', '?', '?', '?', '?', '?', 0, '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', 0, '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'];
indexes = [3, 5, 6, 7, 9, 10, 11, 12 , 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40 ,41 ,42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63];

alphabet = '01';

for i in product(alphabet, repeat=57):
    string = ''.join(i);
    test = [int(char) for char in string];
    for i in indexes:
        etalon[i] = test.pop();

    a = findWeight2baseFUN.calculateWeight(etalon);
    a.calculateFun();
    if(a.presentMatrix() == [32, 32, 32, 32, 32, 32]):
        print(etalon);


