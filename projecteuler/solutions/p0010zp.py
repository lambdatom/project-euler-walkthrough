primes = [2] 

def is_prime(n):
    assert n > 2
    x = int(n / 2) 
    for p in primes: 
        if p > x: 
            return True
        if (n % p) == 0:
            return False

def get_primes_up_to(n):
    for i in range(3, n, 2): 
        if is_prime(i):
            primes.append(i)
            print(max(primes))
    return primes

def solve(): 
     return sum(get_primes_up_to(2000000))

if __name__ == "__main__": 
    print(solve())
