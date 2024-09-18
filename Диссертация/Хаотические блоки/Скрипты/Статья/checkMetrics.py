import summary_class;

def main():    
    with open('bijective-test-2.txt', 'r') as f:
        s = set()
        for line in f:
            s.add(line)
            
        s = list(s)   
            
        for box in s:
            Sbox = eval(box)   
            s = summary_class.Summary(Sbox)
            s.calc()
main()

 


    
    