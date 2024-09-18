import numpy as np
import base4 as b4
import findWeight2base as f2
import findWeight4base as f4
import nonlin as n2
import nonlin4 as n4
    
gf_4_sum = [
    [0, 1, 2, 3],
    [1, 0, 3, 2],
    [2, 3, 0, 1],
    [3, 2, 1, 0],
]

gf_4_mult = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
]

def sumElements(elem1, elem2):
    return gf_4_sum[elem1][elem2]

def multElements(elem1, elem2):
    return gf_4_mult[elem1][elem2]

import summary_class;

def main():   
    base_matrix = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

    # with open('bijective-test-2.txt', 'r') as f:
    #     s = set()
    #     for line in f:
    #         s.add(line)
            
    #     s = list(s)   
            
    #     for box in s:
    #         Sbox = eval(box)   
    #         s = summary_class.Summary(Sbox)
    #         s.calc()
main()


 


    
    