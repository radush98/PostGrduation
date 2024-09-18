import random
import nonlin

POP_SIZE = 100
TARGET = 112
TARGET_LENGTH = 256
GENES = [i for i in range(TARGET_LENGTH)]

def replace_duplicates_with_unique(lst):
    length = len(lst)

    seen = set()
    for i in range(0, len(lst)):
        if lst[i] in seen:
            # If the element is a duplicate, replace all occurrences except the first one
            first_occurrence_index = lst.index(lst[i])
            for j in range(1, lst.count(lst[i])):
                unique_element = (lst[i] + j) % length
                lst[first_occurrence_index + j] = unique_element
                seen.add(unique_element)
        else:
            seen.add(lst[i])
    return lst


def initialize_pop():
    population = list()

    for i in range(POP_SIZE):
        left_elements = GENES.copy()
        temp = list()

        for j in range(TARGET_LENGTH):
            temp.append(random.choice(left_elements))
            index = left_elements.index(temp[j])
            left_elements.pop(index)
        
        population.append(temp)

    return population

def crossover(selected_chromo, population):
    offspring_cross = []
    for i in range(int(POP_SIZE)):
        parent1 = random.choice(selected_chromo)[0]
        parent2 = random.choice(population[:int(POP_SIZE*50)])[0]

        CoP1 = random.randint(0,255)
        CoP2 = random.randint(0,255)

        cnt = random.randint(1,5)

        if (cnt == 1 or cnt == 3):
            ch1 = parent1[0:CoP1] + parent2[CoP1:len(parent2)]
            ch2 = parent2[0:CoP2] + parent1[CoP2: len(parent1)]

            offspring_cross.extend([replace_duplicates_with_unique(ch1)])
            offspring_cross.extend([replace_duplicates_with_unique(ch2)])
        
        else:       
            switcher = random.randint(0,1)

            randCh1P1 = parent1[0:CoP1]
            randCh1P2 = parent2[CoP1:len(parent2)]

            randCh2P1 = parent2[0:CoP2]
            randCh2P2 = parent1[CoP2: len(parent1)]

            # random.shuffle(randCh1P1)
            # random.shuffle(randCh1P2)
            # random.shuffle(randCh2P1)
            # random.shuffle(randCh2P2)

            ch1 = randCh1P1[::-1] + randCh1P2 if switcher == 0 else randCh1P1 + randCh1P2[::-1]
            ch2 = randCh2P1[::-1] + randCh2P2 if switcher == 0 else randCh2P1 + randCh2P2[::-1]

            offspring_cross.extend([replace_duplicates_with_unique(ch1)])
            offspring_cross.extend([replace_duplicates_with_unique(ch2)])

    return offspring_cross 

def selection(population):
    sorted_chromo_pop = sorted(population, key= lambda x: x[1])
    return sorted_chromo_pop[:int(0.5*POP_SIZE)]

def fitness_cal(TARGET, chromo_from_pop):
    difference = TARGET - min(nonlin.calculateSbox(chromo_from_pop))
    return [chromo_from_pop, difference]

def replace(new_gen, population):
    for _ in range(len(population)):
        if population[_][1] > new_gen[_][1]:
          population[_][0] = new_gen[_][0]
          population[_][1] = new_gen[_][1]
    return population

def main(POP_SIZE, TARGET, GENES):
    # 1) initialize population
    initial_population = initialize_pop()
    found = False
    population = []
    generation = 1

    # 2) Calculating the fitness for the current population
    for _ in range(len(initial_population)):
        population.append(fitness_cal(TARGET, initial_population[_]))

    # now population has 2 things, [chromosome, fitness]
    # 3) now we loop until TARGET is found
    while not found:
        # 3.1) select best people from current population
        selected = selection(population)

        # 3.2) mate parents to make new generation
        population = sorted(population, key= lambda x:x[1])
        crossoveredAndMutated = crossover(selected, population)

        new_gen = []
        for _ in crossoveredAndMutated:
            new_gen.append(fitness_cal(TARGET, _))

        # 3.4) replacement of bad population with new generation
        # we sort here first to compare the least fit population with the most fit new_gen
    
        population = replace(new_gen, population)
    
        if (population[0][1] == 0):
            print('Target found')
            print('S-box: ' + str(population[0][0]) + ' Generation: ' + str(generation) + ' Fitness: ' + str(population[0][1]))
            break
        print('S-box: ' + str(population[0][0]) + ' Generation: ' + str(generation) + ' Fitness: ' + str(population[0][1]))
        generation+=1

main(POP_SIZE, TARGET, GENES)