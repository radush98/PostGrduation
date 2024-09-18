import random
import nonlin

def getGenes(TARGET_LENGTH = 256):
    return  [i for i in range(TARGET_LENGTH)]

def initialize_pop(T, TARGET_LENGTH = 256):
    population = list()
    GENES = getGenes()

    for i in range(T):
        left_elements = GENES.copy()
        temp = list()

        for j in range(TARGET_LENGTH):
            temp.append(random.choice(left_elements))
            index = left_elements.index(temp[j])
            left_elements.pop(index)
        
        population.append(temp)

    return population

def main(T, Q):
    m = 0
    n = 0

   