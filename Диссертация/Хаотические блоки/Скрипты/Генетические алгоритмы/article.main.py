import math
import numpy as np
import random

SN = 10 # colony size
C = 0.5 # adjustment parameter
alpha = 0.2 # constant
limits = 10 # iteration limits
k = 3

x0 = 0.34 
y0 = 0.27
z0 = 0.75
k1 = 39.7
k2 = 40
k3 = 38.5
N0 = 500 # transfer effect elimination
mu = 1.5 

#----------- 1 LOGISTIC MAP --------------

def getXn(xn, yn, zn):
    return mu * k1 * yn * (1 - xn) + zn

def getYn(xn1, yn, zn):
    return mu * k2 * yn * zn * 1/(1 + xn1 ** 2)

def getZn(xn1, yn1, zn):
    return mu * (xn1 + yn1 + k3) * math.sin(zn)

def getZ(x, y, z):
    x1 = getXn(x, y , z)
    y1 = getYn(x1, y, z)
    z1 = getZn(x1, y1, z)
    return [x1, y1, z1]

Z = [[x0, y0, z0]]
for i in range(1, 255):
    currentIndex = i -1
    x = Z[currentIndex][0]
    y = Z[currentIndex][1]
    z = Z[currentIndex][2]

    Z.append(getZ(x, y, z))

#----------- 2 SWAP FUNCTION ------------

def swap_min_max(matrix, k, i, C, alpha):
    flattened_matrix = matrix.flatten()
    
    min_indices = np.argpartition(flattened_matrix, k)[:k]
    max_indices = np.argpartition(flattened_matrix, -k)[-k:]
    
    if C * np.random.rand() > alpha:
        if i % 2 == 1:
            # Swap by rows
            matrix[min_indices // matrix.shape[1], min_indices % matrix.shape[1]], matrix[max_indices // matrix.shape[1], max_indices % matrix.shape[1]] = matrix[max_indices // matrix.shape[1], max_indices % matrix.shape[1]].copy(), matrix[min_indices // matrix.shape[1], min_indices % matrix.shape[1]].copy()
        else:
            # Swap by columns
            matrix[:, min_indices % matrix.shape[1]], matrix[:, max_indices % matrix.shape[1]] = matrix[:, max_indices % matrix.shape[1]].copy(), matrix[:, min_indices % matrix.shape[1]].copy()
    
    return matrix

#--------- 4 PROBABILITY OF ONLOOKERS ----------

def onlooker_selection(food_sources):
    max_fitness = max(food_source['fitness'] for food_source in food_sources)
    
    probabilities = [0.9 + food_source['fitness'] / max_fitness * 0.1 for food_source in food_sources]
    
    # Roulette wheel selection
    selected_index = roulette_wheel_selection(probabilities)
    
    return food_sources[selected_index]

def roulette_wheel_selection(probabilities):
    rand_value = random.uniform(0, 1)
    cumulative_prob = 0
    
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if rand_value <= cumulative_prob:
            return i

# Example usage:
food_sources = [{'fitness': 10}, {'fitness': 15}, {'fitness': 8}]
selected_food_source = onlooker_selection(food_sources)
print(f"Selected Food Source: {selected_food_source}")

#--------- 5 FITNESS FUNCTION -----------

def fitness_function(Ns, delta_s):
    if Ns < 90 and delta_s > 18:
        return Ns - delta_s
    elif Ns < 90 and delta_s <= 18:
        return Ns - 2 * delta_s
    elif Ns >= 90 and delta_s > 18:
        return Ns - delta_s
    elif Ns >= 90 and delta_s <= 18:
        return Ns - 2 * delta_s
    else:
        return 0










