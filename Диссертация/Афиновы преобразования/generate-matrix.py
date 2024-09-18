import itertools
import os

def get_unique_combinations(numbers = [0, 1, 2], length = 3):
    if length > len(numbers):
        return []  
    
    combinations = list(itertools.permutations(numbers, length))
    combinations = [list(comb) for comb in combinations]
    
    return combinations

def clearFile(path):
    with open(os.getcwd() + path, 'w') as f:
        f.write('')

def gen1():   
    permutations = itertools.product([1,2,3], repeat=3)
    variants = get_unique_combinations()
    
    base = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    
    clearFile('\\gen1-matrix.txt')

    with open(os.getcwd()+'\\gen1-matrix.txt', 'a') as f:
        for perm in list(permutations):       
            new_base = [row[:] for row in base]
            new_base[0][2] = perm[0]
            new_base[1][1] = perm[1]
            new_base[2][0] = perm[2]

            for v in variants:            
                t = [row[:] for row in new_base]
                t[0] = new_base[v[0]]
                t[1] = new_base[v[1]]
                t[2] = new_base[v[2]]   

                f.write(str(t) + '\n')
            
def gen2():  
    permutations = list(itertools.product([1,2,3], repeat=2))
    variants = get_unique_combinations()
    
    base = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    
    clearFile('\\gen2-matrix.txt')

    with open(os.getcwd()+'\\gen2-matrix.txt', 'a') as f:
        for i in range(1, 4, 1):
            new_base = [row[:] for row in base]
            new_base[0][2] = i
            new_base[1][2] = i
            new_base[2][2] = i
                    
            for perm in permutations:       
                temp = [row[:] for row in new_base]
                temp[1][1] = perm[0]
                temp[2][0] = perm[1]

                for v in variants:            
                    t = [row[:] for row in temp]
                    t[0] = temp[v[0]]
                    t[1] = temp[v[1]]
                    t[2] = temp[v[2]]   

                    f.write(str(t) + '\n')
                    
def gen3():          
    clearFile('\\gen3-matrix.txt')

    with open(os.getcwd()+'\\gen2-matrix.txt', 'r') as f, open(os.getcwd()+'\\gen3-matrix.txt', 'a') as f1:
        for line in f:
            arr = eval(line) 
            
            for i in range(0, len(arr)):
                arr[i].reverse()
                
            f1.write(str(arr) + '\n')
                    
def gen4():   
    permutations = list(itertools.product([1,2,3], repeat=2))
    variants = get_unique_combinations()
    
    base = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    
    clearFile('\\gen4-matrix.txt')
    
    with open(os.getcwd()+'\\gen4-matrix.txt', 'a') as f:
        for i in range(1, 4, 1):
            new_base = [row[:] for row in base]
            new_base[0][1] = i
            new_base[1][1] = i
            new_base[2][1] = i

            for perm in permutations:       
                temp = [row[:] for row in new_base]
                temp[1][2] = perm[0]
                temp[2][0] = perm[1]

                for v in variants:            
                    t = [row[:] for row in temp]
                    t[0] = temp[v[0]]
                    t[1] = temp[v[1]]
                    t[2] = temp[v[2]]   

                    f.write(str(t) + '\n')
                    
gen1()
gen2()
gen3()
gen4()