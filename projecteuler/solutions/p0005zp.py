def find_evenly_divisible_n(): 
    evenly_divisible_n = []
    for n in range (1, 1000000000): 
        evenly_divisible = True
        for i in range(1,20): 
            if n % i != 0: 
                #print(n, "is not divisible by", i, n % i)
                evenly_divisible = False
                break
        if evenly_divisible == True: 
            print(n, "is evenly divisible by all numbers from 1-20")
            evenly_divisible_n.append(n) 
    return evenly_divisible_n

def solve(): 
    print(find_evenly_divisible_n())

if __name__ == "__main__": 
    solve()
