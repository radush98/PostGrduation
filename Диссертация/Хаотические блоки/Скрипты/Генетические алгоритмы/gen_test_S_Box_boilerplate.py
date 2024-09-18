import random
import nonlin

POP_SIZE = 500
TARGET = 112
TARGET_LENGTH = 256
GENES = [i for i in range(TARGET_LENGTH)]

def get_unique_in_order(seq):
    print("Seq >>> ", seq)
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

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
        parent1 = random.choice(selected_chromo)
        parent2 = random.choice(population[:int(POP_SIZE*50)])

        genes_mix = [element for pair in zip(parent1[0], parent2[0]) for element in pair]
        child = get_unique_in_order(genes_mix)
        offspring_cross.extend([child])
    return offspring_cross 

def mutate(offspring):
    mutated_offspring = []

    for arr in offspring:
        random.shuffle(arr)
        mutated_offspring.append(arr)
    return mutated_offspring

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
        crossovered = crossover(selected, population)
            
        # 3.3) mutating the childeren to diversfy the new generation
        mutated = mutate(crossovered)

        new_gen = []
        for _ in mutated:
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