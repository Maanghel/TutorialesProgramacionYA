"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
"""

def largest_prime_factor(n):
    factor = 2
    
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor 
        else:
            factor += 1
    
    return n

#########################   Main    ################################

print(largest_prime_factor(600851475143))