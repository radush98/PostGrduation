import summary_class;

def main():    
    with open('bijective-test-2.txt', 'r') as f:
        s = set()
        for line in f:
            s.add(line.replace(
                '\n', ''
            ))
            
    print(s)
main()

 


    
    