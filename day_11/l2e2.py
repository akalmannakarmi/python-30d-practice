# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    if n in (0,1):
        return 1
    return n*factorial(n-1)

print(factorial(4))