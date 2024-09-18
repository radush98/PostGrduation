import numpy as np

def replace_duplicates(arr):
    unique_values = np.arange(256)
    np.random.shuffle(unique_values)

    _, idx, counts = np.unique(arr, return_inverse=True, return_counts=True)
    duplicates = np.where(counts > 1)[0]

    for dup in duplicates:
        replace_values = unique_values[:counts[dup]-1]
        if(idx == dup):
            arr[idx] = replace_values

    return arr

# Example usage:
original_array = np.array([1, 2, 3, 4, 2, 6, 3, 7, 2])
result_array = replace_duplicates(original_array)
print(result_array)