"""
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:  6857
"""
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return(False)
    return(True)

def largest_prime_factor(x):
    for i in range(1, x):
        if x % i == 0 and is_prime(int(x/i)):
            return(int(x/i))

print(largest_prime_factor(600851475143))
