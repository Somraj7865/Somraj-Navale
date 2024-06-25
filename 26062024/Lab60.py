# Recursion

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:


    # Recursion case
     return n * factorial(n - 1)

print(factorial(5))
