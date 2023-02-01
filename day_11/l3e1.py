# Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True