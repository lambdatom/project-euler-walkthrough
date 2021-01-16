import math

def is_square(i):
    return i == math.isqrt(i) ** 2 

def get_pythagorean_triplet_product(): 
    triplets = []
    for a in range(1, 1001): 
        for b in range (1, 1001): 
            a_squared = a**2
            b_squared = b**2
            c_squared = a_squared + b_squared
            c = int(math.sqrt(c_squared))
            if a < b and b < c and is_square(c_squared): 
                 # We have a Pythagorean triplet
                 if (a + b + c) == 1000: 
                    # We have the only Pythagorean triplet whose members sum is 1000
                    return (a * b * c)

def solve(): 
    return get_pythagorean_triplet_product()

if __name__ == "__main__":
    print(solve())
