import math
import numpy as np
import os
import ci2

class MG():
    def __init__(self, N):
        self.N = N
        self.k = int(math.log2(N)) 
        self.max_unique = 2 ** self.k
            
        self.MIN_10 = 2**(N - self.k - 1) + 2**(N - 2 * self.k) + 1
        self.MAX_10 = self.MIN_10 + 2**(N - self.k -1)
        self.fileName = 'deBrein-' +  str(self.k) + '.txt'

        
    def _autocorrelation(self, x):
        result = np.correlate(x, x, mode='full')
        acf = result[result.size // 2:]
    
        side_lobes = acf[1:]
        max_side_lobe = np.max(np.abs(side_lobes))
        
        print("Autocorrelation function:", acf)
        print("The maximum amplitude of the side lobe:", max_side_lobe)
        
    def _checkData(self):
        if not os.path.exists(self.fileName):
            print(f"File {self.fileName} not found. Calculating values...")
            self.generateMg()        
        
    def _calcUniqueSequences(self, byte_sequence):
        unique_sequences = []
        mask_length = self.k

        for i in range(len(byte_sequence) - mask_length + 1):
           subsequence = byte_sequence[i:i + mask_length]
           if subsequence not in unique_sequences: 
               unique_sequences.append(subsequence)

        return unique_sequences
    
    def _formSbox(self, binary):
        sequences = self._calcUniqueSequences(binary + binary[0:self.k])
        Sbox = []
        for sequence in sequences:
            Sbox.append(int(sequence, 2))
        
        print(Sbox)  
        print('\nCorrelation immune:')
        print(ci2.correlationCalc(Sbox))   
         
            
    def generateSboxes(self):
        self._checkData()
        
        with open(self.fileName, 'r') as f:
            for i in f:
                binary = bin(int(i))[2::].zfill(self.N)
                self._formSbox(binary)
        
    
    def calculateAutocorrelation(self):  
        self._checkData()
                     
        with open(self.fileName, 'r') as f:
            for i in f:
                binary = bin(int(i))[2::].zfill(self.N)
                binary_array = np.array([int(bit) for bit in binary], dtype=int)
                self._autocorrelation(binary_array)
        
    def checkBalanceWeight(self, binary):
        ones = binary.replace('0','')
        zeros = binary.replace('1','')
        res = len(ones) == len(zeros)
        
        return res
    
    def count_unique_byte_sequences(self, byte_sequence):       
        unique_sequences = self._calcUniqueSequences(byte_sequence)
        return len(unique_sequences) == self.max_unique
        
    def generateMg(self):   
        with open(self.fileName, 'w') as f:
            f.write('')   
            
        with open(self.fileName, 'a') as f:
            for i in range(self.MIN_10, self.MAX_10, 2):
                binary = bin(i)[2::].zfill(self.N)

                check = self.checkBalanceWeight(binary) and self.count_unique_byte_sequences(binary + binary[0:self.k])

                if (check):
                    print(i)
                    f.write(str(i) + '\n')
                    
            
mg = MG(32)
mg.generateMg() #Generation
# mg.calculateAutocorrelation() #Autocorrelation calc
# mg.generateSboxes() #S-boxes generation
            
            
            
            