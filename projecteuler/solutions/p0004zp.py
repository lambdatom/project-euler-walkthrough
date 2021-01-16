def find_products():
    products = []
    rx = range(100,999)
    ry = range(100,999)
    for i in rx:
        for j in ry: 
            products.append(i * j)
    return products
    
def is_palindrome(n): 
    s = str(n)
    return s == s[::-1]

def find_largest_palindrome():
    max = 0 
    palindromes = []
    for n in find_products(): 
        if is_palindrome(n): 
            palindromes.append(n)
        if is_palindrome(n) and n > max: 
            max = n
    print("palindromes:", palindromes, "max:", max)
    return max

def solve(): 
    print(find_largest_palindrome())

if __name__ == "__main__": 
    solve()
