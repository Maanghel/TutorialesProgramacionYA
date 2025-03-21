"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples():
    sum_multiples = 0
    for number in range(1, 1001):
        if number % 3 == 0:
            sum_multiples += number
        if number % 5 == 0:
            sum_multiples += number
    
    return sum_multiples

#########################   Main    ################################

print(multiples())