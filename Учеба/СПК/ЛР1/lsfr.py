import math

def getIndexes(polinom):
    polinom.reverse();
    return [i for i in range(0,len(polinom)-1) if polinom[i]==1];

def enlarge(key, length, polinom):
    indexes = getIndexes(polinom);
    gamma = key;
    for i in range(0, length-len(key)):
        gamma.append(multipleXor(gamma,i,indexes));
    return gamma

def multipleXor(gamma, iterator, indexes):
    res = gamma[iterator + indexes[0]];
    for i in range(1, len(indexes)):
        res = int(math.fmod(res + gamma[indexes[i] + iterator], 2))
    return res