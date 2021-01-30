import math

def get_divisors(x):
    divisors = []
    i = 1
    # Iterate from 1 to the square root of the target number
    while i <= math.sqrt(x):
        # Only consider numbers that cleanly divide the target number
        if (x % i == 0):
            # If target number is 100, for example, 100 / 10 == 10, so only add 10 as a divisor once
            if (x / i == i): 
                divisors.append(i)
            else: 
                # Otherwise, we have found a pair of divisors to add to the list
                divisors.append(i)
                divisors.append(int(x/i))
        i = i + 1
    return len(divisors)

def get_triangle_numbers(target_factor_count): 
    for x in range(1, 1000000): 
        triangle_number = int((x * (x + 1)) / 2)
        num_factors = get_divisors(triangle_number)
        print("Found {} factors for triangle number: {}".format(num_factors, triangle_number))
        if num_factors > target_factor_count: 
            print("Found Target triangle number: {} which has more than {} factors".format(triangle_number, target_factor_count))
            return True

def solve():
   return get_triangle_numbers(500)

if __name__ == "__main__": 
    print(solve())
