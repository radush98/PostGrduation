import numpy as np

def chaotic_map(g, x, N):
    e1 = (1/2) - np.sqrt((1/4) - np.floor(g/4)/g)
    e2 = (1/2) + np.sqrt((1/4) - np.floor(g/4)/g)
    x_values = [x]
    
    for i in range(N):
        if g <= 4:
            x_values.append(g * x_values[-1] * (1 - x_values[-1]))
        else:
            if e1 <= x_values[-1] <= e2:
                x_values.append(np.mod(g * x_values[-1] * (1 - x_values[-1]), 1) / np.mod(g/4, 1))
            else:
                x_values.append(np.mod(g * x_values[-1] * (1 - x_values[-1]), 1))
    
    return np.array(x_values)

def generate_binary_sequence(x_values):
    binary_sequence = []
    
    for val in x_values:
        if 0.1 <= val <= 0.6:
            binary_sequence.append(int(np.mod(val * 10**10, 1) >= 0.5))
    
    return np.array(binary_sequence)

def hyperChaos(N):
    g = 4

    x_values = chaotic_map(g, 0.7, N)
    binary_sequence = generate_binary_sequence(x_values)
    
    return binary_sequence