def sum_of_squares():
    sum = 0
    for i in range(1, 101):
        sum += i**2
    return sum

def square_of_sums(): 
    sum = 0 
    for i in range(1, 101):
        sum += i 
    return sum**2

def solve():
    return square_of_sums() - sum_of_squares()

if __name__ == "__main__": 
    solve()
