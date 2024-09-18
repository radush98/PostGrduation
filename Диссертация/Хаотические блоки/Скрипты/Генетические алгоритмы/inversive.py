
def inversive(Sbox):
    inverse_s_box = [0] * 256
    for i, val in enumerate(Sbox):
        inverse_s_box[val] = i
    
    return inverse_s_box