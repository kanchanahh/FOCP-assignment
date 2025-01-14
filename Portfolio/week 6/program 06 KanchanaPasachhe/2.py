"""Write and test a function that takes an integer as its parameter and returns the
 factors of that integer. (A factor is an integer which can be multiplied by another to
 yield the original)."""

import math

def factor(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factor_pair = number // i
            if factor_pair != i:
                factors.append(factor_pair)
    factors.sort()
    print(factors)

number = int(input("Enter a number: "))
factor(number)