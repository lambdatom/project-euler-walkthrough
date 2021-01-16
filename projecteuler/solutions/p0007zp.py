def is_prime(n): 
    assert n > 1
    for i in range(2, n): 
        if (n % i) == 0: 
            return False
    return True

def get_nth_prime_number(n):
    primes = []
    i = 2
    if n == 1: 
        return 1
    while (len(primes) < n): 
        if is_prime(i): 
            primes.append(i)
        if len(primes) == n: 
            print(primes)
            return primes[n-1]
        i+=1

def solve():    
    return get_nth_prime_number(10001)

if __name__ == "__main__": 
    print(solve())
