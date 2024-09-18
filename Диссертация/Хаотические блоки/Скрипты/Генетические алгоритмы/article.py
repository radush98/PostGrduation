import math
import numpy as np

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

#-------- 1 ---------

def swap_min_max(matrix, k, i, C, alpha):
    # Flatten the matrix to easily swap values
    flattened_matrix = matrix.flatten()
    
    # Indices of k minima and maxima
    print(flattened_matrix)
    min_indices = np.argpartition(flattened_matrix, k)[:k]
    print(min_indices)
    max_indices = np.argpartition(flattened_matrix, -k)[-k:]
    
    # Check conditions for swapping
    if C * np.random.rand() > alpha:
        if i % 2 == 1:
            # Swap by rows
            matrix[min_indices // matrix.shape[1], min_indices % matrix.shape[1]], matrix[max_indices // matrix.shape[1], max_indices % matrix.shape[1]] = matrix[max_indices // matrix.shape[1], max_indices % matrix.shape[1]].copy(), matrix[min_indices // matrix.shape[1], min_indices % matrix.shape[1]].copy()
        else:
            # Swap by columns
            matrix[:, min_indices % matrix.shape[1]], matrix[:, max_indices % matrix.shape[1]] = matrix[:, max_indices % matrix.shape[1]].copy(), matrix[:, min_indices % matrix.shape[1]].copy()
    
    return matrix

matrix_size = 16
my_matrix = np.random.randint(256, size=(16, 16))

for i in range(32):
    my_matrix = swap_min_max(my_matrix, k, i, C, alpha)

# ------------ 2 ---------------




# # Gauss Mutation Operator
# def gauss_mutation(solution, best_solution, C):
#     mutation = C * np.random.normal(0, 1, len(solution)) * (solution - best_solution)
#     solution += mutation

# # Cauchy Mutation Operator
# def cauchy_mutation(solution, best_solution, C):
#     mutation = C * np.random.standard_cauchy(len(solution)) * (solution - best_solution)
#     solution += mutation

# # Function to perform commutator operation
# def commutator_swap(solution, x, y):
#     solution[x], solution[y] = solution[y], solution[x]

# # Function to calculate commutator sequence
# def commutator_sequence(solution1, solution2):
#     commutators = []
#     for i in range(len(solution1)):
#         if solution1[i] != solution2[i]:
#             x = solution1.index(solution2[i])
#             commutator_swap(solution1, i, x)
#             commutators.append((i, x))
#     return commutators

# # Function to perform solution exchange using commutator sequence
# def apply_commutator_sequence(solution, commutators):
#     for commutator in commutators:
#         commutator_swap(solution, *commutator)

# # Artificial Bee Colony Algorithm with Gauss and Cauchy mutations
# def abc_algorithm(initial_solution, fitness_function, max_iterations):
#     current_solution = initial_solution.copy()
#     best_solution = current_solution.copy()
#     best_fitness = fitness_function(current_solution)

#     for iteration in range(max_iterations):
#         # Gauss Mutation (Leading Bee Stage)
#         if np.random.rand() < alpha:
#             gauss_mutation(current_solution, best_solution, C)

#         # Evaluate fitness
#         current_fitness = fitness_function(current_solution)

#         # Update best solution if needed
#         if current_fitness > best_fitness:
#             best_solution = current_solution.copy()
#             best_fitness = current_fitness

#         # Cauchy Mutation (Scouts Stage)
#         if current_fitness < best_fitness:
#             if np.random.rand() < alpha:
#                 cauchy_mutation(current_solution, best_solution, C)

#     return best_solution

# fitness_function = lambda x: sum(x)
# initial_solution = np.arange(1, SN + 1)

# best_solution = abc_algorithm(initial_solution, fitness_function, limits)
# print("Best Solution:", best_solution)

def getXn(xn, yn, zn):
    return mu * k1 * yn * (1 - xn) + zn

def getYn(xn1, yn, zn):
    return mu * k2 * yn * zn * 1/(1 + xn1 ** 2)

def getZn(xn1, yn1, zn):
    return mu * (xn1 + yn1 + k3) * math.sin(zn)






