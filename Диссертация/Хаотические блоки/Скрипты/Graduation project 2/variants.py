
from itertools import product

etalon = [0, 0, 0, '?', 0, '?', '?', '?', 0, '?', '?', '?', '?', '?', '?', '?', 0, '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'];
indexes = [3, 5, 6, 7, 9, 10, 11, 12 , 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];

alphabet = '01';

for i in product(alphabet, repeat=26):
    string = ''.join(i);
    test = [int(char) for char in string];
    for i in indexes:
        etalon[i] = test.pop();
        print(etalon);
