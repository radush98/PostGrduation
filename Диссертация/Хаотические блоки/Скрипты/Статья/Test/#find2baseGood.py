import findWeight2base
from itertools import permutations

for i in permutations([0,1,2,3,4,5,6,7], r=8):
    sample = [j for j in i];
    a = findWeight2base.calculateWeight(sample);
    if a.createFuns() == [[4,4,4],[4,4,4],[4,4,4]]:
        print(sample);

    #print(b)

'''a = findWeight2base.calculateWeight([0,1,2,3,4,5,6,7]);
print(a.createFuns());'''