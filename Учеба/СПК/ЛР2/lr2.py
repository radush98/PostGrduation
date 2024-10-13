import math
import itertools
import os
import ci2

class MG4:
    def __init__(self, N):
        self.N = N
        self.k = int(math.log(N, 4)) 
        self.geo_constr_sum = 4**self.k - 4*self.k
        self.possible_states = ['01', '02', '03', '20', '21', '23', '10', '12', '13', '30', '31', '32']
        self.stationary_states = ['00', '11', '22', '33']
        self.filename = 'mg4.txt'
            
    def _calcUniqueSequences(self, byte_sequence):
        unique_sequences = []
        mask_length = self.k

        for i in range(len(byte_sequence) - mask_length + 1):
           subsequence = byte_sequence[i:i + mask_length]
           if subsequence not in unique_sequences: 
               unique_sequences.append(subsequence)

        return unique_sequences
            
    def _genVariants(self, length):
        filename = 'mg4_' + str(self.N) + '_' + str(length) + '.txt'
        
        if not os.path.exists(filename):
            combinations = list(itertools.permutations(self.possible_states, length))
            
            with open(filename, 'a') as f1:
                for combination in combinations:
                    f1.write(str(list(combination)) + '\n')
          
            return combinations
        
        else:
            with open(filename, 'r') as f:
                result = []
                for line in f:
                    result.append(eval(line))
                
                return result
        
    def _calculateRequiredLength(self, geoconstr):
        counter = 0
                
        for i in geoconstr:
            if (i % 2 == 0):
                counter = counter + i / 2
            else:
                counter = counter + (i + 1) / 2
                
        return int(counter)
        
    def genBaseStructure(self, geoconstr):
        mg4 = self.stationary_states[0] + '-' * (self.N - len(self.stationary_states[0]))
        
        last_position = len(self.stationary_states[0])
        
        for index in range(0, int(self.N / (2 * 2))):            
            current_stationary_state = self.stationary_states[index]
            stationary_state_length = len(current_stationary_state)
                                   
            if index != 0:
                padding = geoconstr[index - 1] + last_position
                mg4 = mg4[:padding] + self.stationary_states[index] + mg4[padding + stationary_state_length:]
                last_position = padding + stationary_state_length
            
        return mg4
    
    def getIndexes(self, baseConstruction, geoConstr):
        result = []
        index = 2
        counter = 0
        
        for i in geoConstr:            
            if (i == 0):
                index += 2
                continue
            
            elif (i % 2 == 0):
                length = int(i / 2)
                for var in range(length):
                    result.append({"symbol":None, "index": index})
                    index += 2
                    
                if (counter < len(geoConstr) - 1):
                    index += 2
                    
            else:
                if (i != 1):
                    length = math.floor((i / 2))
                    result.append({"symbol":baseConstruction[index - 1], "index": index})
                    index += 1
                    
                    for var in range(length):
                        result.append({"symbol":None, "index": index})
                        index += 2
                        
                    if (counter < len(geoConstr) - 1):
                        index += 2

                else:
                    result.append({"symbol":baseConstruction[index - 1], "index": index})
                    index += 3
            counter += 1
        return result
    
    
    def genMGFamily(self, geoconstr):        
        requiredLength = self._calculateRequiredLength(geoconstr)
        variants = self._genVariants(requiredLength)  
        baseConstruction = self.genBaseStructure(geoconstr)
        indexes = self.getIndexes(baseConstruction, geoconstr)
        
        results = []  

        for variant in variants:
            result = baseConstruction  

            for i in range(len(indexes)):
                if indexes[i]['symbol'] is None:
                    result = (
                        result[:indexes[i]['index']]
                        + variant[i]
                        + result[indexes[i]['index'] + len(variant[i]):]
                    )
                    
                else:
                    if indexes[i]['symbol'] == variant[i][0]:
                        result = (
                            result[:indexes[i]['index'] - 1]
                            + variant[i]
                            + result[indexes[i]['index'] - 1 + len(variant[i]):]
                        )
                    else:
                        break

            temp = result.replace('-', '')

            if len(self._calcUniqueSequences(temp + temp[0])) == self.N:
                results.append(result)
                
        print('MG4 count:', len(results))
        return results
        
            
    def cyclic_shifts(self, seq):
        return [seq[i:] + seq[:i] for i in range(len(seq))]

    def canonical_form(self, seq):
        shifts = self.cyclic_shifts(seq)
        mirrored_seq = seq[::-1]
        shifts += self.cyclic_shifts(mirrored_seq)
        return min(shifts)
    
    def _formSbox(self, base4code):
        sequences = self._calcUniqueSequences(base4code + base4code[0])
        
        Sbox = []
        for sequence in sequences:
            Sbox.append(int(sequence, 4))     
        
        print(Sbox)  
        print('Correlation immune:')
        print(ci2.correlationCalc(Sbox))   
        print('------------\n')
            
    def generateSboxes(self):        
        with open(self.filename, 'r') as f:
            for i in f:
                self._formSbox(str(i).replace('\n', ''))
        

    def buildGeoConstr(self):
        alphabet = [i for i in range(0, self.geo_constr_sum + 1)]
        all_sequences = itertools.product(alphabet, repeat=4)
        valid_sequences = [seq for seq in all_sequences if sum(seq) == self.geo_constr_sum]
        unique_sequences = set()

        for seq in valid_sequences:
            canonical = self.canonical_form(seq)
            unique_sequences.add(tuple(canonical))
        
        with open(self.filename, 'w') as f, open('mg4_meta.txt', 'w') as f1:
            f.write('')
            f1.write('')
            
        with open(self.filename, 'a') as f,  open('mg4_meta.txt', 'a') as f1:
            
            for seq in sorted(unique_sequences):
                print('----', seq, '----')
                results = self.genMGFamily(list(seq))
                
                f1.write('----' + str(seq) + '----' + '\n')
                f1.write('Total:' + str(int(len(results))) + '\n')
                
                for result in results:
                    f.write(result + '\n')
                    f1.write(result + '\n')
                
                f1.write('\n')
                    
    


mg4 = MG4(16)
# mg4.buildGeoConstr()
mg4.generateSboxes()

