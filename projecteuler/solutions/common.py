# Return the nth Fibonacci number where F1=F2=1
# https://mathworld.wolfram.com/FibonacciNumber.html
def fibonacci(n):
    if n < 0:
        raise Exception("Invalid Fibonacci number")
    elif n == 0:
        return 0
    else:
        fn2 = 0  # Fib(n-2)
        fn1 = 1  # Fib(n-1)
        fn = 1

        for i in range(1, n):
            fn = fn1 + fn2
            fn2 = fn1
            fn1 = fn

        return fn
