





def collatz_sequence(n): 
    sequence = []
    i = n
    while i > 1: 
        if i % 2 == 0: 
            next_item = int(i/2)
            sequence.append(next_item)
        else: 
            next_item = (i*3) + 1 
            sequence.append(next_item)
        i = next_item
    return sequence

def solve(): 
    return collatz_sequence(15)

if __name__ == "__main__": 
    print(solve())
